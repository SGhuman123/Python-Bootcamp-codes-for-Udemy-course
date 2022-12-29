class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, departureAirportCode, departureCity, arrivalAirportCode, arrivalCity, departureTime, arrivalTime):
        self.price = price
        self.departure_airport_code = departureAirportCode
        self.departure_city = departureCity
        self.arrival_airport_code = arrivalAirportCode
        self.arrival_city = arrivalCity
        self.departure_time = departureTime
        self.arrival_time = arrivalTime

