import sys

# define main Fn
def main():
  if check_arg(sys.argv):
    line_of_code = get_lines_of_code(sys.argv[1])
    print(line_of_code)


# define check_arg Fn to validate comman-line arguments
def check_arg(arg):
  if len(arg) == 2:
    if arg[1].endswith(".py"):
      return True  # valid python file extension
    else:
      sys.exit("Not a Python file")
  elif len(arg) < 2:
    sys.exit("Too few command-line arguments")
  elif len(arg) > 2:
    sys.exit("Too many command-line arguments")

# define get_lines_of_code Fn to calculate the non-comment and non-empty lines of code
def get_lines_of_code(py_file):
  try:
    with open(py_file, "r") as file:
      lines = 0
      for line in file:
        if not(line.strip().startswith("#")) and not(line.strip() == ""):
          # count lines that are not comment and non-empty
          lines += 1
      return lines
  except FileNotFoundError:
    sys.exit("File does not exist")

if __name__ == "__main__":
  main()
