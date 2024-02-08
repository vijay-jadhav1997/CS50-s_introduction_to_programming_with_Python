# define main Function
def main():
  greet = input("Greeting: ").strip().capitalize()

  reward = value(greet)
  print(f"${reward}")

# define howGreeting Fn
def value(greeting):
  if greeting.startswith('Hello'):
    return 0
  elif greeting.startswith('H'):
    return 20
  else:
    return 100

# call main Fn at the end
if __name__ == "__main__":
  main()
