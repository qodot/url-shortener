class Error(Exception):
    pass


class NotExistShortUrlError(Error):
    message = 'this short url is not exists'


class AlreadyExistOriginUrl(Error):
    message = 'this origin url is already exists'
