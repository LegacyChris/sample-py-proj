## This is a simple program that converts days to hours
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days equals {num_of_days * calculation_to_units} {name_of_unit}"
    

def validate_and_execute():
    try:
        user_input_number = int(num_of_days)
        if user_input_number > 0:
            calculated_result = days_to_units(user_input_number)
            print(calculated_result)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid number")
        else:
            print("You entered a negative number as input. Not sure what you are thinking")
            
    except ValueError:
        print("Your input is not a number. Don't ruin my program!")

# get user input
num_of_days = ""

#Execute the function
while num_of_days != "exit" and num_of_days != "quit":
    num_of_days = input("Enter any number of days and I will convert that for you (enter 'exit' or 'quit' to exit): ")
    if num_of_days == "exit" or num_of_days == "quit":
        print("Thank you for stopping by")
        break
    else:
        validate_and_execute()
        
        
