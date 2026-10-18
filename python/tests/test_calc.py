import pytest

from playground.calc import add, average, fizzbuzz


def test_add():
    assert add(1, 2) == 3


def test_average():
    assert average([1, 2, 3]) == 2


def test_average_empty():
    with pytest.raises(ValueError):
        average([])


@pytest.mark.parametrize(
    ("n", "expected"),
    [(1, "1"), (3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")],
)
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected
