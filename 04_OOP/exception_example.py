import pytest

class MyException(Exception):
    pass

def func_with_exception(arg):
    if arg == 1:
        raise MyException()
    else:
        raise ValueError()

def test_is_exception_raised():
    with pytest.raises(MyException):
        func_with_exception(1)