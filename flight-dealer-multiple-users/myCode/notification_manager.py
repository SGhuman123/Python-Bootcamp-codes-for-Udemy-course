from twilio.rest import Client


class NotificationManager:
    def __init__(self, price, from_location, from_code, to_location, to_code, from_date, to_date, number_of_stop_over=0,
                 stop_over_city=None):
        self.price = price
        self.from_location = from_location
        self.from_code = from_code
        self.to_location = to_location
        self.to_code = to_code
        self.from_date = from_date
        self.to_date = to_date
        self.number_of_stop_over = number_of_stop_over
        self.stop_over_city = stop_over_city

    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self):
        if self.number_of_stop_over == 0:
            message_to_be_sent = f'Low price alert! Only ${self.price} SGD to fly from {self.from_location}-' \
                                 f'{self.from_code} to {self.to_location}-{self.to_code}, from' \
                                 f'{self.from_date} to {self.to_date}.'
        elif self.number_of_stop_over > 0:
            message_to_be_sent = f'Low price alert! Only ${self.price} SGD to fly from {self.from_location}-' \
                                f'{self.from_code} to {self.to_location}-{self.to_code}, from ' \
                                f'{self.from_date} to {self.to_date}.' \
                                f'Flight has {self.number_of_stop_over} stop over, via {self.stop_over_city}.'

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
