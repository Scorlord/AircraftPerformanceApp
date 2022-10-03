from aircraft_factory import AircraftFactory
from ast import If
import math


factory = AircraftFactory()
#aircraft = factory.getAircraft("F-86")

#aircraft = factory.getAircraft("B-52")  ## Find Specific Aircraft
performanceWeight = 0  ## desired weight in kilograms
performanceSpeed = 0   ## desired speed in meters per second

def selectAircraft():
    selectMethod = input("Enter selection method, exit to quit, or help for list of selection options: ")
    selectionList = ["Model Name", "Nickname", "Heaviest", "Lightest", "Slowest", "Best Useful Load", "Fastest", "Oldest", "Newest"]
    if selectMethod == "exit":
        exit()
    if selectMethod == "help":
        print("Search able options:")
        print(selectionList)
    elif selectMethod == "Model Name":
        modelName = input("Enter model number: ")
        if modelName == None:
            print("No aircraft found.")
            exit()
        return factory.getModelName(modelName)
    elif selectMethod == "Nickname":
        nickName = input("Enter nickname: ")
        return factory.getNickName(nickName)
    elif selectMethod == "Heaviest":
        return factory.getHeaviestMTOW
    elif selectMethod == "Lightest":
        return factory.getLightestMTOW
    elif selectMethod == "Best Useful Load":
        return factory.getBestUsefulLoad

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
    command = input("Enter Command:")
    if command == "exit":
        exit()
    elif command == "select":
        aircraft = selectAircraft()
        print(str(aircraft.modelName))
        print(str(aircraft.nickName))
    if aircraft == None:
        print("Aircraft could no be found.")
    elif command == "check":
        performanceWeight = round((aircraft.maxTakeOffWeight * .8),2)  ## desired weight in kilograms
        performanceSpeed = round((aircraft.minSpeedSea * 2),2)   ## desired speed in meters per second  

