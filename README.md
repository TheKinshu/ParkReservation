# Park Reservation Selenium Webdriver

This Selenium Webdriver is dedicated to Ontario Parks to help users automate the proccess of selecting a campsite. User will enter informations beforehand to give to the webdriver.

## Installation 

Use the requirements.txt to install the require packages

```bash
pip install -r requirements.txt
```

## Getting Started

Firstly, open camp.txt file:

```bash
Username: ~~~~
Password: ~~~
Equipment: Trailer or RV up to 32ft (9.7m)
partySize: 3
serviceType:Electric
MonthOfArrival: Aug 
DateOfArrival: 30
NightStayed: 7
Campsite: Algonquin - Lake Of Two Rivers Campground
```

Options you can choose to select (Recommend to copy the following information to avoid type errors):
```bash
Equipment:
2 Tents
3 Tents
Trailer or Rv up to 18ft (5.5m)
Trailer or Rv up to 25ft (7.6m)
Trailer or Rv up to 32ft (9.7m)
Trailer or Rv up over 32ft (9.7m)

Park/Campsite:
A full list of the parks is in location.txt file

MonthOfArrival:
Use the first three character of the month with the first letter capitalize.

DateOfArrival:
The day of the month you wish to go to.

NightStayed:
The length of stay duration.

serviceType: 
No-Preference
Non-Electric
Electric

partySize:
From 1-6
```

Once open you can modifiy any of the pre-set information located.

Secondly, click on the batch file to run the program.

Lastly, once everything is completed log-in to ontarioparks.com to complete the transaction.