import re
import sys

def main():
  html = input("HTML: ")
  watch_url = parse(html)
  print(watch_url)

# define parse function which return desired link/None
def parse(s):
  try:
    my_regex = r"^<iframe.*src=[\'\"]https?://(?:www\.)?youtube\.com/embed/(\w+)"
    result = re.search(my_regex, s)
    if result:
      video_id = result.group(1)
      watch_youtube_url = f"https://youtu.be/{video_id}"
      return watch_youtube_url
    else:
      return None
  except ValueError:
    pass


if __name__ == "__main__":
  main()
