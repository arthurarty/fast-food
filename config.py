"""
module config
"""
class Config:
    """
    parent config class
    """
    DEBUG = False

class DevelopmentConfig(Config):
    """
    class for development configuration
    """
    DEBUG = True
    DATABASE_URL = 'postgresql://localhost/fastfood'
class TestingConfig(Config):
    """
    class for testing configuration
    """
    DEBUG = True
    DATABASE_URL = 'postgresql://localhost/test'