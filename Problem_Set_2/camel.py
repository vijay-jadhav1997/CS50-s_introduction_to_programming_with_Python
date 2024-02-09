def main():
  camel = input("camelCase: ")
  convert_to_snake_case(camel)


# def convert_to_snake_case()
def convert_to_snake_case(name):
  snake = ""
  for letter in name:
    if letter.isupper():
      snake += f"_{letter.lower()}"
    else:
      snake += letter

  print(f"snake_case: {snake.strip()}")




# call main Fn:
if __name__ == "__main__":
  main()
