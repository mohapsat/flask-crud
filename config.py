class Config(object):
    """
    common configurations
    """

    # Put configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    # Enable Flask's debugging features. Should be False in production
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
