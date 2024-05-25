import datetime

# Get the goal from the user
user_input = input("Enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_left_in_total= deadline_date - today_date

#Calculate how many more days you have till the deadline
print(f"Dear user, You only have {time_left_in_total.days} left to complete {goal}")
