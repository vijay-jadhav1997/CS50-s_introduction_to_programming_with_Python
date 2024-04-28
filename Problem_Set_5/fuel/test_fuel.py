import pytest
from Problem_Set_5.fuel.fuel import convert
from Problem_Set_5.fuel.fuel import gauge

def main():
  test_convert()
  test_gauge()


def test_convert():
  assert convert("3/4") == 75 , "3/4 should be return as 75"
  assert convert("1/4") == 25 , "1/4 should be return as 25"
  assert convert("4/4") == 100 , "4/4 should be return as 100"
  assert convert("0/4") == 0 , "4/4 should be return as 0"

  # test ZeroDivisionError
  with pytest.raises(ZeroDivisionError):
    convert("4/0")

  # test ValueError
  with pytest.raises(ValueError):
    convert("1.5/3")

  # test ValueError
  with pytest.raises(ValueError):
    convert("Jay/Shree")

def test_gauge():
  assert gauge(75) == "75%"
  assert gauge(1) == "E"
  assert gauge(99) == "F"
  assert gauge(67) == "67%"

if __name__ == "__main__":
  main()
