# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas as pd
import datetime as dt
from random import randint
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today = dt.date.today()

data = pd.read_csv("birthdays.csv")
birthdays_today = data.loc[
    (data["month"] == today.month) &
    (data["day"] == today.day)]
bd_name = birthdays_today["name"].to_string(index=False)
bd_email = birthdays_today["email"].to_string(index=False)


rnd_num = randint(1, 3)

if not birthdays_today.empty:
    with open(f"letter_templates/letter_{rnd_num}.txt", "r") as file:
        message = file.read()
        message = message.replace("[NAME]", bd_name)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=bd_email,
            msg=f"Subject:Happy Birthday!\n\n{message}"
        )
