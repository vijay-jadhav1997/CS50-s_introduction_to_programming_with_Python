import sys
from pyfiglet import Figlet
import random

# define main fn
def main():
  if get_inpt():
    word = input("")
    print(figlet.renderText(word))

figlet = Figlet()
# Get font list
fonts = figlet.getFonts()


# define get_inpt fn
def get_inpt():
  if len(sys.argv) == 1:
    f = random.choice(fonts)
    figlet.setFont(font= f)
    return True
  elif len(sys.argv) != 3:
    sys.exit("Invalid usage")
  elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    if sys.argv[2] in fonts:
      f = sys.argv[2]
      figlet.setFont(font= f)
      return True
    else:
      sys.exit("Invalid usage")
  else:
    sys.exit("Invalid usage")


if __name__ == "__main__":
  main()
