from database import sql


def get_by_user_id(_id: int):
    enrolls = sql.session.execute(select(Enroll))