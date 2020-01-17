# A Table Reservation System For A Restaurant


Introduction:
------
This is a small practice project I got during job interview process. This repo includes a software system design document with all the details. The first part of my work is to design the system model based on task problem, the second part of my work is to implement and test the system I built. I use flask as framework to build and test system model.

User Case:
------
![GitHub Logo](/img/user1.png)
![GitHub Logo](/img/user2.png)
![GitHub Logo](/img/user3.png)

Interaction Diagram:
------
![GitHub Logo](/img/system.png)

Task Problem:
------
PROBLEM 1 Your job is to create a reservation system for a restaurant. The restaurant has N tables. You need to be able to provide following functionality for this system. Let user reserve a table or clear a reservation.
- In a restaurant, there are multiple tables with varying seating capacities.
- A table of seating capacity of n can be booked for m people of a group such that m <= n.
- A table can be re-booked for the same day only if there is a minimum T duration
- difference between 2 bookings.
- Booking can be done in fixed hours when the restaurant operates

Task: First, start with a design and identify the classes, data members and interfaces needed and how they will interact with each other. Define all the entities need for this application and the assumptions you are going to make. And Implement the classes and interfaces defined above.

PROBLEM 2 (Extending your solution to add additional features via Feature Flags)
Suggest other “optional” features you would like to add to your reservation system. Depending on the client vendor, you should be able to enable/disable these features (Think of these features which would enhance your solution for customers)

Installation:
------
$ virtualenv flask

$ cd flask

$ source bin/activate

$ pip install flask

$ pip install Flask-SQLAlchemy

$ pip install flask-wtf

$ python run.py

Application Testing:
------
![GitHub Logo](/img/screen1.png)
![GitHub Logo](/img/screen2.png)
![GitHub Logo](/img/screen3.png)




