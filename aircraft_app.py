from aircraft_factory import AircraftFactory
from ast import If
import math


factory = AircraftFactory()
aircraft = "F-80"

aircraft = factory.getAircraft("B-52")  ## Find Specific Aircraft
performanceWeight = round((aircraft.maxTakeOffWeight * 1),2)  ## desired weight in kilograms
performanceSpeed = round((aircraft.maxSpeedSea * .5),2)   ## desired speed in meters per second


if performanceWeight < aircraft.emptyWeight:
    print("Weight not acceptable as it is less than the aircraft empty weight.")
    exit()
if performanceWeight > aircraft.maxTakeOffWeight:
    print("Weight not acceptable as it is more than aircraft maxium take off weight.")
    exit()
else:
    pass
if performanceSpeed < aircraft.minSpeedSea:
    print("Speed cannot be less than stall speed.")
    exit()
else:
    pass


def bestTurnDyanmicPressure(wingArea, thrust, zeroLiftDrag, inducedDrag, maxLift):
    return ((1 / wingArea) * (thrust / (zeroLiftDrag + inducedDrag * (maxLift**2))))*100

bestTurnDyanmicPressureAns = bestTurnDyanmicPressure(wingArea = aircraft.wingArea, thrust = (aircraft.thrust + aircraft.afterburner), zeroLiftDrag = aircraft.zeroLiftDrag(), inducedDrag = aircraft.inducedDrag(), maxLift = aircraft.maxLift())

def bestTurnSpeed(dynamicPressure):
    return math.sqrt((2 * dynamicPressure * 1000) / 1.225) 

bestTurnSpeedAns = round(bestTurnSpeed(dynamicPressure = bestTurnDyanmicPressureAns), 2)

def bestTurnLoadFactor(wingArea, maxLift, dynamicPressure, weight):
    return (wingArea * maxLift * 100 * dynamicPressure) / weight

bestTurnFactorAns = bestTurnLoadFactor(wingArea = aircraft.wingArea, maxLift= aircraft.maxLift(), dynamicPressure= bestTurnDyanmicPressureAns, weight = performanceWeight)

def bestTurnRate(velocity, loadFactor):
    return (9.8 / velocity) * math.sqrt((loadFactor ** 2) -1) * 180 / math.pi

bestTurnRateAns = round(bestTurnRate(velocity = bestTurnSpeedAns, loadFactor = bestTurnFactorAns), 2)

def bestTurnRadius(velocity, loadFactor):
    return (velocity**2)/9.8 * (1 / math.sqrt((loadFactor **2) -1))

bestTurnRadiusAns = round(bestTurnRadius(velocity = bestTurnSpeedAns, loadFactor = bestTurnFactorAns), 2)

def instantTurnRadiusFunction(weight, pressure,  surfaceArea, maxLift, frameLimit): ## Instant turn radius, typically not equal to substained radius
    return (weight / (0.5 * pressure * surfaceArea * maxLift)) * (frameLimit / math.sqrt((frameLimit **2) - 1))

instantTurnradiusAns = round((instantTurnRadiusFunction(weight = performanceWeight, pressure = 1.225, surfaceArea = aircraft.wingArea, maxLift = aircraft.maxLift(), frameLimit = aircraft.structuralLimit)), 2)

def instantTurnRateFunction(weight, pressure,  surfaceArea, maxLift, frameLimit): ## Instant turn rate, typically not equal to substained rate
    return ( ( (9.80665 * (math.sqrt( (0.5 * pressure * surfaceArea * maxLift) / weight)) * (frameLimit / math.sqrt((frameLimit **2) - 1)) ) * 180 ) / math.pi)

instantTurnRateAns = round((instantTurnRateFunction(weight = performanceWeight, pressure = 1.225, surfaceArea = aircraft.wingArea, maxLift = aircraft.maxLift(), frameLimit = aircraft.structuralLimit)), 2)

def instantTurnThrustRequired(zeroLiftDrag, inducedDrag, maxLift, velocity, wingArea):
    return ((zeroLiftDrag + inducedDrag * (maxLift**2)) * 1.225 * velocity * wingArea)/1000

instantTurnThrustRequiredAns = instantTurnThrustRequired(zeroLiftDrag = aircraft.zeroLiftDrag(), inducedDrag = aircraft.inducedDrag(), maxLift = aircraft.maxLift(), velocity = performanceSpeed, wingArea = aircraft.wingArea)

def performanceWeightPercentage(weight, mtow):
    return (weight / mtow) * 100

weightPercentage = round(performanceWeightPercentage(weight = performanceWeight, mtow = aircraft.maxTakeOffWeight), 0)

print("The " + aircraft.modelName + " " + aircraft.nickName + " was made in the " + aircraft.nation + " and was introduced in " + str(aircraft.year) + ". The " + aircraft.nickName + " uses a " + aircraft.airFoil + " airfoil, which has a max sea level speed of " + str(aircraft.maxSpeedSea) + " m/s, and stalls at " + str(aircraft.minSpeedSea) + " m/s.")
print("With an empty weight of " + str(aircraft.emptyWeight) + " kg, and max-take-off-weight of " + str(aircraft.maxTakeOffWeight) + " kg, which gives it a useful load of " + str(aircraft.maxTakeOffWeight - aircraft.emptyWeight)+ " k/g. Minus the max internal fuel load of " + str(aircraft.maxInternalfuel) + " kg, allows it to carry " + str(aircraft.maxTakeOffWeight - (aircraft.emptyWeight - aircraft.maxInternalfuel)) + " kg mission load.")
print("If the " + aircraft.nickName + " is at a speed of " + str(performanceSpeed) + " m/s, and has a weight of " + str(performanceWeight) + " kg(" + str(weightPercentage)  + "% of MTOW) we can determine the following.")
    
if instantTurnThrustRequiredAns > (aircraft.thrust + aircraft.afterburner):
    print("That the " + aircraft.modelName + " has an instant turn rate of " + str(instantTurnRateAns) + " degrees per second, and instant turn radius of " + str(instantTurnradiusAns) + " meters, which is higher than its substained turn rate.")
    print("Where its susbtained turn occurs at " + str(bestTurnSpeedAns) + " m/s, giving it a radius of " + str(bestTurnRadiusAns) + " meters, and turn rate of " + str(bestTurnRateAns) + " degrees per second.")
    exit()

if instantTurnThrustRequiredAns < (aircraft.thrust + aircraft.afterburner):
    print("That the " + aircraft.modelName + " has a substained turn rate of " + str(instantTurnRateAns) + " degrees per second, and substained turn radius of " + str(instantTurnradiusAns) + " meters, which is lower than its best turn rate.")
    print("Where its best susbtained turn rate occurs at " + str(bestTurnSpeedAns) + " m/s. Giving it a turn radius of " + str(bestTurnRadiusAns) + " meters, at a turn rate of " + str(bestTurnRateAns) + " degrees per second.")
    exit()

if instantTurnThrustRequiredAns == (aircraft.thrust + aircraft.afterburner): 
    print("That the " + aircraft.modelName + " has a substained turn rate of " + str(instantTurnRateAns) + " degrees per second, and substained turn radius of " + str(instantTurnradiusAns) + " meters.")
    exit()
