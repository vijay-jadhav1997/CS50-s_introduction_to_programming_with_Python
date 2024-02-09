def main():
  time = input("What time is it? ")

  if convert(time) >= 7.0 and convert(time) <= 8.0:
    print("breakfast time")
  elif convert(time) >= 12.0 and convert(time) <= 13.0:
    print("lunch time")
  elif convert(time) >= 18.0 and convert(time) <= 19.0:
    print("dinner time")

def convert(t):
  hrs, mins = t.split(":")
  hrs = int(hrs)
  mins = round(int(mins) * (1/60), 2)

  return hrs + mins




if __name__ == "__main__":
  main()

