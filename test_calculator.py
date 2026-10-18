import pytest
from calculator import add,subtract,multiply

def test_add():
    assert add(4,3)==7

def test_subtract():
    assert subtract(4,3)==1

def test_multiply():
    assert multiply(4,3)==12

@pytest.mark.parametrize("a,b",[(0,2),(-1,2),(2,0),(2,-1),(1.5,2),(True,2)])
def test_invalid_inputs(a,b):
    with pytest.raises(ValueError):
        add(a,b)
