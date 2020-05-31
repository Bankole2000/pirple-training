"""
Name: functions.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #2
Task: Functions to return values of 
      data from Homework #1 (main.py) 
"""

from main import *


def genre():
    print(f"Genre: {Genre}")
    return Genre


def artist():
    print(f"Artist: {Artist}")
    return Artist


def year():
    print(f"Year: {YearReleased}")
    return YearReleased


def inStoresNow():
    if InStoresNow:
        print(f"Out Now!!! (ie InStoresNow == {InStoresNow})")
        return(InStoresNow)
    else:
        print(f"Not available in stores (ie InStoresNow == {False})")
        return(False)


genre()
artist()
year()
inStoresNow()
