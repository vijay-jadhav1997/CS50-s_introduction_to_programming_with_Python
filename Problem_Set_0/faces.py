# Get user input
user_inp = input("Enter how you're feeling today with emoticons => ").strip()

# Replace emoticons with emoji
result = user_inp.replace(":)", "🙂").replace(":(", "🙁")

# print result:
print(result)

