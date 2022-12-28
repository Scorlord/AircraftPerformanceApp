#Comparrisons of Airframes
from select import select
from aircraft_factory import AircraftFactory
from aircraft_equations import *
from ast import If
import math


def comparisonOfAircraft():
    comparison == None
    while comparison == None:
        comparisonMethod = input("Please enter what comparison or comparions you wish to view: ")
        comparisonList = ["Introduction Year, Weight, Length, Wingspan, Wing Area, Thrust, Thrust vs Weight, Max Speed, Stall Speed, Energy-Maneuverability Factor, All, or Exit"]
        if comparisonMethod.lower() == "exit":
            exit()
         elif comparisonMethod.lower() == "help":
            print("Search able options:")
            print(comparisonList)
            continue



