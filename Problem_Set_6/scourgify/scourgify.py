import csv
import sys


def main():
  if validate_arg(sys.argv):
    data = get_csvfile_data(sys.argv[1])
    write_csvfile(sys.argv[2], data)


# define validate_arg Fn to validate command-line arguments
def validate_arg(arg):
  if len(arg) == 3:
    if arg[1].endswith(".csv") and arg[2].endswith(".csv"):
      return True  # valid csv files if both are csv files
    else:
      sys.exit("Not a CSV file")
  elif len(arg) < 3:
    sys.exit("Too few command-line arguments")
  elif len(arg) > 3:
    sys.exit("Too many command-line arguments")


# define get_csvfile_data fn to get list of row list of csv_file
def get_csvfile_data(csv_file):
  try:
    listed_data = []
    with open(csv_file, "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
        last, first = row["name"].strip().split(",")  # unpacking "first" & "last" name from "name".
        # creat dict with "first", "last" & "house" keys.
        row_dict = {"first": first.strip(), "last": last.strip(), "house": row["house"]}
        listed_data.append(row_dict)
    return listed_data  # returns the list of row_dict of csv_file
  except FileNotFoundError:
      sys.exit(f"Could not read {csv_file}")


# define write_csvfile to create csv file of expected format
def write_csvfile(after_csvfile, obj_list):
  try:
    with open(after_csvfile, "w") as file:
      writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
      writer.writeheader()
      for obj in obj_list:
        writer.writerow({"first": obj["first"], "last": obj["last"], "house": obj["house"]})
  except ValueError:
    print(ValueError)


if __name__ == "__main__":
  main()
