class Error(Exception):
    pass


class NotExistShortUrlError(Error):
    message = 'this short url is not exists'
