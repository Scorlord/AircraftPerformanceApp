from select import select
from aircraft_factory import AircraftFactory
from ast import If
import math

factory = AircraftFactory()
aircraft = factory.getHeaviestMTOW()
performanceWeight = round((aircraft.maxTakeOffWeight * .8),2)
performanceSpeed = round((aircraft.minSpeedSea * 2),2)

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

print(f'The {aircraft.modelName} {aircraft.nickName} was made in the {aircraft.nation} and was introduced in {aircraft.year}. The {aircraft.nickName} uses a {aircraft.airFoil} airfoil, which has a max sea level speed of {aircraft.maxSpeedSea} m/s, and stalls at {aircraft.minSpeedSea} m/s.')
print(f'With an empty weight of {aircraft.emptyWeight} kg, and max-take-off-weight of {aircraft.maxTakeOffWeight} kg, which gives it a useful load of {aircraft.maxTakeOffWeight - aircraft.emptyWeight} k/g. Minus the max internal fuel load of {aircraft.maxInternalfuel} kg, allows it to carry {aircraft.maxTakeOffWeight - aircraft.emptyWeight - aircraft.maxInternalfuel} kg mission load.')
print(f'If the {aircraft.nickName} is at a speed of {performanceSpeed} m/s, and has a weight of {performanceWeight} kg({weightPercentage}% of MTOW) we can determine the following.')
    
if instantTurnThrustRequiredAns > (aircraft.thrust + aircraft.afterburner):
    print(f'That the {aircraft.modelName} has an instant turn rate of {instantTurnRateAns} degrees per second, and instant turn radius of {instantTurnradiusAns} meters, which is higher than its substained turn rate.')
    print(f'Where its susbtained turn occurs at {bestTurnSpeedAns} m/s, giving it a radius of {bestTurnRadiusAns} meters, and turn rate of {bestTurnRateAns} degrees per second.')
    exit()

if instantTurnThrustRequiredAns < (aircraft.thrust + aircraft.afterburner):
    print(f'That the {aircraft.modelName} has a substained turn rate of {instantTurnRateAns} degrees per second, and substained turn radius of {instantTurnradiusAns} meters, which is lower than its best turn rate.')
    print(f'Where its best susbtained turn rate occurs at {bestTurnSpeedAns} m/s. Giving it a turn radius of {bestTurnRadiusAns} meters, at a turn rate of {bestTurnRateAns} degrees per second.')
    exit()

if instantTurnThrustRequiredAns == (aircraft.thrust + aircraft.afterburner): 
    print(f'That the {aircraft.modelName} has a substained turn rate of {instantTurnRateAns} degrees per second, and substained turn radius of {instantTurnradiusAns} meters.')
    exit()
