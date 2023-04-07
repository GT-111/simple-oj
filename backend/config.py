class Config:
    # General
    SECRET_KEY = 'sandevistan'
    FLASK_ENV = 'debug'

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
