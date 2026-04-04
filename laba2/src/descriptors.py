from .errors import InvalidTypeError, InvalidValueError


class PositiveInt:
    """Дескриптор проверки на положительное целое число."""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise InvalidTypeError(f"{self.name} должен быть int")
        if value <= 0:
            raise InvalidValueError(f"{self.name} должен быть больше 0")
        obj.__dict__[self.name] = value


class NotEmptyString:
    """Дескриптор проверки на непустую строку."""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise InvalidTypeError(f"{self.name} должен быть str")
        if not value.strip():
            raise InvalidValueError(f"{self.name} не может быть пустым")
        obj.__dict__[self.name] = value
