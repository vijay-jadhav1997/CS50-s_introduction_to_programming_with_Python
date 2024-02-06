# prompt user input
user_inp = input('Enter here, what\'s in your mind. => ')

# trim user_inp leading and trailing whitespace, and then replace whitespace between words to "..."
user_inp = user_inp.strip().replace(" ", "...")

# display playback user_inp

print(user_inp)

