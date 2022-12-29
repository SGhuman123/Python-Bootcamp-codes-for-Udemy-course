import requests
import smtplib


class CustomerDataManager:
    def __init__(self, price, from_location, from_code, to_location, to_code, from_date, to_date, number_of_stop_over=0,
                 stop_over_city=None):
        self.headers = {"Authorization": "TOKEN"}
        self.post_sheety_endpoint = "YOUR SHEETY PRICES ENDPOINT"
        self.email = "SENDER EMAIL"
        self.password = "SENDER EMAIL PASSWORD"
        self.price = price
        self.from_location = from_location
        self.from_code = from_code
        self.to_location = to_location
        self.to_code = to_code
        self.from_date = from_date
        self.to_date = to_date
        self.number_of_stop_over = number_of_stop_over
        self.stop_over_city = stop_over_city
        self.add_user_to_database()

    def add_user_to_database(self):
        print('''Welcome to Hikari's Flight Club.\nWe find the best flight deals and email you.''')
        first_name = input("What is your first name?")
        last_name = input("What is your last name?")
        email = input("What is you email?")
        email_validation = input("Type your email again.")

        if email == email_validation:
            print("You're in the club!")

        sheety_parameters = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email_validation
            }
        }
        response_sheety = requests.post(url=self.post_sheety_endpoint, json=sheety_parameters,
                                        headers=self.headers)
        print(response_sheety.text)

    def send_email(self):
        obtained_data = requests.get(url=self.post_sheety_endpoint, headers=self.headers).json()
        # print(obtained_data)
        # print(type(obtained_data))
        if self.number_of_stop_over == 0:
            message_to_be_sent = f'Low price alert! Only ${self.price} SGD to fly from {self.from_location}-' \
                                 f'{self.from_code} to {self.to_location}-{self.to_code}, from' \
                                 f'{self.from_date} to {self.to_date}.'
        elif self.number_of_stop_over > 0:
            message_to_be_sent = f'Low price alert! Only ${self.price} SGD to fly from {self.from_location}-' \
                                f'{self.from_code} to {self.to_location}-{self.to_code}, from ' \
                                f'{self.from_date} to {self.to_date}.' \
                                f'Flight has {self.number_of_stop_over} stop over, via {self.stop_over_city}.'
        for email in obtained_data["users"]:
            obtained_email = email["email"]
            print(obtained_email)
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.password)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=obtained_email,
                    msg=message_to_be_sent
                )
        pass


# CustomerDataManager().send_email()
