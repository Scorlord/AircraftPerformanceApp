from select import select
from aircraft_factory import AircraftFactory
from aircraft_equations import *
from aircraft_comparrison import *
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
        selectionList = ["Model Name", "Nickname", "Heaviest", "Lightest", "Slowest", "Best Useful Load", "Fastest", "Oldest", "Newest", "Best Energy", "Worst Energy", "Index List"]
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
        elif selectMethod.lower() == "best energy":
            selectedAircraft = factory.getBestEnergy()
        elif selectMethod.lower() == "worst energy":
            selectedAircraft = factory.getWorstEnergy()
        elif selectMethod.lower() == "index list":
            factory.printAicraftListIndex()
            idx = input("Enter Index Number: ")
            if idx.isnumeric():
                selectedAircraft = factory.getIndexedAircraft(int(idx))
            else:
                print("Not a valid entry.")
        else:
            print("Not a valid method.")
            continue

    if selectedAircraft == None:
        print("No aircraft selected, please select one to continue.")
    else:
        return selectedAircraft

def selectAircraft2():
    selectedAircraft2 = None
    while selectedAircraft2 == None:
        selectMethod = input("Enter selection method, exit to quit, or help for list of selection options: ")
        selectionList = ["Model Name", "Nickname", "Heaviest", "Lightest", "Slowest", "Best Useful Load", "Fastest", "Oldest", "Newest", "Best Energy", "Worst Energy" , "Index List"]
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
            selectedAircraft2 = factory.getModelName(modelName)
        elif selectMethod.lower() == "nickname":
            nickName = input("Enter nickname: ").title()
            selectedAircraft2 = factory.getNickName(nickName)
        elif selectMethod.lower() == "heaviest":
            selectedAircraft2 = factory.getHeaviestMTOW()
        elif selectMethod.lower() == "lightest":
            selectedAircraft2 = factory.getLightestMTOW()
        elif selectMethod.lower() == "best useful load":
            selectedAircraft2 = factory.getBestUsefulLoad()
        elif selectMethod.lower() == "fastest":
            selectedAircraft2 = factory.getFastedMaxSpeed()
        elif selectMethod.lower() == "slowest":
            selectedAircraft2 = factory.getSlowestMaxSpeed()
        elif selectMethod.lower() == "oldest":
            selectedAircraft2 = factory.getOldestIntroDate()
        elif selectMethod.lower() == "newest":
            selectedAircraft2 = factory.getNewestIntroDate()
        elif selectMethod.lower() == "best energy":
            selectedAircraft2 = factory.getBestEnergy()
        elif selectMethod.lower() == "worst energy":
            selectedAircraft2 = factory.getWorstEnergy()
        elif selectMethod.lower() == "index list":
            factory.printAicraftListIndex()
            idx = input("Enter Index Number: ")
            if idx.isnumeric():
                selectedAircraft2 = factory.getIndexedAircraft(int(idx))
            else:
                print("Not a valid entry.")
        else:
            print("Not a valid method.")
            continue

    if selectedAircraft2 == None:
        print("No aircraft selected, please select one to continue.")
    else:
        return selectedAircraft2

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
    command = input("Enter Command or help for options:")
    if command.lower() == "exit":
        exit()
    elif command.lower() == "help":
        print("Command options are Select, Compare, Performance Check, List Aircraft, and Exit.")
    elif command.lower() == "select":
        aircraft = selectAircraft()
        factory.printAircraft(aircraft)
    elif command == "list aircraft" or "list":
        print("Model Name: _____ | Nickname: _____ | Nation of origin: _____ | Introduction year: _____ ")
        factory.printAicraftList()
        continue
    elif command.lower() == "compare":
        compareAircraft = selectAircraft()
        print(f'1st Selected aircraft is {compareAircraft.modelName} {compareAircraft.nickName}.')
        compareAircraft2 = selectAircraft2()
        comparisonOfAircraft()
        #print(f'2nd Selected aircraft is {compareAircraft2.modelName} {compareAircraft2.nickName}')
        #print(f'{compareAircraft.modelName} {compareAircraft.nickName} was first flown by the {compareAircraft.nation} in {compareAircraft.year}. Where the {compareAircraft2.modelName} {compareAircraft2.nickName} was first flown by the {compareAircraft2.nation} in {compareAircraft2.year}.')
        #if compareAircraft.maxSpeedSea > compareAircraft2.maxSpeedSea:
            #print(f'The {compareAircraft.nickName} has a top speed of {compareAircraft.maxSpeedSea} m/s at sea level, which is {round(compareAircraft.maxSpeedSea - compareAircraft2.maxSpeedSea,2)} m/s faster than the {compareAircraft2.nickName} top speed of {compareAircraft2.maxSpeedSea}.')
        #if compareAircraft.maxSpeedSea < compareAircraft2.maxSpeedSea:
            #print(f'The {compareAircraft2.nickName} has a top speed of {compareAircraft2.maxSpeedSea} m/s at sea level, which is {round(compareAircraft2.maxSpeedSea - compareAircraft.maxSpeedSea,2)} m/s faster than the {compareAircraft.nickName} top speed of {compareAircraft.maxSpeedSea} m/s.')

    #elif command.lower() == "performance check" or "performance":
        #aircraft = selectAircraft()
        #print(bestTurnSpeedAns())


    elif command.lower() == "check":
        aircraft = selectAircraft()
        if aircraft == None:
            print("No aircraft selected, please select to continue.")
            continue
        speed = checkPerformanceSpeed()
        weight = checkPerformanceWeight()
        print(f'Model Name: {aircraft.modelName} | Performance Speed: {aircraft.nickName} | Performance Weight: {aircraft.nation}')


