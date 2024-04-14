def main():
  greet = input("Greeting: ").strip().lower()

  reward = value(greet)
  print(f"${reward}")

def value(greeting):
  if greeting.startswith('Hello'):
    return 0
  elif greeting.startswith('H'):
    return 20
  else:
    return 100

if __name__ == "__main__":
  main()
