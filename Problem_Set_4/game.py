import random

# define main fn
def main():
  level = get_level()
  play_game(level)


# define get_level fn
def get_level():
  while True:
    try:
      level_input = int(input("Level: "))
    except ValueError:
      pass
    else:
      if level_input < 1:
        pass
      else:
        return level_input

# define play_game fn
def play_game(max):
  random_num = random.randint(1, max)
  while True:
    try:
      guess = int(input("Guess: "))
    except ValueError or KeyError:
      pass
    else:
      if random_num == guess:
        print("Just right!")
        break
      elif random_num > guess:
        print("Too small!")
      else:
        print("Too large!")


# call main fn
if __name__ == "__main__":
  main()
