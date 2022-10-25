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
        if selectMethod.lower() == "exit":
            exit()
        elif selectMethod.lower() == "help":
            print("Search able options:")
            print(selectionList)
            continue
        elif selectMethod.lower() == "back":
            return
        elif selectMethod.lower() == "model name":
            modelName = input("Enter model number: ").upper()
            selectedAircraft = factory.getModelName(modelName)
        elif selectMethod.lower() == "nickname":
            nickName = input("Enter nickname: ").title()
            selectedAircraft = factory.getNickName(nickName)
        elif selectMethod.lower() == "heaviest":
            selectedAircraft = factory.getHeaviestMTOW()
        elif selectMethod.lower() == "lightest":
            selectedAircraft = factory.getLightestMTOW()
        elif selectMethod.lower() == "best useful load":
            selectedAircraft = factory.getBestUsefulLoad()
        elif selectMethod.lower() == "fastest":
            selectedAircraft = factory.getFastedMaxSpeed()
        elif selectMethod.lower() == "slowest":
            selectedAircraft = factory.getSlowestMaxSpeed()
        elif selectMethod.lower() == "oldest":
            selectedAircraft = factory.getOldestIntroDate()
        elif selectMethod.lower() == "newest":
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
    if command.lower() == "exit":
        exit()
    elif command.lower() == "select":
        aircraft = selectAircraft()
        factory.printAircraft(aircraft)
    elif command == "list aircraft":
        print("Model Name: _____ | Nickname: _____ | Nation of origin: _____ | Introduction year: _____ ")
        factory.printAicraftList()
        continue
    elif command.lower() == "compare":
        compareAircraft = selectAircraft()
        if compareAircraft != None:
            print("Selected aircraft is " + compareAircraft.modelName + " " + compareAircraft.nickName + ".")
    elif command.lower() == "check":
        if aircraft == None:
            print("No aircraft selected, please select to continue.")
            continue
        speed = checkPerformanceSpeed()
        weight = checkPerformanceWeight()
        print(f'Model Name: {aircraft.modelName} | Performance Speed: {aircraft.nickName} | Performance Weight: {aircraft.nation}')


