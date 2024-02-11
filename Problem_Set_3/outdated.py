def main():
  user_date = get_user_date("Date: ")
  result_date = format_date(user_date)
  print(result_date)

# list of months:
months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]

# define get_user_date fn
def get_user_date(promt):
  while True:
    try:
      date_inp = input(promt).strip()
      if date_inp[0].isalpha():
        month_day, year = date_inp.split(",")
        month, day = month_day.split(" ")
        year = year.strip()
        month = month.title()
        day = int(day)
        # print(year, month, day)
        if month in months and day <= 31 and len(year) == 4:
          month = months.index(month) + 1
          return [year, month, day]
      elif date_inp[0].isdigit():
        month, day, year = date_inp.split("/")
        month = int(month)
        day = int(day)
        if month <= 12 and day <= 31 and len(year) == 4 and not(" " in year):
          return [year, month, day]
    except ValueError or KeyError:
      pass




# define format_date Fn
def format_date(date_list):
  yy = date_list[0]
  mm = date_list[1]
  dd = date_list[2]

  if mm < 10 and dd < 10:
    return f"{yy}-0{mm}-0{dd}"
  elif mm < 10:
    return f"{yy}-0{mm}-{dd}"
  elif dd < 10:
    return f"{yy}-{mm}-0{dd}"
  else:
    return f"{yy}-{mm}-{dd}"


# call main Fn
if __name__ == "__main__":
  main()
