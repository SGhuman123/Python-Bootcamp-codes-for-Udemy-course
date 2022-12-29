import requests
from data_manager import DataManager
from notification_manager import NotificationManager
from customer_data_system_manager import CustomerDataManager

data_manager = DataManager()

# DONE: Create a way to add city/location and price to google sheets
do_you_want_to_add_more_locations = True
while do_you_want_to_add_more_locations:
    location = input("Where do you want to go to?")
    price = input("What is your budget?")
    data_manager.add_location_and_price(location, price)
    any_where_else = input("Anywhere else you wish to go? (Y/N) answers only").upper()
    if any_where_else == "Y":
        do_you_want_to_add_more_locations = True
    else:
        do_you_want_to_add_more_locations = False

# DONE: z also if the place is not a city figure a way to add in the IATA code

# This is to update the list with IATA codes for the respective cities
data_manager.update_list()

collated_data = data_manager.data_storer
# print(collated_data)
# print(data_manager.compare_price)
data_manager.compare_price()


index_number = 0
decider = data_manager.send_message
for data in data_manager.data_storer:
    # print(data.stop_overs)
    if decider[index_number]["lowerPrice"]:
        if data.stop_overs == 0:
            # print("First if is working")
            notification_manager = NotificationManager(data.price, data.departure_city, data.departure_airport_code,
                                                       data.arrival_city, data.arrival_airport_code,
                                                       data.departure_time,
                                                       data.arrival_time)
            customer_data_manager = CustomerDataManager(data.price, data.departure_city, data.departure_airport_code,
                                                        data.arrival_city, data.arrival_airport_code,
                                                        data.departure_time,
                                                        data.arrival_time)
        elif data.stop_overs > 0:
            # print("Second if is working")
            notification_manager = NotificationManager(data.price, data.departure_city, data.departure_airport_code,
                                                       data.arrival_city, data.arrival_airport_code,
                                                       data.departure_time,
                                                       data.arrival_time, number_of_stop_over=data.stop_overs,
                                                       stop_over_city=data.via_city)
            customer_data_manager = CustomerDataManager(data.price, data.departure_city, data.departure_airport_code,
                                                        data.arrival_city, data.arrival_airport_code,
                                                        data.departure_time,
                                                        data.arrival_time, number_of_stop_over=data.stop_overs,
                                                        stop_over_city=data.via_city)

        notification_manager.send_message()
        customer_data_manager.send_email()

    index_number += 1
