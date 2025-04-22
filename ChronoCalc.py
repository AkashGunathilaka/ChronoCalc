import datetime
def selector():
    # This function is used to select the function to be executed before i had the function call on itself and realized this leads to stack overflow so i changed it into a while true loop 
    while True:
        print("""
Select the function you want to execute:
1. Time to current date
2. Time between two dates
3. Time to future date             
3. Exit""")

        choice = input("Enter your choice: ")

        if choice == '1':
            timetocurrent()
        elif choice == '2':
            timebetween()
        elif choice == '3':
            timetofuture()    
        elif choice == '4':
            exit()
        else:
            print("Invalid choice. Please try again.")
            break

def timetocurrent():
    # This function calculates the time difference to the current date 
    date1 = input("Enter the date (YYYY/MM/DD): ")
    
    # Convert input date to a datetime object
    date1 = datetime.datetime.strptime(date1, "%Y/%m/%d")
    
    # Get current date as a datetime object
    currentdate = datetime.datetime.now()
    
    # Calculate the difference in years, months, and days
    years = currentdate.year - date1.year
    months = currentdate.month - date1.month
    days = currentdate.day - date1.day

    # Adjust if current day is earlier in the month than the input day
    if days < 0:
        months -= 1
        prev_year = currentdate.year if currentdate.month != 1 else currentdate.year - 1
        days_in_prev_month = (datetime.datetime(prev_year, prev_month + 1, 1) - datetime.datetime(prev_year, prev_month, 1)).days
        days += days_in_prev_month

    # Adjust if current month is earlier in the year than the input month
    if months < 0:
        years -= 1
        months += 12

    print(f"The difference is: {years} years, {months} months, and {days} days.")

    selector()

def timetofuture():
    # This function calculates the time difference to the future date
    date1 = input("Enter the date (YYYY/MM/DD): ")
    
    date1 = datetime.datetime.strptime(date1, "%Y/%m/%d")

    currentdate = datetime.datetime.now()

    # Calculate the difference in years, months, and days
    years = date1.year - currentdate.year
    months = date1.month - currentdate.month
    days = date1.day - currentdate.day

    # Adjust if current day is later in the month than the input day
    if days < 0:
        months -= 1
        prev_month = (date1.month - 1) or 12
        prev_year = date1.year if date1.month != 1 else date1.year - 1
        days_in_prev_month = (datetime.datetime(prev_year, prev_month + 1, 1) - datetime.datetime(prev_year, prev_month, 1)).days
        days += days_in_prev_month

    # Adjust if current month is later in the year than the input month
    if months < 0:
        years -= 1
        months += 12

    print(f"The difference is: {years} years, {months} months, and {days} days.")
    selector()


def timebetween():
    # This function calculats the time between two dates
    date1 = input("Enter the first date (YYYY/MM/DD H:M): ")
    date2 = input("Enter the second date (YYYY/MM/DD H:M): ")

    # so in this the user enters the date but it is stored as a string and we need to convert it into a date object to do this we need to parse the string and get the relevant information

    try :
        if " " in date1 and " " in date2:
            date1 = datetime.datetime.strptime(date1, "%Y/%m/%d %H:%M")
            date2 = datetime.datetime.strptime(date2, "%Y/%m/%d %H:%M")
        else:
            date1 = datetime.datetime.strptime(date1, "%Y/%m/%d")
            date2 = datetime.datetime.strptime(date2, "%Y/%m/%d")

    except ValueError:
        print("Invalid date format. Please enter the date in the correct format.")
        timebetween()
        return        

    # Now we can calculate the difference between the two dates

    difference = date2 - date1
    days = difference.days
    hours = difference.seconds // 3600  
    minutes = (difference.seconds // 60) % 60
    # Now we can print the difference
    print(f"The difference is: {days} days, {hours} hours, and {minutes} minutes.")
    selector()
    
# when we subtract two date objects we get a timedelta object which is not clear so we need to convert it into a more readable format by breaking down the time delta object and labelling the different parts our self and printing a formatted string 
selector()


# now we need to do some error handling to make sure the user enters in the correct format
# we can also write a function to handle if the month is later in the year than the input month