from arithmetic.arithmetic import add


def test_add_int():
    result = add(2, 4)
    assert 6 == result


def test_add_str():
    result = add("Hello ", "world")
    assert "Hello world" == result
