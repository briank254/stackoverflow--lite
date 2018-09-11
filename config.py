"""
Application configuration settings
"""
import os

class Config:
    """
    Common configurations
    """ 
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    DATABASE = os.getenv('TEST_DB')

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}