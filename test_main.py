import pytest
from main import is_prime

@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected