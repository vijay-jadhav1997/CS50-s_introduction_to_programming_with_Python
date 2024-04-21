import pytest
from working import convert


def main():
  test_convert_for_early_work()
  test_convert_for_late_work()

# define 'test_convert_for_early_work' function to test convert function for day time
def test_convert_for_early_work():
  assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
  assert convert("4 AM to 1 PM") == "04:00 to 13:00"
  assert convert("10:59 AM to 7:20 PM") == "10:59 to 19:20"
  assert convert("12:59 PM to 9:00 PM") == "12:59 to 21:00"

# define 'test_convert_for_late_work' function to test convert function for late in the day or night time
def test_convert_for_late_work():
  assert convert("9 PM to 5 AM") == "21:00 to 05:00"
  assert convert("11:59 PM to 8:00 AM") == "23:59 to 08:00"
  assert convert("12:59 AM to 10:00 AM") == "00:59 to 10:00"
  assert convert("7:00 PM to 4:30 AM") == "19:00 to 04:30"

# define 'test_cotest_convert_for_late_worknvert_for_errors' function to test convert function for Value Errors
def test_cotest_convert_for_late_worknvert_for_errors():
  with pytest.raises(ValueError):
    convert("12:60 AM to 9:00 PM")

  with pytest.raises(ValueError):
    convert("13:00 PM to 5:30 PM")

  with pytest.raises(ValueError):
    convert("5:30 PM to 12:60 PM")

  with pytest.raises(ValueError):
    convert("4 PM to 13 AM")
  with pytest.raises(ValueError):
    convert("9 PM - 5 AM")
  with pytest.raises(ValueError):
    convert("08:30 PM  04:30 AM")



if __name__ == "__main__":
  main()
