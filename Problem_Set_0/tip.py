# Define main fn
def main():
  dollars = dollars_to_float(input("How much was the meal? "))
  percent = percent_to_float(input("What percent would you like to tip? "))
  tip = dollars * percent
  print(f"Leave ${tip:.2f}")

# define dollars_to_float fn
def dollars_to_float(d):
  d = d.replace("$", "")
  return float(d)

# define percent_to_float fn
def percent_to_float(p):
  p = p.replace("%", "")
  return float(p)/100

# call main fn
main()
