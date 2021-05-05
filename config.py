import os

class Config:
    pass
    # we change to our own databases 
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mugera:Mugbwo9856@localhost/letewa'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://githui:Kqcaptain#2@localhost/letewa'

    


class ProdConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = "postgresql://vzptjkvwwukqax:9f863d965fec49851c9daa903a53bb7d5acb267c1ea1d19ea0012b73ff9e1f65@ec2-34-225-167-77.compute-1.amazonaws.com:5432/ddjuf4iqfo6c55?sslmode=require"


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
