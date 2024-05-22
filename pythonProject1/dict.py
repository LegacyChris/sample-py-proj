# get user input
from helper import validate_and_execute, user_input_message
import os
import logging
from datetime import datetime, date

print(datetime.now())
print(os.name)
# num_of_days = ""

# #Execute the function
# while num_of_days != "exit" and num_of_days != "quit":
#     try:
#         num_of_days = input(user_input_message)
#         days_and_unit = num_of_days.split(":")
#         print(days_and_unit)
#         days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
#         print(days_and_unit_dict)
#         validate_and_execute(days_and_unit_dict)    
#     except IndexError:
#         print("Try again next time")