import datetime as dt
import random
import smtplib


def sendmail(quote):
    my_email = "youremail@youremail.com"
    password = 'yourpassword'

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="emailto@emailto.com",
            msg=f"Subject:Good Morning\n\n{quote}")


date = dt.datetime.now()
day_of_week = date.weekday()

if day_of_week == 0:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        sendmail(quote)
