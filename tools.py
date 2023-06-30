import time
from functools import wraps
from datetime import datetime

from logger_factory import make_logger


def time_it(function):
    function_name = function.__name__
    module_name = function.__module__
    logger = make_logger(f"{module_name}.{function_name}")

    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            logger.info("begin function execution: %s", function_name)
            start = datetime.utcnow()
            result = function(*args, **kwargs)
            end = datetime.utcnow()
            duration = (end - start).microseconds
            logger.info("execution of function %s ended successfuly after %dms", function_name, duration)
            return result
        except Exception as error:
            logger.exception("function %s has failed: %s", function_name, error)
            raise error

    return wrapper


def apply_to_public_methods(decorator):
    def decorate(cls):
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and not attr_name.startswith('_'):
                setattr(cls, attr_name, decorator(attr))
        return cls
    return decorate
