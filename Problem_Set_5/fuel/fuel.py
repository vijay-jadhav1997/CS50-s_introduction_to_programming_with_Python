import sys
def main():
  frac = input("Fraction: ")
  percent = convert(frac)
  if f"{percent}".isdigit():
    fuel = gauge(percent)
    print(fuel)

def convert(fraction):
  try:
    numer, denom = fraction.split("/")

    numer = int(numer)
    denom = int(denom)
    result = round((numer / denom) * 100)

  except ZeroDivisionError:
    raise ZeroDivisionError
  except ValueError:
    raise ValueError
  else:
    return result


def gauge(percentage):
  if percentage <= 1:
    return "E"
  elif percentage >= 99:
    return "F"
  else:
    return f"{percentage}%"

if __name__ == "__main__":
  main()
