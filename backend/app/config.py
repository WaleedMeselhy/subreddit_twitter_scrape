from flask_env import MetaFlaskEnv


class BaseConfig(metaclass=MetaFlaskEnv):
    ENV_PREFIX = ''
    ENV_LOAD_ALL = False
    SCRAPYD_HOST = ''
    ELASTICSEARCH_HOST = ''

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


class StagingConfig(BaseConfig):
    """Staging configuration"""
    DEBUG = False


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
