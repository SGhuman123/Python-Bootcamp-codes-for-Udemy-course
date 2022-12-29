from twilio.rest import Client


class NotificationManager:
    def __init__(self, price, from_location, from_code, to_location, to_code, from_date, to_date):
        self.price = price
        self.from_location = from_location
        self.from_code = from_code
        self.to_location = to_location
        self.to_code = to_code
        self.from_date = from_date
        self.to_date = to_date

    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self):
        message_to_be_sent = f'Low price alert! Only ${self.price} SGD to fly from {self.from_location}-' \
                             f'{self.from_code} to {self.to_location}-{self.to_code}, from' \
                             f'{self.from_date} to {self.to_date}.'
        account_sid = "YOUR TWILIO ACCOUNT SID"
        auth_token = "YOUR TWILIO AUTH TOKEN"
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=message_to_be_sent,
            from_='YOUR TWILIO VIRTUAL NUMBER',
            to='YOUR TWILIO VERIFIED NUMBER'
        )
        # print(message.status)

    pass
