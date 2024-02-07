# define main fn
def main():
  # Promt user input and convert str to int
  mass = int(input("m : "))
  # call energy_calc fn
  energy_calc(mass)

def energy_calc(m):
  # Convert mass to equivalent energy
  speed_sqr = 300000000 ** 2
  energy = m * speed_sqr
  # Display energy
  print(f"E : {energy}")


# call main fn
main()
