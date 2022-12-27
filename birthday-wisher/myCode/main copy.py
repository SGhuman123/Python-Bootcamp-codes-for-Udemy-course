##################### Extra Hard Starting Project ######################

import datetime as dt
import pandas
import random
import smtplib

# 1. Update the birthdays.csv -- DONE

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
# print(now)
my_email = "YOUR EMAIL"
password = "YOUR EMAIL PASSWORD"
birthday_list = pandas.read_csv("birthdays.csv")
birthday_list = birthday_list.to_dict(orient="records")
for birthday in birthday_list:
    if birthday['month'] == now.month and birthday['day'] == now.day:
        # print(birthday['name'], birthday['email'])

        # 3. If step 2 is true, pick a random letter from letter templates
        # and replace the [NAME] with the person's actual name from birthdays.csv
        letter_number = random.randint(1, 3)
        letter_format = f"letter_templates/letter_{letter_number}.txt"
        with open(letter_format, "r") as file:
            file_format = file.read()
        letter_to_be_sent = file_format.replace("[NAME]", birthday['name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday['email'],
                msg=f"Subject: Happy Birthday!!!\n\n{letter_to_be_sent}"
            )
