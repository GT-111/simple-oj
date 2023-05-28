# OSS Authentication #
import oss2
from sqlalchemy import select

auth = oss2.Auth('LTAI5tKQF3nNp9hNafr2QmAs', '3b4s0o4NgAXEmmdv63bFlRXkECQkHq')
bucket = oss2.Bucket(auth, 'https://oss-cn-shenzhen.aliyuncs.com', 'simple-oj')

# bucketConfig = oss2.models.BucketCreateConfig(oss2.BUCKET_STORAGE_CLASS_STANDARD, oss2.BUCKET_DATA_REDUNDANCY_TYPE_ZRS)
# bucket.create_bucket(oss2.BUCKET_ACL_PRIVATE, bucketConfig)
bucket.create_bucket()

# OSS Authentication #


from flask import request, jsonify
from flask_login import login_required, current_user

from response import Response
from database import sql
from extentions import login_manager, bcrypt
from problem.model import Problem, ProblemModel
from upload.model import Upload, UploadModel, Oss, OssModel
from upload import upload_view


def get_max_id_plus1():
    max_id_oss = Oss.query.order_by(Oss.id.desc()).first()
    if max_id_oss:
        return max_id_oss.id + 1
    else:
        return 1


def get_oss_by_id(_id: int):
    oss = sql.session.execute(select(Oss).where(Oss.id == _id))
    return oss.fetchone()[0]


def get_problem_by_id(_id: int):
    problem = sql.session.execute(select(Problem).where(Problem.id == _id))
    return problem.fetchone()[0]


@upload_view.route('/assignment', methods=['POST'])
def assignment():
    content = request.get_json()
    # { 'user_id': 2, 'oss_id': 3, 'context_id': 4 }
    r = Response()
    temp_oss = get_oss_by_id(content['oss_id'])
    try:
        upload_model = UploadModel(**content)
    except ValueError:
        r.message = 'invalid param'
        r.status_code = 406
        return r.to_json()
    print(content['user_id'])
    temp_oss.user_id = content['user_id']
    upload_dict = upload_model.dict()
    temp_upload = Upload(**upload_dict)
    sql.session.add(temp_upload)
    r.data = temp_upload.to_json()
    sql.session.commit()
    return r.to_json()


@upload_view.route('/zip', methods=['POST'])
def zip():
    content = request.get_json()
    # { 'oss_id': 3, 'problem_id': 2 }
    r = Response()
    temp_oss: Oss = get_oss_by_id(content['oss_id'])
    temp_problem: Problem = get_problem_by_id(content['problem_id'])
    print(content['user_id'])
    temp_oss.user_id = content['user_id']
    temp_problem.oss_id = content['oss_id']
    sql.session.commit()
    r.data = temp_problem.to_json()
    return r.to_json()


@upload_view.route('/upload_zip', methods=['POST'])
def upload_zip():
    r = Response()
    f = request.files.get('file')
    if f.filename != '':
        print(f.filename)
        serial = str(get_max_id_plus1()) + '.zip'
        bucket.put_object(serial, f)
        r.status_code = 200
        oss_model = OssModel(user_id=-1, type='zip')
        oss_dict = oss_model.dict()
        temp_oss = Oss(**oss_dict)
        sql.session.add(temp_oss)
        sql.session.commit()
        r.status_code = 200
        r.data = serial
    else:
        r.message = 'no file uploaded'
        r.status_code = 400
    return r.to_json()


@upload_view.route('/upload_assignment', methods=['POST'])
def upload_assignment():
    r = Response()
    f = request.files.get('file')
    if f.filename != '':
        print(f.filename)
        serial = str(get_max_id_plus1())
        bucket.put_object(serial, f)
        r.status_code = 200
        oss_model = OssModel(user_id=-1, type='assignment')
        oss_dict = oss_model.dict()
        temp_oss = Oss(**oss_dict)
        sql.session.add(temp_oss)
        sql.session.commit()
        r.status_code = 200
        r.data = serial
    else:
        r.message = 'no file uploaded'
        r.status_code = 400
    return r.to_json()
