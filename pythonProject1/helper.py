## This is a simple program that converts days to hours

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days equals {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days equals {num_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days equal {num_of_days * 24 * 60 * 60} seconds"
    else:
        return "unsupported unit"
    
def validate_and_execute(days_and_unit_dict):
    try:
        user_input_number = int(days_and_unit_dict["days"])
        if user_input_number > 0:
            calculated_result = days_to_units(user_input_number, days_and_unit_dict["unit"])
            print(calculated_result)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid number")
        else:
            print("You entered a negative number as input. Not sure what you are thinking")
            
    except ValueError:
        print("Your input is not a number. Don't ruin my program!")
        

user_input_message = "Hey, enter any number of days and conversion unit (enter 'exit' or 'quit' to exit):\n "