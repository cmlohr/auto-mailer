import smtplib
import datetime as dt
import random
import pandas

# parameters set for gmail
# personal email and pass removed before push to git
SEND_EMAIL = "xxxxxx0@gmail.com"  # gmail email login
PASSWORD = "xxxxxxxxxx"  # gmail login password
GMAIL = "smtp.gmail.com"  # google smtp
NAME = "[NAME]"
LETTER_PATH = f"./letter_templates/letter_{random.randint(1,3)}.txt"

todays_date = dt.datetime.now()
today = (todays_date.month, todays_date.day)

data = pandas.read_csv("names_and_dates.csv")
email_dates = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
person = email_dates[today]
name = person["name"]
email = person["email"]

if today in email_dates:
    with open(LETTER_PATH) as letter:
        contents = letter.read()
        new_contents = contents.replace(NAME, name)
    with smtplib.SMTP(GMAIL, port=587) as connect:
        connect.starttls()
        connect.login(user=SEND_EMAIL, password=PASSWORD)
        connect.sendmail(
            from_addr=SEND_EMAIL,
            to_addrs=email,
            msg=f"Subject:You are invited {name}!\n\n{new_contents}"
        )

