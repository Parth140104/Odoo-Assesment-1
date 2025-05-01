from datetime import datetime

def calculate_date_difference():
    # Take input from the user
    date_format = "%d-%m-%Y"
    date1_str = input("Enter the first date (dd-mm-yyyy): ")
    date2_str = input("Enter the second date (dd-mm-yyyy): ")

    try:
        # Convert strings to datetime objects
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)

        # Calculating difference
        difference = abs((date2 - date1).days)
        print(f"\nThe difference between {date1_str} and {date2_str} is {difference} day(s).")

    except ValueError:
        print(" Invalid date format. Please enter dates in dd-mm-yyyy format.")

calculate_date_difference()
