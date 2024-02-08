# Declare main Fn
def main():
  file_name = input("File name: ").strip().lower()
  check_file_extension(file_name)

# declare check_file_extension Fn:
def check_file_extension(name):
  if name.endswith(".gif"):
    print("image/gif")
  elif name.endswith(".jpg") or name.endswith(".jpeg") :
    print("image/jpeg")
  elif name.endswith(".png"):
    print("image/png")
  elif name.endswith(".pdf"):
    print("application/pdf")
  elif name.endswith(".txt"):
    print("text/plain")
  elif name.endswith(".zip"):
    print("application/zip")
  else:
    print("application/octet-stream")

main()

