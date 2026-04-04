class TaskError(Exception):
    """Общее исключение."""
    pass


class TaskValidationError(TaskError):
    """Базовое исключение валидации."""
    pass


class InvalidIdError(TaskValidationError):
    """Недопустимый id."""
    pass


class InvalidPriorityError(TaskValidationError):
    """Недопустимый приоритет."""
    pass


class InvalidDescriptionError(TaskValidationError):
    """Недопустимое описание."""
    pass


class InvalidStatusError(TaskValidationError):
    """Недопустимый статус."""
    pass


class InvalidTypeError(TaskValidationError):
    """Недопустимый тип значения."""
    pass


class InvalidValueError(TaskValidationError):
    """Недопустимое значение."""
    pass
