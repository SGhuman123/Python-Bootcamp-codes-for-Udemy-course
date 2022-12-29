# Description

This program allows users to find the cheapest flight deals. First, key in the location they are starting from. Then the program would work with Google sheets.  Users will first be prompted the following: "Which city will you be flying from?". This will get the departure location of the user. Then through the help of the Sheety API, it will read the data off the Google sheet.

<img width="340" alt="Screenshot 2022-12-29 at 4 20 51 PM" src="https://user-images.githubusercontent.com/63066897/209923886-9a7b2409-43d8-44a1-9abe-bf5c0a67b151.png">


Then it will update the list with the appropriate IATA codes to produce the result as seen below which is done through the use of the KIWI API.

<img width="390" alt="Screenshot 2022-12-29 at 4 21 45 PM" src="https://user-images.githubusercontent.com/63066897/209923993-5be0766b-63a9-473e-9111-e7bb811bf5c1.png">

Moreover, when searching for flights, we are looking only for direct flights, that leave anytime between tomorrow and in 6 months (6x30days) time. We are also looking for round trips that return between 7 and 28 days in length.

Subsequently, if the price found by the API is indeed lower than the one in the Google sheet, then we shall receive a message from the Twilio API to let us know that there is a much cheaper flight deal.

## Modification of program from solution code:

In my program unlike the provided solution code that assumes the user starts from London, my program allows the users to choose their starting location.


## Folder description

1) myCode: This folder contains my original code to the flight dealer challenge
2) providedSol: This folder contains the provided code by the course instructor Dr Angela Yu to the flight dealer challenge

## Files descriptions:
Inside both the myCode and providedSol folders, both contains 5 py files of the same name which are:
1) main.py
2) flight_search.py
3) notification_manager.py
4) flight_data.py
5) data_manager.py

main.py is where the program is run.

flight_search.py is where the class FlightSearch() resides. This class contains the following methods:
- find_location(self) which is in charge of finding the IATA code of the desired location.
- search_price(self) which is in charge of finding the price of the from the user's inputed location to his or her desired destination.

notification_manager.py is where the class NotificationManager() resides it has a method:
- send_message() which is in charge of sending message to the desired user if there is a price lower than their budget.

flight_data.py is where the class FlightData() resides and is the class that is in charge of storing the necessary flight data such as the price, departure airport code, departure city, arrival airport code, arrival city, departure time and arrival time.

data_manager.py is where the class DataManager() resides. This class contains the methods:
- get_current_data(self): this is used to obtain the data from the Google sheets
- update_list(self): this method is used to update the IATA code column of the Google sheet with the appropriate IATA codes.
- compare_price(self): this method is used to compare the price of the budget the user have for the flight (the price in the google sheet) to the price obtained in from the API. If the price is lower the user will then receive a message through the help of the Twilio API otherwise, the user will receive the message, to notifiy them of the low price alert otherwise no message is sent. 





