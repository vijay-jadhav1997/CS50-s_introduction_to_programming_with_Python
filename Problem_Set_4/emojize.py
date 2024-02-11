import emoji

def main():
  user_inp = input("Input: ")
  output = emoji.emojize(user_inp, language='alias')
  print(f"Output: {output}")

# call main fn
if __name__ == "__main__":
  main()
