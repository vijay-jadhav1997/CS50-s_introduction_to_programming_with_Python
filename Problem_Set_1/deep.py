# Define main fn
def main():
  answer = input("What is the Answer to the Question of Life, the Universe, the Everthing? ").strip().lower()
  isCorrect(answer)

# define isCorrect Fn
def isCorrect(ans):
  match ans:
    case '42' | 'forty-two' | 'forty two' :
      print("Yes")
    case _:
      print("No")

main()
