import pytest
import datetime

from seasons import is_valid_format, get_age_in_minutes


def main():
    test_is_valid_format()
    test_get_age_in_minutes()


# define test_is_valid_format function to test
def test_is_valid_format():
    assert is_valid_format("2024-02-24") == True
    assert is_valid_format("1997-12-31") == True

    with pytest.raises(SystemExit):
        is_valid_format("January 1st, 2024")

    with pytest.raises(SystemExit):
        is_valid_format("31-12-2001")


# define test_get_age_in_minutes function to test
def test_get_age_in_minutes():
    assert get_age_in_minutes("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_age_in_minutes("1998-01-01") == "One million, fifty-one thousand, two hundred minutes"


if __name__ == "__main__":
    main()
