# import re
# import sys


# def main():
#     ipv4_address = input("IPv4 Address: ")
#     print(validate(ipv4_address))


# def validate(address):
#     if re.search(".", address):
#         return True
#     else:
#         return False

# if __name__ == "__main__":
#     main()

def main():
  user_inp = input("Enter IPv4 Address ").strip()
  print(True if validate(user_inp) else False)


def validate(address):
  try:
    valid = []
    for i in address.split("."):
      i = int(i)
      if 0 <= i <= 255:
        valid.append(i)
  except (ValueError, IndexError, SyntaxError, TypeError, NameError):
    return False
  else:
    if len(valid) == 4:
      return True
    else:
      return False

if __name__ == "__main__":
  main()
