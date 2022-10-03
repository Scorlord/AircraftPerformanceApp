import math
from pickle import APPEND
from types import DynamicClassAttribute


class Aircraft:

    def __init__(self, modelName, nickName, nation, year, length, wingSpan, wingArea, emptyWeight, maxTakeOffWeight, maxInternalfuel, thurst, minSpeedSea, maxSpeedSea, airFoil, 
    manualStallweight, afterburner, structuralLimit):
        self.modelName = modelName ## Model of Aircraft, such as F-16, Mig-21, etc
        self.nickName = nickName ## Nickname of Aircraft, such as Flacon, Fishbed, etc
        self.nation = nation ## Nation Origin of Aircraft
        self.year =  year ## Introduction year of Aircraft
        self.length = length ## Legnth of aircraft in meters
        self.wingSpan = wingSpan ## Wingspan of aircraft in meters
        self.wingArea = wingArea ## Wing area or surface area of wing, in square meters
        self.emptyWeight = emptyWeight ##Dry or empty weight of the aircraft in kilograms
        self.maxTakeOffWeight = maxTakeOffWeight ## Max weight in order to take off
        self.maxInternalfuel = maxInternalfuel ## Max internal fuel is kilograms. Standard jet fuel is approx 0.8 kg per Liter
        self.thrust = thurst ## Max Thrust without afterburner. Does not allow piston aircraft yet
        self.minSpeedSea = minSpeedSea ## Minium speed at seal leve in meters per second (stall speed)
        self.maxSpeedSea = maxSpeedSea ## Max speed at sea level in meters per second
        self.airFoil = airFoil ## Airfoil used by aircraft
        self.manualStallWeight = manualStallweight ## Listed stall weight from manual
        self.afterburner = afterburner ## if airframe has an afterbuner add the difference here i.e 44 normal thrust 69 thrust with afterbuner is 69-44=25
        self.structuralLimit = structuralLimit ## Max structural limit for airframe or "g" rating
        ##self.performanceWeight = performanceWeight ## Set weight of aircraft in kilograms
        ##self.performanceSpeed = performanceSpeed ## Set speed of aicraft in meters per second
   

    def stallDynamicPressure(self): ## needed to find max lift(maxCL) of aircraft
        return 1.225 * (self.minSpeedSea ** 2) * 0.5

    def maxLift(self): ## max lift is used for most equations
        return (self.manualStallWeight * 9.81) / (self.stallDynamicPressure() * self.wingArea) 

    def maxDragSea(self):
        return ( ( ((self.thrust + self.afterburner)) / (0.5 * 1.225 * self.maxSpeedSea * self.wingArea) ) * 1000)

    def aspectRatio(self):
        return ( (self.wingSpan **2) / self.wingArea )

    def zeroLift(self):
        return ((self.maxTakeOffWeight * .8) / (.5 * 1.225 * self.maxSpeedSea**2 * self.wingArea)) * 10

    def inducedDrag(self):
        return  (( (self.zeroLift() **2) / (math.pi * self.aspectRatio()) ) *10)

    def zeroLiftDrag(self):
        return (self.maxDragSea() - self.inducedDrag())

    def performanceWeight(self):
        return 0


    ##def maxLiftDrag(self):

    #def turnDynamicPressure(self):
     #  return (self.performanceWeight / self.wingArea) * math.sqrt(self.inducedDrag / self.zeroLiftdrag)

    ## def instantTurnRadius(self): ## Instant turn radius, typically not equal to substained radius
        ##return ( self.performanceWeight / (0.5 * 1.225 * self.wingArea * self.maxLift ) ) * (self.structuralLimit / math.sqrt((self.structuralLimit **2) - 1))

    
    ## def instantTurnRate(self): ## Instant turn rate, typically not equal to substained rate
          ##return ( ( (9.80665 * (math.sqrt( (0.5 * 1.225 * self.wingArea * self.maxLift) / self.performanceWeight)) * (self.structuralLimit / math.sqrt((self.structuralLimit **2) - 1)) ) * 180 ) / math.pi)


class Fighter(Aircraft):
    pass

class Attacker(Aircraft):
    pass

class Bomber(Aircraft):
    pass

class Trainer(Aircraft):
    pass
