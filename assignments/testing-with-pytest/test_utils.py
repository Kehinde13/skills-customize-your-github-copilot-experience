import pytest

from src.utils import is_palindrome, calculate_discount, format_full_name


def test_is_palindrome_true():
    assert is_palindrome("Racecar") is True


def test_is_palindrome_false():
    assert is_palindrome("Python") is False


def test_is_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_calculate_discount_normal():
    assert calculate_discount(100, 25) == 75.0


def test_calculate_discount_zero_discount():
    assert calculate_discount(50, 0) == 50.0


def test_calculate_discount_full_discount():
    assert calculate_discount(80, 100) == 0.0


def test_calculate_discount_invalid_price():
    with pytest.raises(ValueError):
        calculate_discount(-10, 20)


def test_calculate_discount_invalid_percent():
    with pytest.raises(ValueError):
        calculate_discount(100, 110)


def test_format_full_name():
    assert format_full_name("jane", "doe") == "Jane Doe"


def test_format_full_name_with_whitespace():
    assert format_full_name("  john", "doe  ") == "John Doe"


@pytest.fixture
def sample_names():
    return [
        ("alice", "smith", "Alice Smith"),
        ("BOB", "jones", "Bob Jones"),
        (" maria", "lopez ", "Maria Lopez"),
    ]


@pytest.mark.parametrize("first,last,expected", [
    ("amelia", "earhart", "Amelia Earhart"),
    ("MARK", "TWAIN", "Mark Twain"),
])
def test_format_full_name_parametrized(first, last, expected):
    assert format_full_name(first, last) == expected


def test_sample_names_fixture(sample_names):
    for first, last, expected in sample_names:
        assert format_full_name(first, last) == expected
