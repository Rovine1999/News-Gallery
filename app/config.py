class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey=5d2b0a6a455c4d4db1029ce0d678f050'
    NEWS_API_ARTICLES_URL='https://newsapi.org/v2/everything?q=bitcoin&apiKey=5d2b0a6a455c4d4db1029ce0d678f050'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

