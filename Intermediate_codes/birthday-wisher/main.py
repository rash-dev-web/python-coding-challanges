# import smtplib
#
# my_email = "pyuserone@gmail.com"
# my_pwd = ""
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_pwd)
#     connection.sendmail(from_addr=my_pwd,
#                         to_addrs="pyusertwo@yahoo.com",
#                         msg="Subject:Third message\n\nThis is the body of the email")


# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# print(now.year)
# print(now.weekday())
#
# date_of_birth = dt.datetime(year=2000, month=11, day=12)
# print(date_of_birth)


# project send motivational quotes on Mondays vai Email
import datetime as dt
import random
import smtplib

# obtain the current day of the week
current_day_of_week = dt.datetime.now().weekday()
print(current_day_of_week)

# open quotes.txt and obtain the list of quotes
with open("quotes.txt", "r") as quotes_file:
    all_quotes = quotes_file.readlines()
    # print(all_quotes)

# use random module to pick a random quotes from your list of quotes
quote = random.choice(all_quotes)
# print(quote)

# use smtplib to send an email with the selected quote
my_email = "pyuserone@gmail.com"
my_pwd = "PwbD7HV+l8Q%p"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pwd)
    if current_day_of_week == 6:
        connection.sendmail(from_addr=my_email,
                            to_addrs="pyusertwo@yahoo.com",
                            msg=f"Subject:Happy Birthday\n\n{quote.encode('utf-8')}")
