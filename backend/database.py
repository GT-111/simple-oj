from flask_mongoengine import MongoEngine

db = MongoEngine()

# class CURDMixin(object):
#
#     @classmethod
#     def get_by_id(cls, id: str):
#         if isinstance(id, str):
#             return cls.objects(id=id).first()
#
#     @classmethod
#     def create(cls, **kwargs):
#         instance = cls(**kwargs)
#         return instance.save()
#
#     @classmethod
#     def delete(cls, id: str):
#         if isinstance(id, str):
#             return cls.delete()
