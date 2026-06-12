from src.utils.helpers import truncate, validate_positive_int
import pytest


def test_truncate_short():
    assert truncate("hello", 10) == "hello"


def test_truncate_long():
    result = truncate("a" * 100, 20)
    assert len(result) == 20
    assert result.endswith("…")


def test_validate_positive_int_ok():
    assert validate_positive_int(5, "hours") == 5


def test_validate_positive_int_fail():
    with pytest.raises(ValueError):
        validate_positive_int(0, "hours")
