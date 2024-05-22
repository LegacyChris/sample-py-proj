months = {'January', 'February', 'March', 'April', 'May', 'June'}

for month in months:
    print(month.upper())
    
    
def print_month(new_month):
    print(f"You were born in {new_month.upper()}!")
    

my_dob = input("What month where you born in? ")
print(print_month(my_dob))

newd = "test".split()
print(newd)