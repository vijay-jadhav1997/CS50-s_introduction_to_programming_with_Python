from inflect import engine


def main():
  sentence = engine()
  names = get_inp()
  print(f"Adieu, adieu, to {sentence.join(names)}")

# define get_inp fn
def get_inp():
  names = []

  while True:
    try:
      name = input("Name: ").strip()
    except EOFError:
      return names
    except KeyError:
      pass
    else:
      names.append(name)


if __name__ == "__main__":
  main()
