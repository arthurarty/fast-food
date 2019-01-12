"""
module config
"""
import os


class Config:
    """
    parent config class
    """
    DEBUG = False
    JWT_SECRET_KEY = 'qweBas12@!asBASD'


class DevelopmentConfig(Config):
    """
    class for development configuration
    """
    DEBUG = True
    DATABASE_URL = os.environ.get(
        'DATABASE_URL') or 'postgres://postgres:qwe@localhost:5432/fastfood'


class TestingConfig(Config):
    """
    class for testing configuration
    """
    DEBUG = True
    DATABASE_URL = 'postgres://postgres:qwe@localhost:5432/fastfood'
