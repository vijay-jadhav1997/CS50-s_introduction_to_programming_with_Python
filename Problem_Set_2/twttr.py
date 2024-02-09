# Define main fn
def main():
  user_inp = input("Input: ")
  result = shorten(user_inp)
  print(f"Output: {result}")

# define remove_vowals fn
def shorten(word):
  output = ""
  for letter in word :
    match letter :
      case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u" :
        output
      case _ :
        output += letter

  return output

# call main Fn
if __name__ == "__main__":
  main()
