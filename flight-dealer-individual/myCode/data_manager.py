import requests
from flight_search import FlightSearch
from flight_data import FlightData


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {"Authorization": "TOKEN"}
        self.get_sheety_endpoint = "YOUR SHEETY PRICES ENDPOINT"
        self.fly_from = input("Which city will you be flying from?")
        self.fly_from_iata_code = FlightSearch(self.fly_from, None).find_location()
        self.data_storer = []
        self.send_message = []

    def get_current_data(self):
        current_data = requests.get(url=self.get_sheety_endpoint, headers=self.headers)
        return current_data.json()

    def update_list(self):
        current_data_to_be_updated = self.get_current_data()["prices"]
        for city in current_data_to_be_updated:
            # print(city["city"])
            city_to_fly_to = FlightSearch(city["city"], self.fly_from)
            city["iataCode"] = city_to_fly_to.find_location()
            # print(city["iataCode"])
            city_parameters = {"price": {key: value for (key, value) in city.items()}}
            put_sheety_endpoint = f"{self.get_sheety_endpoint}/{city['id']}"
            # print(city_parameters)
            # tester is to test search_price() function
            # print(city["iataCode"])

            price = city_to_fly_to.search_price(city["iataCode"], self.fly_from_iata_code)
            # departure_time = city_to_fly_to.
            arrival_time = city_to_fly_to.arrival_time
            departure_time = city_to_fly_to.departure_time
            travel_location_data = FlightData(price, self.fly_from_iata_code, self.fly_from, city["iataCode"],
                                              city["city"], departure_time, arrival_time)
            self.data_storer.append(travel_location_data)
            requests.put(url=put_sheety_endpoint, headers=self.headers, json=city_parameters)

    def compare_price(self):
        current_data_to_be_updated = self.get_current_data()["prices"]
        index_number = 0
        for city in current_data_to_be_updated:
            try:
                if int(self.data_storer[index_number].price) < int(city['lowestPrice']):
                    self.send_message.append({"cityName": city["city"], "lowerPrice": True})
                else:
                    self.send_message.append({"cityName": city["city"], "lowerPrice": False})
            except ValueError:
                self.send_message.append({"cityName": city["city"], "lowerPrice": False})
            index_number += 1
