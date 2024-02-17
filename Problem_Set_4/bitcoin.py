import sys
import requests

# define main fn
def main():
  if len(sys.argv) == 2:
    try:
      num = float(sys.argv[1])
    except ValueError:
      sys.exit("Command-line argument is not a number")
    else:
      get_bitcoin(num)
  elif len(sys.argv) == 1 :
    sys.exit("Missing command-line argument")


# define get_user_input fn
def get_bitcoin(dollar):
  try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
  except requests.RequestException:
    pass
  else:
    data = response.json()
    rate = data["bpi"]["USD"]["rate_float"]
    bitcoin = round(rate * dollar, 4)
  print(f"${'{:,}'.format(bitcoin)}")

# call main fn
if __name__ == "__main__":
  main()
