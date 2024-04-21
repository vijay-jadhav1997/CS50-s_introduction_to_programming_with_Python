from numb3rs import validate
import pytest


def main():
    test_validate_for_digits()
    test_validate_for_alphanum()

def test_validate_for_digits():
    assert validate("127.0.0.1") == True
    assert validate("127.100.50.256") == False
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("12.52.51.002") == True
    assert validate("1.1.1.1.1") == False

def test_validate_for_alphanum():
    assert validate("VJ24") == False
    assert validate("21.DK.056") == False
    assert validate("o.100.101.102") == False
    assert validate("efo.10ab0.10jkl1.102") == False

if __name__ == "__main__":
    main()
