import random

lower = "abcdefghijklmnopqrstuvwyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
numbers = "0123456789"
symbols = "~`! @#$%^&*()_-+={[}]|\:;'<,>.?/"

all_chars = lower + upper + numbers + symbols
length = 16
# password = "".join(random.sample(all,length))


for _ in range(10):
    password = "".join(random.sample(all_chars, length))
    print(password)

print("\nYou can choose either of these 10 randomly generated passwords.")