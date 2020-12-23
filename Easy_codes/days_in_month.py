def is_leap(year):
    """It takes a year as input and return the boolean value if year is leap or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print("Leap year.")
                return True
            else:
                # print("Not leap year.")
                return False
        else:
            # print("Leap year.")
            return True
    else:
        # print("Not leap year.")
        return False


def days_in_month(year_value, month_value):
    """Function to return the number of days in a months"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_value > 12 or month_value < 1:
        return "Not a valid month!"
    if month_value == 2:
        if is_leap(year_value):
            return 29
    return month_days[month_value - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)













