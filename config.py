import os

class Config:
    pass
  

    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    


class ProdConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = "postgresql://vzptjkvwwukqax:9f863d965fec49851c9daa903a53bb7d5acb267c1ea1d19ea0012b73ff9e1f65@ec2-34-225-167-77.compute-1.amazonaws.com:5432/ddjuf4iqfo6c55?sslmode=require"


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://mugera:Mugbwo9856@localhost/letewa-test'

class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugera:Mugbwo9856@localhost/letewa'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig,
}

