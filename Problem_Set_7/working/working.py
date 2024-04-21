import re


def main():
    user_inp = input("Hours: ")
    result = convert(user_inp)
    print(result)

# define convert function to convert 12hrs clock time format to 24hrs clock time format
def convert(hours):
    try:
        my_regex = r"^(\d{1,2}):?(\d{2})?\s(AM|PM)\sto\s(\d{1,2}):?(\d{2})?\s(AM|PM)$"
        search_result = re.search(my_regex, hours)
        if search_result:
            start_hrs = int(search_result.group(1))
            start_mins = search_result.group(2)
            start_period = search_result.group(3)
            end_hrs = int(search_result.group(4))
            end_mins = search_result.group(5)
            end_period = search_result.group(6)

            if (start_hrs > 12) or (end_hrs > 12):
                raise ValueError("Invalid input") # if either hrs is more than 12, raises error. Since, in 12hrs format hrs can't be more than 12.
            # when hrs is less than 12 and it is "post meridiem", add 12 to hrs (example, 1PM => 13, 10:30 PM => 22:30)
            if (start_period == "PM") and (start_hrs < 12):
                start_hrs += 12
            if (end_period == "PM") and (end_hrs < 12):
                end_hrs += 12
            # when hrs is equal to 12 and it is "ante meridiem", set hrs to zero (example- 12:30 AM => 00:30)
            if (start_period == "AM") and (start_hrs == 12):
                start_hrs = 0
            if (end_period == "AM") and (end_hrs == 12):
                end_hrs = 0
        else:
            raise ValueError("Invalid input")
    except ValueError:
        raise ValueError("Invalid input")
    else:
        if start_mins and end_mins: # check either mins value whether None Type or not ('None' is Falsy value)
          # if either mins values are not 'None Type', Do following task
            start_mins = int(start_mins)
            end_mins = int(end_mins)

            if (start_mins > 59) or (end_mins > 59):
                raise ValueError("Invalid input") # if either hrs is more than 12, raises error. Since, in mins  can't be more than 59.
            else:
                return f"{start_hrs:02}:{start_mins:02} to {end_hrs:02}:{end_mins:02}" # format int with leading zeroes.
        else:
            return f"{start_hrs:02}:00 to {end_hrs:02}:00" # for plain hrs, mins are zero.


if __name__ == "__main__":
    main()
