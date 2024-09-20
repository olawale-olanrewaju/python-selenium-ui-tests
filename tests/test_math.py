import pytest

def test_addition():
    assert 1 + 1 == 2

@pytest.mark.parametrize("a,b,expected", [(2,3,6),(3,3,9),(4,5,20)])
def test_multiplication(a, b, expected):
    assert a * b == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0