from plates import is_valid

def main():
  test_start_with_2letter()
  test_max6_and_min2_char()
  test_numb_not_in_middle()
  test_first_digit_not_zero()
  test_no_period_spaces_punctuation()


def test_start_with_2letter():
  assert is_valid("CS50") == True
  assert is_valid("50CS") == False
  assert is_valid("JAY321") == True
  assert is_valid("908172") == False

def test_max6_and_min2_char():
  assert is_valid("GREAT50") == False
  assert is_valid("SMRT10") == True
  assert is_valid("S") == False
  assert is_valid("OUTOFDATE") == False

def test_numb_not_in_middle():
  assert is_valid("CS50P2") == False
  assert is_valid("PY10ND") == False
  assert is_valid("LOVE21") == True

def test_first_digit_not_zero():
  assert is_valid("CS05") == False
  assert is_valid("DEV001") == False
  assert is_valid("TEN10") == True

def test_no_period_spaces_punctuation():
  assert is_valid("PI3.14") == False
  assert is_valid("PI314") == True
  assert is_valid("HEY,10") == False
  assert is_valid("LOVE 1") == False


if __name__ == "__main__":
  main()
