import pytest

# function to test square
def square(n):
    return n**2
def cube(n):
    return n**3
def fifth_power(n):
    return n**5


# testing the square function
def test_square():
    assert square(2) == 4, "test failed square of 2 should be 4"
    assert square(3) == 4, "test failed square of 3 should be 9"

def test_cube():
    assert cube(2) == 8, "test failed cube of 2 should be 8"
    assert cube(3) == 27, "test failed cube of 3 should be 27"

def fifth_square():
    assert fifth_power(2) == 32, "test failed fifth_power of 2 should be 32"
    assert fifth_power(3) == 243, "test failed fifth_power of 3 should be 243"

# test for invalid input

def test_invalid_input():
    with pytest.raises(TypeError):
        square('string')