from select import select
from aircraft_factory import AircraftFactory
from ast import If
import math


factory = AircraftFactory()
#aircraft = factory.getAircraft("F-86")

#aircraft = factory.getAircraft("B-52")  ## Find Specific Aircraft
performanceWeight = 0  ## desired weight in kilograms
performanceSpeed = 0   ## desired speed in meters per second



def selectAircraft():
    selectedAircraft = None
    while selectedAircraft == None:
        selectMethod = input("Enter selection method, exit to quit, or help for list of selection options: ")
        selectionList = ["Model Name", "Nickname", "Heaviest", "Lightest", "Slowest", "Best Useful Load", "Fastest", "Oldest", "Newest"]
        if selectMethod == "exit":
            exit()
        elif selectMethod == "help":
            print("Search able options:")
            print(selectionList)
            continue
        elif selectMethod == "Model Name":
            modelName = input("Enter model number: ")
            selectedAircraft = factory.getModelName(modelName)
        elif selectMethod == "Nickname":
            nickName = input("Enter nickname: ")
            selectedAircraft = factory.getNickName(nickName)
        elif selectMethod == "Heaviest":
            selectedAircraft = factory.getHeaviestMTOW()
        elif selectMethod == "Lightest":
            selectedAircraft = factory.getLightestMTOW()
        elif selectMethod == "Best Useful Load":
            selectedAircraft = factory.getBestUsefulLoad()
        elif selectMethod == "Fastest":
            selectedAircraft = factory.getFastedMaxSpeed()
        elif selectMethod == "Slowest":
            selectedAircraft = factory.getSlowestMaxSpeed()
        elif selectMethod == "Oldest":
            selectedAircraft = factory.getOldestIntroDate()
        elif selectMethod == "Newest":
            selectedAircraft = factory.getNewestIntroDate()
        else:
            print("Not a valid method.")
            continue

    if selectedAircraft == None:
        print("No aircraft selected, please select one to continue.")
    else:
        return selectedAircraft


def checkPerformanceWeight():
    checkWeight = input("Enter performance weight in kilograms.")
    if checkWeight < aircraft.emptyWeight:
        print("Weight cannot be less than empty weight of aircraft.")
        exit()
    if checkWeight > aircraft.maxTakeOffWeight:
        print("Weight cannot be more than max take off weight for aircraft.")
    else:
        performanceWeight = checkWeight

def checkPerformanceSpeed():
    checkSpeed = input("Enter peformance speed in meters per second.")
    if checkSpeed < aircraft.minSpeedSea:
        print("Speed cannont be less than aircraft stall speed.")
    else:
        performanceSpeed = checkSpeed


while True:
    aircraft = None
    command = input("Enter Command:")
    if command == "exit":
        exit()
    elif command == "select":
        aircraft = selectAircraft()
        print("Selected aircraft is " + aircraft.modelName + " " + aircraft.nickName + ".")
        continue
    elif command == "Stat Display":
        aircraft = selectAircraft()
        print(aircraft.aircraftList)
        continue
    elif command == "check":
        if aircraft == None:
            print("No aircraft selected, please select to continue.")
            continue
        performanceWeight = round((aircraft.maxTakeOffWeight * .8),2)  ## desired weight in kilograms
        performanceSpeed = round((aircraft.minSpeedSea * 2),2)   ## desired speed in meters per second  


