from aircraft import Aircraft, Fighter, Bomber, Attacker, Recon, Trainer


class AircraftFactory:
    def __init__(self):
        self.aircraftList = [
            #List( modelName, nickName, nation, year, length, wingSpan, wingArea, emptyWeight, maxTakeOffWeight, maxInternalfuel, thurst, minSpeedSea, maxSpeedSea, airFoil, manualStallweight, afterburner, structuralLimit)
            #Example("F-X", "Aurora", "USA", 1984, 20, 20, 20, 5000, 10000, 1300, 50, 50, 400, "Fakefoil", 7000, 25, 9)
            Fighter("ME 262", "Swallow", "Nazi Germany", 1944, 10.6, 12.6, 21.7, 8367, 15719, 2161, 17.6, 45.88, 232.5, "NACA 00011-0.825", 5090, 0, 9),
            Fighter("F-80", "Shooting Star", "USA", 1945, 10.49, 11.81, 22.07, 3819, 7646, 1317, 24.000, 49.17, 265.56, "NACA 65-213", 3628.739, 0, 6),
            Fighter("F-84", "Thunderjet", "USA", 1947, 11.61, 11.1, 24, 5033, 7646, 1362, 25.000, 70.47, 278.03, "Republic R-4", 6159.78, 0, 6),
            Fighter("F-84F", "Thunderstreak", "USA", 1954, 13.23, 10.25, 30, 5200, 12701, 1700, 32.1, 69.44, 310.67, "Republic R-4", 6803.89, 0, 6),
            Fighter("F-86", "Sabre", "USA", 1949, 11.3, 11.91, 29.12, 5046, 8234, 1288.43, 26.300, 56.58, 307.09, "NACA 0009-64", 7098.72, 0, 7),
            Fighter("F-89", "Scorpion", "USA", 1950, 16.40, 18.20, 56.30, 11428, 19160, 5215.63, 48.400, 54.53, 290.55, "NACA 0009-64", 12700.59, 15, 5),
            Fighter("F-94", "Starfire", "USA", 1950, 13.56, 12.93, 21.63, 5764, 10970, 1485.38, 28.2, 59.16, 282.92, "NACA 65-213", 5896.7, 10.7 ,8),
            Fighter("F-100", "Super Sabre", "USA", 1953, 15, 11.81, 37, 9525, 15800, 3505, 45, 83.33, 339.72, "NACA 64A007", 10886.22, 26.00, 6),
            Fighter("F-101", "Voodoo", "USA", 1957, 20.55, 12.09, 34.2, 12925, 23768, 6144, 106.6, 82.35, 286.53, "NACA 65A007", 13607.77, 43.400, 6),
            Fighter("F-102", "Delta Dagger", "USA", 1956, 20.83, 11.61, 65.6, 8777, 14288, 3199.18, 52.000, 81.72, 308.7, "NACA 0004-65", 12473.79, 24, 6),
            Fighter("F-104", "Starfighter", "USA", 1958, 16.66, 6.63, 18.22, 6350, 13166, 4918, 44.000, 90.02, 360, "Biconvex 3.36%", 6803.88, 25, 6),
            Fighter("F-105", "Thunderchief", "USA", 1958, 19.63, 10.65, 35.8, 12181, 23967, 3098.72, 64.000, 90.02, 373.87, "NACA 65A005", 13607.77, 53, 6),
            Fighter("F-106", "Delta Dart", "USA", 1959, 21.55, 11.67, 65.00, 11077.00, 15653, 4463.80, 72.000, 85.75, 329.22, "NACA 0004-65", 11793.40, 37, 6),
            Fighter("F3D", "Skyknight", "USA", 1951, 13.84, 15.24, 37.00, 6799.00, 26731.00, 3455.00, 30.00, 45.27, 236.91, "NACA 1412", 6804, 0, 5),
            Fighter("F4D", "Skyray", "USA", 1956, 13.79, 10.21, 51.70, 7268.00, 10273.00, 2045.00, 45.00, 48.87, 334.36, "NACA 0007-63/30-9.5", 7257.49, 26, 6),
            Fighter("F9F-5", "Panther", "USA", 1949, 11.84, 11.58, 23.00, 4603.00, 8492.00, 2729.71, 27.80, 44.75, 257.20, "NACA 65-212", 5216.31, 0, 6),
            Fighter("F9F-6", "Cougar", "USA", 1952, 12.47, 10.52, 28.00, 5209.00, 9072.00, 2360.00, 24.91, 51.44, 292.34, "NACA 64A010", 5443, 0, 6),
            Fighter("F2H", "Banshee", "USA", 1948, 14.68, 12.73, 27.30, 5980.00, 11437.00, 2360.00, 49.00, 50.93, 259.26, "NACA 65-212", 7108.7, 0, 6),
            Fighter("F3H", "Demon", "USA", 1956, 18.00, 10.77, 48.20, 9586.00, 15377.00, 4645.15, 43.00, 48.47, 320.00, "NACA 0006.77", 10800.94, 22.6, 6),
            Fighter("F7U", "Cutlass", "USA", 1951, 12.59, 12.10, 46.10, 8260.00, 14353.00, 4768.53, 40.00, 53.50, 311.67, "CVA 4", 10234.4, 14, 6),
            Fighter("FJ1", "Fury", "USA", 1947, 10.48, 11.63, 20.50, 4010.00, 7076.00, 3162.00, 18.00, 54.26, 236.62, "NACA 64-112", 6856, 0, 7),
            Fighter("FJ2", "Fury", "USA", 1954, 11.46, 11.32, 26.80, 5353.00, 8523.00, 2958.00, 27.00, 50.82, 300.92, "NACA 0012", 6407, 0, 7),
            Fighter("F-5E", "Tiger II", "USA", 1970, 14.68, 8.13, 17.3, 4347, 11192, 2057.95, 32,60.7, 349.86, "NACA 65A004.8", 4535.92, 12, 7.33),
            Bomber("YB-49", "Flying Wing", "USA", 1947,16.18, 52.43, 370, 40117, 87969, 44194.14, 144, 44.7, 154.22, "NACA 65-019", 88991.65, 0, 3),
            Bomber("B-45", "Tornado", "USA", 1948, 22.96, 27.13, 109.2, 20726, 41628, 9974.5, 92, 59.156, 252.57, "NACA 66–215", 36930.58, 0, 2),
            Bomber("B-47", "Stratojet", "USA", 1951, 32.64, 35.36, 132.7, 36287, 100244, 29357.6, 192, 61.73, 233.54, "NACA 64A(.225)12", 37194, 0, 2),
            Bomber("B-52", "Stratofortress", "USA", 1955, 48.5, 56.4, 370, 83250, 221323, 105189.9, 608, 54.01, 167.63, "NACA 63A219.3", 102058, 0, 2),
            Bomber("B-57", "Canaberra", "USA", 1959, 20, 19.5, 89, 12285, 24365, 6705.91, 64.2, 47.83, 266.67, "RAE/D 12% symm", 12700.59, 0, 2),
            Bomber("B-58", "Hustler", "USA", 1960, 29.51, 17.3, 143.3, 25202, 80236, 32512.14, 184, 72.02, 280.35, "NACA 0003.46", 32205.06, 84, 2),
            Bomber("B-66", "Destroyer", "USA", 1956, 22.91, 22.1, 72, 19300, 37648, 13801, 90, 51.44, 281.89, "NACA 63-009.9", 22679.62, 0, 3),
            Attacker("A-3", "Skywarrior", "USA", 1956, 23.27, 22.1, 75.4, 17876, 31795, 13525.22, 90, 51.44, 272.63, "NACA 63-009.9", 19043.62, 0, 3),
            Attacker("A-4", "Skyhawk", "USA", 1956, 12.23, 8.38, 24, 4469, 11113, 2467.54, 38, 46.76, 300.92, "NACA 0008-1.1-25", 4784.49, 0, 8),
            Attacker("A-6", "Intruder", "USA", 1963, 16.69, 16.15, 46.14, 12093, 27397, 7257.48, 82, 42.13, 288.06, "NACA 64A009", 11855.09, 0, 6),
            Attacker("A-7", "Corsair", "USA", 1967, 14.06, 11.8, 34.83, 8676, 19050, 6616.1, 66.7, 74.59, 308.64, "NACA 65A007", 13607.77, 0, 6),
            Attacker("A-10", "Thunderbolt II", "USA", 1977, 16.26, 17.53, 47, 11321, 20865, 4990, 80.64, 61.73, 195.99, "NACA 6716", 14000, 0, 6),
            Attacker("A-37", "Dragonfly", "USA", 1967, 8.62, 10.94, 17.08, 2817, 6350, 1540.81, 25.4, 42.7, 213.48, "NACA 2418", 2721.55, 0, 8),
            Recon("SR-71", "Blackbird", "USA", 1966, 32.74, 16.94, 170, 30617, 78018, 33228.87, 160.14, 85.94, 222.95, "Hexagonal", 45359.24, 68.72, 2),
            Recon("U-2", "Dragon Lady", "USA", 1956, 15.15, 24.38, 55.74, 6291.33, 9380.29, 3939.45, 75.62, 39.09, 113.17, "NACA 63A-409", 6350.29, 0, 3),
         ]

    def getModelName(self, modelName):
        for aircraft in self.aircraftList:
            if aircraft.modelName == modelName:
                return aircraft
        return None

    def getNickName(self, nickName):
        for aircraft in self.aircraftList:
            if aircraft.nickName == nickName:
                return aircraft
        return None

    def getLightestMTOW(self):
        lightest = None
        for aircraft in self.aircraftList:
            if lightest == None or aircraft.maxTakeOffWeight < lightest.maxTakeOffWeight:
                lightest = aircraft
        return lightest

    def getHeaviestMTOW(self):
        heaviest = None
        for aircraft in self.aircraftList:
            if heaviest == None or aircraft.maxTakeOffWeight > heaviest.maxTakeOffWeight:
                heaviest = aircraft
        return heaviest

    def getFastedMaxSpeed(self):
        fastest = None
        for aircraft in self.aircraftList:
            if fastest == None or aircraft.maxSpeedSea > fastest.maxSpeedSea:
                fastest = aircraft
        return fastest

    def getBestUsefulLoad(self):
        BestUsefulLoad = None
        for aircraft in self.aircraftList:
            if BestUsefulLoad == None or (aircraft.maxTakeOffWeight - aircraft.emptyWeight  - aircraft.maxInternalfuel) > (aircraft.maxTakeOffWeight - aircraft.emptyWeight - aircraft.maxInternalfuel):
                BestUsefulLoad = aircraft
        return BestUsefulLoad

    def getSlowestMaxSpeed(self):
        slowest = None
        for aircraft in self.aircraftList:
            if slowest == None or aircraft.maxSpeedSea < slowest.maxSpeedSea:
                slowest = aircraft
        return slowest

    def getOldestIntroDate(self):
        oldest = None
        for aircraft in self.aircraftList:
            if oldest == None or aircraft.year < oldest.year:
                oldest = aircraft
        return oldest

    def getNewestIntroDate(self):
        newest = None
        for aircraft in self.aircraftList:
            if newest == None or aircraft.year > newest.year:
                newest = aircraft
        return newest

    def getBestEnergy(self):
        bestEnergy = None
        for aircraft in self.aircraftList:
               if bestEnergy == None or aircraft.energyManeuverability() > bestEnergy.energyManeuverability():
                   bestEnergy = aircraft
        return bestEnergy

    def getWorstEnergy(self):
        worstEnergy = None
        for aircraft in self.aircraftList:
               if worstEnergy == None or aircraft.energyManeuverability() < worstEnergy.energyManeuverability():
                   worstEnergy = aircraft
        return worstEnergy
    
    def printAircraftList(self):
        print(f'Model Name: {aircraft.modelName} | Nickname: {aircraft.nickName} | Nation of origin: {aircraft.nation} | Introduction year: {aircraft.list}')

    def printAircraft(self, aircraft):
        print(f'Model Name: {aircraft.modelName} | Nickname: {aircraft.nickName} | Nation of origin: {aircraft.nation} | Introduction year: {aircraft.year}  | Airfoil:{aircraft.airFoil}')
        print(f'Length:{aircraft.length}m | Wingspan:{aircraft.wingSpan}m | Wing Area:{aircraft.wingArea}sq m | Aspect Ratio:{round(aircraft.aspectRatio(),2)} | Wing Load:{round(aircraft.maxTakeOffWeight / aircraft.wingArea,2)}kg/sq m')
        print(f'Empty Weight:{aircraft.emptyWeight}kg | Max Take-Off Weight:{aircraft.maxTakeOffWeight}kg | Total Internal Fuel Weight:{aircraft.maxInternalfuel}kg | Useful Load:{round(aircraft.maxTakeOffWeight - aircraft.maxInternalfuel,2)}kg')
        print(f'Dry Thrust:{aircraft.thrust}kN | Afterburner/Wet Thrust:{aircraft.afterburner}kN | Total Thrust:{round(aircraft.thrust + aircraft.afterburner,2)}kN') 
        print(f'Stall Speed:{aircraft.minSpeedSea}m/s | Max Speed at Sea Level:{aircraft.maxSpeedSea}m/s | Energy-Manueverability(Boyd Theory):{round(aircraft.energyManeuverability(),2)} Ps')
        print(f'Max Lift:{round(aircraft.maxLift(),2)} | Zero Lift:{round(aircraft.zeroLift(),2)} | Max Drag at Sea Level:{round(aircraft.maxDragSea(),2)} | Zero Lift Drag:{round(aircraft.zeroLiftDrag(),2)}')

    def printAicraftListIndex(self):
        for idx, aircraft in enumerate(self.aircraftList):
            print(f'{idx} | Model Name: {aircraft.modelName} | Nickname: {aircraft.nickName}')

    def getIndexedAircraft(self, idx):
        if idx >= len(self.aircraftList) or idx < 0:
            return None
        return self.aircraftList[idx]



        
