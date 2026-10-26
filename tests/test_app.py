import pytest

from app import add, is_even


# ---------- add ----------

def test_add_simple():
    assert add(2, 3) == 5


def test_add_negative_and_zero():
    assert add(-4, 4) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_add_strings():
    assert add("Hello, ", "pytest") == "Hello, pytest"


# ---------- is_even ----------

@pytest.mark.parametrize("value, expected", [
    (2, True),
    (3, False),
    (10, True),
    (0, True),
    (-4, True),
    (-7, False),
])
def test_is_even(value, expected):
    assert is_even(value) == expected


# ---------- fixture ----------

@pytest.fixture
def sample_numbers():
    return [2, 4, 6]


def test_all_even(sample_numbers):
    for n in sample_numbers:
        assert is_even(n)
