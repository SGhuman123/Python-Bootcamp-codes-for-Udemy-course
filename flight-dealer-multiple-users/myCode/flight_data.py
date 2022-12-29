class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, departureAirportCode, departureCity, arrivalAirportCode, arrivalCity, departureTime, arrivalTime, stop_overs=0, via_city=""):
        self.price = price
        self.departure_airport_code = departureAirportCode
        self.departure_city = departureCity
        self.arrival_airport_code = arrivalAirportCode
        self.arrival_city = arrivalCity
        self.departure_time = departureTime
        self.arrival_time = arrivalTime
        self.stop_overs = stop_overs
        self.via_city = via_city

