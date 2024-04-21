import re


def main():
    text = input("Text: ")
    count_result = count(text)
    print(count_result)


# define count function to count 'um' case-insensitively and return count
def count(s):
    um_regex = r"\bum\b"
    result = re.findall(um_regex, s, flags=re.IGNORECASE)  # re.findall() => returns list
    return len(result)


if __name__ == "__main__":
    main()
