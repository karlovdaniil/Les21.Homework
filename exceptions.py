class BaseError(Exception):
    message = NotImplemented


class RequestError(BaseError):
    message = NotImplemented


class LogisticError(BaseError):
    message = NotImplemented


class NotEnoughSpace(LogisticError):
    message = 'Недостаточно места на складе'


class NotEnoughProduct(LogisticError):
    message = 'Недостаточно товара на складе'


class UnknownProduct(LogisticError):
    message = 'Неизвестный товар'


class TooManyDifferentProduct(LogisticError):
    message = 'Слишком много разных товаров'


class InvalidRequest(RequestError):
    message = 'Неправильный запрос. Попробуйте снова'


class InvalidStorageName(RequestError):
    message = 'Выбран не существующий склад'
