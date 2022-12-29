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
        self.tequila_header = {
            "apikey": self.tequila_api_key
        }

    def find_location(self):
        tequila_parameters = {
            "term": self.locationName
        }
        iata_code = requests.get(url=self.tequila_endpoint, headers=self.tequila_header, params=tequila_parameters)
        output = iata_code.json()
        return output["locations"][0]["code"]

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
        # print(type(data_json))
        # print(data_json[""])
        # print(search_price.text)
        # search_price.raise_for_status()
        try:
            result = data_json['data'][0]['price']
            self.departure_time = data_json['data'][0]["route"][0]["local_departure"].split("T")[0]
            self.arrival_time = data_json['data'][0]["route"][0]["local_arrival"].split("T")[0]
        except IndexError:
            result = f"No flights found for {fly_to_iata_code}"
        return result

