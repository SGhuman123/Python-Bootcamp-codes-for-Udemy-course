# Description

This program is a modification of the single user flight dealer program. It can now notify multiple users.
The program allows users to find the cheapest flight deals. First, key in the location they are starting from. Then the program would work with Google sheets.  Users will first be prompted the following: "Which city will you be flying from?". This will get the departure location of the user. The program will then ask the user the following:

1) "Where do you want to go to?"
2) "What is your budget?"
3) "Anywhere else you wish to go? (Y/N) answers only"
3a) If "Y" is inputed, then steps 1-3 will repeat itself until "N" is selected
3b) If "N" is inputed, then steps 1-3 will not repeat itself


Then through the help of the Sheety API, it will read the data off the Google sheet.

<img width="340" alt="Screenshot 2022-12-29 at 4 20 51 PM" src="https://user-images.githubusercontent.com/63066897/209923886-9a7b2409-43d8-44a1-9abe-bf5c0a67b151.png">


Then it will update the list with the appropriate IATA codes to produce the result as seen below which is done through the use of the KIWI API.

<img width="390" alt="Screenshot 2022-12-29 at 4 21 45 PM" src="https://user-images.githubusercontent.com/63066897/209923993-5be0766b-63a9-473e-9111-e7bb811bf5c1.png">

Moreover, when searching for flights, we not not only look for direct flights, that leave anytime between tomorrow and in 6 months (6x30days) time, round trips that return between 7 and 28 days in length but we also look at flights with stopovers.

Then the program shall ask the following:
1) "Welcome to Hikari's Flight Club. We find the best flight deals and email you."
2) "What is your first name?"
3) "What is your last name?"
4) "What is your email?"
5) "Type your email again."
6) "You're in the club!"

<img width="405" alt="Screenshot 2022-12-29 at 7 39 03 PM" src="https://user-images.githubusercontent.com/63066897/209945952-1ce20313-8459-4286-af5c-a8fc52fd7915.png">


Subsequently, if the price found by the API is indeed lower than the one in the Google sheet, then we shall receive a message from the Twilio API to let us know that there is a much cheaper flight deal. The user also the inputed email as well as other email of usaers stored in the Google sheet shall also receive the email.

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
6) customer_data_system_manager.py

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
- add_location_and_price(self, location, price): this method is responsible for adding the location name as well as the user's budget to the Google sheet.

customer_data_system_manager.py is where the class CustomerDataManager() resides and it is the class in charge of managing the information of the customers on the Google sheets.
- add_user_to_database(self): This method is in charge of adding the first name, last name and email of the users to the Google sheets.
- send_email(self): This class is responsible for sending emails to users whose details have been stored in the database.
