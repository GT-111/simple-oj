import redis


class Config:
    #General
    FLASK_ENV = 'debug'

    # Session and Redis
    # redis://:[password]@[host_url]:[port].
    # SECRET_KEY = 'sandevistan'
    # REDIS_URI = 'redis://:admin@localhost:6379'
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = redis.from_url(REDIS_URI)




    # MongoDB
    MONGODB_SETTINGS = {
        'db': 'oj',
        'host': 'localhost',
        'port': 27017
    }

    # MySQL
    # mysql+pymysql://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE_NAME]
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@localhost:3306/oj'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
