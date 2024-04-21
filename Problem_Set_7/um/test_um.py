import pytest
from um import count


def main():
    test_count()

# define test_count function that test count function for return of count of 'um'
def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Jay Hari um! .. um, ohh um") == 3


# define test_count function that test count function for return of count of 'um' case-insensitively.
def test_count_for_case_insensitivity():
    assert count("Um? ... um By the way uM Thanks UM ...") == 4
    assert count("UM") == 1
    assert count("uM?") == 1


# define test_count function that test count function for return of count of 'um' for not subs.
def test_count_for_not_substring():
    assert count("ummm") == 0
    assert count("um_um, give me umbrela!") == 0
    assert count("Umma, thanks for the album.") == 0


if __name__ == "__main__":
    main()
