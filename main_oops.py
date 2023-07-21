import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv("hotels.csv", dtype={'id': str})


# Abstract class is a class that cannot be instantiated
# All of its subclasses must implement Abstract class methods
# So Hotel and ReservationTicket class must implement this generate method.
class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class Hotel:
    # The class and methods are a blueprint for instance(objects)

    watermark = "The United Kingdom Company"

    # Class variable - common for all

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        # init - Whenever you're creating a class instance, this method is called in background. 
        # init - If you want to add arguments in class, then put them in init method
        # self - a variable which holds instance that is being created
        # self.name - Instance variable(Specific to what instance you're creating) [{hotel_id}: Left side - property of variable, Right side - value] 
        # arguments in this method can be used for all of this class's methods

    def book(self):
        """Book a hotel and change its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # Magic methods - overwriting the behaviour of method
    # Initially, returns False when comparing two instance of same variable(hotel_object), but now returns True
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False
    # OUTPUT:
    # hotel = Hotel("655")
    # hotel1 = Hotel("655")
    # hotel == hotel1
    # True

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f""""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel: {self.hotel.name}
        """
        return content

    # Property -> Defined as a method, but behaves like a variable, so used in above method as a variable
    # Here -> the_customer_name = name
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2
    # Used to perform  calculation or conversion that is relevant to the class as a whole
    # But does not depend on any specific instance variables.


hotel = Hotel(hotel_id="134")
hotel1 = Hotel(hotel_id="456")

print(hotel1.available())

print(hotel.name)
print(hotel1.name)

print(hotel.watermark)
print(hotel1.watermark)

print(Hotel.watermark)

print(Hotel.get_hotel_count(data=df))
print(hotel1.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="gowtham selvaraj  ", hotel_object=hotel1)
print(ticket.the_customer_name)
# For property, you don't need to mention (), coz it behaves like a variable
print(ticket.generate())

converted = ReservationTicket.convert(10)
print(converted)
