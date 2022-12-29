import requests
# from flight_data import FlightData
import datetime


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, locationName, fly_from):
        self.locationName = locationName
        self.fly_from = fly_from
        self.tequila_parameters = None
        self.tequila_api_key = "YOUR FLIGHT SEARCH API KEY"
        self.tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.tequila_endpoint_search_api = "https://api.tequila.kiwi.com/v2/search"
        self.departure_time = None
        self.arrival_time = None
        self.stop_over = None
        self.tequila_header = {
            "apikey": self.tequila_api_key
        }

    # The purpose of this function is to get the code of the location
    def find_location(self):
        tequila_parameters = {
            "term": self.locationName
        }
        iata_code = requests.get(url=self.tequila_endpoint, headers=self.tequila_header, params=tequila_parameters)
        output = iata_code.json()
        # if self.locationName == "Bali":
        #     print(output)
        result = output["locations"][0]["code"]
        if not result.isupper():
            result = output["locations"][0]["locations_nearby"][0]["id"]
        return result

    def search_price(self, fly_to_iata_code, fly_from_iata_code):
        # print(self.fly_from)
        # print(fly_from_iata_code)
        tequila_search_api_parameters = {
            "fly_from": fly_from_iata_code,
            "fly_to": fly_to_iata_code,
            "date_from": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.datetime.now() + datetime.timedelta(days=6 * 30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "SGD",
            "one_for_city": 1
            # dd/mm/yyyy format
        }
        # print(self.tequila_header)
        search_price = requests.get(url=self.tequila_endpoint_search_api,
                                    headers=self.tequila_header,
                                    params=tequila_search_api_parameters)
        data_json = search_price.json()
        # print(data_json)
        # print(type(data_json))
        # print(data_json[""])
        # print(search_price.text)
        # search_price.raise_for_status()

        try:
            # This is to extract the departure and arrival time of the locations
            result = data_json['data'][0]['price']
            self.departure_time = data_json['data'][0]["route"][0]["local_departure"].split("T")[0]
            self.arrival_time = data_json['data'][0]["route"][0]["local_arrival"].split("T")[0]
            # print(data_json)

            return result

        except IndexError or KeyError:
            # print("IndexError working")
            try:
                tequila_search_api_parameters = {
                    "fly_from": fly_from_iata_code,
                    "fly_to": fly_to_iata_code,
                    "date_from": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"),
                    "date_to": (datetime.datetime.now() + datetime.timedelta(days=6 * 30)).strftime("%d/%m/%Y"),
                    "nights_in_dst_from": 7,
                    "nights_in_dst_to": 28,
                    "flight_type": "round",
                    "max_stopovers": 2,
                    "curr": "SGD",
                    "one_for_city": 1
                    # dd/mm/yyyy format
                }
                # print(self.tequila_header)
                search_price = requests.get(url=self.tequila_endpoint_search_api,
                                            headers=self.tequila_header,
                                            params=tequila_search_api_parameters)
                data_json = search_price.json()
                result = data_json['data'][0]['price']
                self.departure_time = data_json['data'][0]["route"][0]["local_departure"].split("T")[0]
                self.arrival_time = data_json['data'][0]["route"][2]["local_arrival"].split("T")[0]
                self.stop_over = data_json['data'][0]["route"][0]["cityTo"]
                # print(data_json)
            except KeyError:
                result = f"No flights found for {fly_to_iata_code}"

            return result
            # result = data_json
            # print(result)
