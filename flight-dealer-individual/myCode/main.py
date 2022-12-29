#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet
# with International Air Transport Association (IATA) codes for each city.
# Most of the cities in the sheet include multiple airports,
# you want the city code (not the airport code see here).
#
# Use the Flight Search API to check for the cheapest flights
# from tomorrow to 6 months later for all the cities in the Google Sheet.
#
# If the price is lower than the lowest price listed
# in the Google Sheet then send an SMS
# to your own number with the Twilio API.
#
# The SMS should include the departure airport IATA code,
# destination airport IATA code, departure city, destination city,
# flight price and flight dates. e.g.

import requests
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()

# This is to update the list with IATA codes for the respective cities
data_manager.update_list()

collated_data = data_manager.data_storer
# print(collated_data)
# print(data_manager.compare_price)
data_manager.compare_price()

index_number = 0
decider = data_manager.send_message
for data in data_manager.data_storer:
    if decider[index_number]["lowerPrice"]:
        # def __init__(self, price, from_location, from_code, to_location, to_code, from_date, to_date):
        # self.price = price
        # self.departure_airport_code = departureAirportCode
        # self.departure_city = departureCity
        # self.arrival_airport_code = arrivalAirportCode
        # self.arrival_city = arrivalCity
        # self.departure_time = departureTime
        # self.arrival_time = arrivalTime
        notification_manager = NotificationManager(data.price, data.departure_city, data.departure_airport_code, data.arrival_city, data.arrival_airport_code, data.departure_time, data.arrival_time)
        notification_manager.send_message()
    index_number += 1













