import pytest

from arithmetic import divide


def test_divide():
    result = divide(9, 3)
    assert 3 == result


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(9, 0)
