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

    # The purpose of this function is to get all the data currently on the google sheets
    def get_current_data(self):
        current_data = requests.get(url=self.get_sheety_endpoint, headers=self.headers)
        return current_data.json()

    # The purpose of this function is to update the google sheets with the IATA code of each location
    def update_list(self):
        current_data_to_be_updated = self.get_current_data()["prices"]
        for city in current_data_to_be_updated:
            # print(city["city"])

            # This is to obtain the IATA code of the city to fly to
            city_to_fly_to = FlightSearch(city["city"], self.fly_from)
            city["iataCode"] = city_to_fly_to.find_location()
            # print(city["iataCode"])

            # This is to update the IATA code of the city to the google sheets
            city_parameters = {"price": {key: value for (key, value) in city.items()}}
            put_sheety_endpoint = f"{self.get_sheety_endpoint}/{city['id']}"
            # print(city_parameters)
            # tester is to test search_price() function
            # print(city["iataCode"])

        # TODO: look into the search_price function find a way that allows 1 stopover if there are
        # TODO: no direct flights
            # This searches for price of getting from one location to the next
            price = city_to_fly_to.search_price(city["iataCode"], self.fly_from_iata_code)

            # This is to get the arrival_time and departure_time of the flight
            arrival_time = city_to_fly_to.arrival_time
            departure_time = city_to_fly_to.departure_time

            # This is to put the travel location data in an appropriate format and store it in a list called self.data_storer
            if city_to_fly_to.stop_over is None:
                travel_location_data = FlightData(price, self.fly_from_iata_code, self.fly_from, city["iataCode"],
                                                  city["city"], departure_time, arrival_time)
            elif city_to_fly_to.stop_over is not None:
                travel_location_data = FlightData(price, self.fly_from_iata_code, self.fly_from, city["iataCode"],
                                                  city["city"], departure_time, arrival_time, stop_overs=1, via_city=city_to_fly_to.stop_over)

            self.data_storer.append(travel_location_data)
            requests.put(url=put_sheety_endpoint, headers=self.headers, json=city_parameters)

    def compare_price(self):
        current_data_to_be_updated = self.get_current_data()["prices"]
        index_number = 0
        for city in current_data_to_be_updated:
            try:
                print(int(self.data_storer[index_number].price))
                print(city)
                if int(self.data_storer[index_number].price) < int(city['lowestPrice']):
                    self.send_message.append({"cityName": city["city"], "lowerPrice": True})
                else:
                    self.send_message.append({"cityName": city["city"], "lowerPrice": False})
            except ValueError:
                self.send_message.append({"cityName": city["city"], "lowerPrice": False})
            # except TypeError:
            #     print(self.data_storer[index_number].price)
            index_number += 1

    def add_location_and_price(self, location, price):
        # This is responsible for adding the location and price to the google sheets
        post_sheety_endpoint = self.get_sheety_endpoint
        sheety_parameters = {
            "price": {
                "city": location,
                "iATACode": None,
                "lowestPrice": price
            }
        }
        response_sheety = requests.post(url=post_sheety_endpoint, json=sheety_parameters,
                                        headers=self.headers)
        # print(response_sheety.text)

        pass
