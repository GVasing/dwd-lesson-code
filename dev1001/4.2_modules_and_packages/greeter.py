import datetime
import random

current_date = datetime.date.today()
print(current_date)

greetings = ["Hello, welcome!", "Hope you're having a nice day", "Good luck today!", "Hey there!", "'Sup"]

random_greeting = random.choice(greetings)

print(random_greeting)