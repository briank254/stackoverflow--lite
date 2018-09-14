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
    DATABASE = os.getenv('TEST_DB')

class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    DATABASE = os.getenv('TEST_DB') or 'postgresql://gray:graycadeau@localhost/stackoverflow_lite'

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