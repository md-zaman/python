from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")

print(datetime.strptime(deadline, "%d.%m.%Y"))
print(type(datetime.strptime(deadline, "%d.%m.%Y")))
print(input_list)

todays_date = datetime.today()

time_remaining = deadline_date - todays_date
num_of_hours = int(time_remaining.total_seconds() / 60 / 60)    
print(f"Hey User, the time remaining until your deadline {goal} is {num_of_hours} hours")
