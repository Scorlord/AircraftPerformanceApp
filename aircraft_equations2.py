from aircraft import Aircraft, Fighter, Bomber, Attacker
from cmath import pi, sqrt
from select import select
from aircraft_factory import AircraftFactory
from ast import If
import math

factory = AircraftFactory()
aircraft = factory.getModelName("F-80")
performanceWeight = round((aircraft.maxTakeOffWeight * .8),2)
performanceSpeed = round((aircraft.maxSpeedSea * 1),2)


def instantTurnDynamicPressure(weight,wingArea, zeroLiftDrag, inducedDrag):
    return (weight / wingArea) * sqrt(zeroLiftDrag/inducedDrag) 
instantTurnDynamicPressureAns = instantTurnDynamicPressure(weight = performanceWeight, wingArea = aircraft.wingArea, zeroLiftDrag = aircraft.zeroLiftDrag(), inducedDrag= aircraft.inducedDrag())

def instantTurnSpeedPressure(velocity):
    return (velocity**2*1.225)/2
instantTurnSpeedPressureAns = instantTurnSpeedPressure(velocity=performanceSpeed)

def instantTurnSpeed(dynamicPressure):
    return sqrt((2*dynamicPressure)/ 1.225)
instantTurnSpeedAns = instantTurnSpeed(dynamicPressure=instantTurnSpeedPressureAns)

def instantTurnRadius(velocity, structuralLimit):
    return (velocity**2 / 9.81) * 1/sqrt(structuralLimit^2-1)
instantTurnRadiusAns = instantTurnRadius(velocity = performanceSpeed, structuralLimit = aircraft.structuralLimit)

def instantTurnRate(velocity, structuralLimit):
    return  ( ( (9.81 / velocity) *sqrt(structuralLimit^2-1) ) *180 ) / math.pi
instantTurnRateAns = instantTurnRate(velocity = performanceSpeed, structuralLimit = aircraft.structuralLimit)

print(f'{aircraft.modelName}')
print(f'{aircraft.maxSpeedSea}')
print(f'{aircraft.minSpeedSea}')
#print(f'{aircraft.zeroLiftDrag()}')
print(f'{instantTurnSpeedPressureAns}')
#print(f'{instantTurnSpeedAns}')
print(f'{instantTurnSpeedAns}')
print(f'{instantTurnRadiusAns}')
print(f'{instantTurnRateAns}')