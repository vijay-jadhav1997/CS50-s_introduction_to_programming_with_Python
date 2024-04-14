from bank import value

def main():
  test_hello()
  test_starts_with_h()
  test_other()


def test_hello():
  assert value("Hello") == 0
  assert value("Hello, Newman") == 0


def test_starts_with_h():
  assert value("How you doing?") == 20
  assert value( "Hey there!") == 20

def test_other():
  assert value("What's happening?") == 100
  assert value( "Long time no see!") == 100



if __name__ == "__main__":
  main()
