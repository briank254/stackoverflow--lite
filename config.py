"""
Application configuration settings
"""
import os

class Config:
    """
    Common configurations
    """ 
    DEBUG = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    DATABASE = os.getenv('DEVELOPMENT_DB') or 'postgresql://test:testpassword@localhost/test_db'

class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    DATABASE = os.getenv('TEST_DB') or 'postgresql://test:testpassword@localhost/test_db'

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    DATABASE = os.getenv('DATABASE_URL')

CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}