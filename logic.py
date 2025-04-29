import datetime
from dateutil.relativedelta import relativedelta
import calendar



def selector():
    # This function is used to select the function to be executed before i had the function call on itself and realized this leads to stack overflow so i changed it into a while true loop 
    while True:
        print("""
Select the function you want to execute:
1. Time to current date
2. Time between two dates
3. Time to future date
4. Day of the week                          
5. Exit""")

        choice = input("Enter your choice: ")

        if choice == '1':
            timetocurrent()
        elif choice == '2':
            timebetween()
        elif choice == '3':
            timetofuture()   
        elif choice == '4':
            day_of_week()     
        elif choice == '5':
            print("Thanks for using ChronoCalc. Goodbye!")
            break # use break instead of exit for graceful termination ie graceful termination means that the program will close all resources when exiting the app and close connections without immediately ending the program
        else:
            print("Invalid choice. Please try again.")


def timetocurrent():
    # This function calculates the time difference to the current date 
    date1 = get_valid_date("Enter the date (YYYY/MM/DD): ")
    
    # Get current date as a datetime object
    currentdate = datetime.datetime.now()
    
    # Calculate the difference in years, months, and days
    years = currentdate.year - date1.year
    months = currentdate.month - date1.month
    days = currentdate.day - date1.day

    # Adjust if current day is earlier in the month than the input day
    if days < 0:
        months -= 1
        prev_month = (currentdate.month - 1) or 12
        prev_year = currentdate.year if currentdate.month != 1 else currentdate.year - 1
        days_in_prev_month = (datetime.datetime(prev_year, prev_month + 1, 1) - datetime.datetime(prev_year, prev_month, 1)).days
        days += days_in_prev_month

    # Adjust if current month is earlier in the year than the input month
    if months < 0:
        years -= 1
        months += 12

    print(f"The difference is: {years} years, {months} months, and {days} days.")

    

def timetofuture():
    # This function calculates the time difference to the future date
    date1 = get_valid_date("Enter the date (YYYY/MM/DD): ")

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
    


def timebetween():
    # This function calculats the time between two dates
    date1 = get_valid_date("Enter the first date (YYYY/MM/DD H:M): ", with_time=True)
    date2 = get_valid_date("Enter the second date (YYYY/MM/DD H:M): ", with_time=True)

    # so in this the user enters the date but it is stored as a string and we need to convert it into a date object to do this we need to parse the string and get the relevant information

    # Now we can calculate the difference between the two dates

    if date1 > date2:
        date1, date2 = date2, date1
    
    difference = relativedelta(date2, date1)
    # Now we can print the difference
    print(f"The difference is: {difference.years} years, {difference.days} days, {difference.hours} hours, and {difference.minutes} minutes.")

def day_of_week():
    # This function calculates the day of the week for a given date
    date = get_valid_date("Enter the date (YYYY/MM/DD): ")

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = days[date.weekday()]

    print(f"The day of the week is: {day_of_week}")


def get_valid_date(prompt , with_time = False):
    # This function is used to get a valid date from the user
    while True:
        user_input = input(prompt).strip()  # Remove leading and trailing whitespace

        if with_time:

            if " " not in user_input:
                user_input += " 00:00"

        date_format = "%Y/%m/%d %H:%M" if with_time else "%Y/%m/%d"
        
        try:
            return datetime.datetime.strptime(user_input, date_format)
        except ValueError:
            readable_date_format = "YYYY/MM/DD" if not with_time else "YYYY/MM/DD HH:M<"
            print(f"Invalid date format. Please enter the date in the format {readable_date_format}.")


    
# when we subtract two date objects we get a timedelta object which is not clear so we need to convert it into a more readable format by breaking down the time delta object and labelling the different parts our self and printing a formatted string 
selector()

