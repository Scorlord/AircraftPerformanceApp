from aircraft import Aircraft, Fighter, Bomber, Attacker


class AircraftFactory:
    def __init__(self):
        self.aircraftList = [
            Fighter("F-80", "Shooting Star", "USA", 1945, 10.49, 11.81, 22.07, 3819, 7646, 1317, 24.000, 49.17, 265.56, "NACA 65-213", 3628.739, 0, 6),
            Fighter("F-84", "Thunderjet", "USA", 1947, 11.61, 11.1, 24, 5033, 7646, 1362, 25.000, 70.47, 278.03, "Republic R-4", 6159.78, 0, 6),
            Fighter("F-84F", "Thunderstreak", "USA", 1954, 13.23, 10.25, 4.39, 5200, 12.701, 1700, 3210, 69.44, 310.67, "Republic R-4", 6803.89, 0, 6),
            Fighter("F-86", "Sabre", "USA", 1949, 11.3, 11.91, 29.12, 5046, 8234, 1288.43, 26.300, 56.58, 307.09, "NACA 0009-64", 7098.72, 0, 7),
            Fighter("F-89", "Scorpion", "USA", 1950, 16.40, 18.20, 56.30, 11428, 19160, 5215.63, 48.400, 54.53, 290.55, "NACA 0009-64", 12700.59, 153600, 5),
            Fighter("F-100", "Super Sabre", "USA", 1953, 15, 11.81, 37, 9525, 15800, 3505, 45.000, 163, 339.72, "NACA 64A007", 10886.22, 263000, 6),
            Fighter("F-101", "Voodoo", "USA", 1957, 20.55, 12.09, 5.49, 12925, 23768, 6144, 106.600, 160, 286.53, "NACA 65A007", 13607.77, 43400, 6),
            Fighter("F-102", "Delta Dagger", "USA", 1956, 20.83, 11.61, 65.6, 8777, 14288, 3199.18, 52.000, 81.72, 308.7, "NACA 0004-65", 12473.79, 243000, 6),
            Fighter("F-104", "Starfighter", "USA", 1958, 16.66, 6.63, 18.22, 6350, 13166, 4918, 44.000, 90.02, 360, "Biconvex 3.36%", 25, 25000, 6),
            Fighter("F-105", "Thunderchief", "USA", 1958, 19.63, 10.65, 35.8, 12181, 23967, 3098.72, 64.000, 90.02, 373.87, "NACA 65A005", 13607.77, 533880, 6),
            Fighter("F-106", "Delta Dart", "USA", 1959, 21.55, 11.67, 65.00, 11077.00, 15653, 4463.80, 72.000, 85.75, 329.22, "NACA 0004-65", 11793.40, 373000, 6),
            Fighter("F3D", "Skyknight", "USA", 1951, 13.84, 15.24, 37.00, 6799.00, 26731.00, 3455.00, 30.00, 45.27, 236.91, "NACA 1412", 6804, 0, 5),
            Fighter("F4D", "Skyray", "USA", 1956, 13.79, 10.21, 51.70, 7268.00, 10273.00, 2045.00, 45.00, 48.87, 334.36, "NACA 0007-63/30-9.5", 7257.49, 26, 6),
            Fighter("F9F-5", "Panther", "USA", 1949, 11.84, 11.58, 23.00, 4603.00, 8492.00, 2729.71, 27.80, 44.75, 257.20, "NACA 65-212", 5216.31, 0, 6),
            Fighter("F9F-6", "Cougar", "USA", 1952, 12.47, 10.52, 28.00, 5209.00, 9072.00, 2360.00, 24.91, 51.44, 292.34, "NACA 64A010", 5443, 0, 6),
            Fighter("F2H", "Banshee", "USA", 1948, 14.68, 12.73, 27.30, 5980.00, 11437.00, 2360.00, 49.00, 50.93, 259.26, "NACA 65-212", 7108.7, 0, 6),
            Fighter("F3H", "Demon", "USA", 1956, 18.00, 10.77, 48.20, 9586.00, 15377.00, 4645.15, 43.00, 48.47, 1152.00, "NACA 0006.77", 10800.94, 22.6, 6),
            Fighter("F7U", "Cutlass", "USA", 1951, 12.59, 12.10, 46.10, 8260.00, 14353.00, 4768.53, 40.00, 53.50, 1122.00, "CVA 4", 10234.4, 14, 6),
            Fighter("FJ1", "Fury", "USA", 1947, 10.48, 11.63, 20.50, 4010.00, 7076.00, 3162.00, 18.00, 54.26, 236.62, "NACA 64-112", 6856, 0, 7),
            Fighter("FJ2", "Fury", "USA", 1954, 11.46, 11.32, 26.80, 5353.00, 8523.00, 2958.00, 27.00, 50.82, 300.92, "NACA 0012", 6407, 0, 7),
            Bomber("B-45", "Tornado", "USA", 1948, 22.96, 27.13, 109.2, 20726, 41628, 9974.5, 92, 59.156, 252.57, "NACA 66–215", 36930.58, 0, 2),
            Bomber("B-47", "Stratojet", "USA", 1951, 32.64, 35.36, 132.7, 36287, 100244, 29357.6, 192, 61.73, 233.54, "NACA 64A(.225)12", 37194, 0, 2),
            Bomber("B-52", "Stratofortress", "USA", 1955, 48.5, 56.4, 370, 83250, 221323, 105189.9, 608, 54.01, 167.63, "NACA 63A219.3", 102058, 0, 2),
            Bomber("B-57", "Canaberra", "USA", 1959, 20, 19.5, 89, 12285, 24365, 6705.91, 64.2, 47.83, 266.67, "RAE/D 12% symm", 12700.59, 0, 2),
            Bomber("B-58", "Hustler", "USA", 1960, 29.51, 17.3, 143.3, 25202, 80236, 32512.14, 184, 72.02, 280.35, "NACA 0003.46", 32205.06, 84, 2),
            Bomber("B-66", "Destroyer", "USA", 1956, 22.91, 22.1, 72, 19300, 37648, 13801, 90, 51.44, 281.89, "NACA 63-009.9", 22679.62, 0, 3),
            Attacker("A-3", "Skywarrior", "USA", 1956, 23.27, 22.1, 75.4, 17876, 31795, 13525.22, 90, 51.44, 272.63, "NACA 63-009.9", 19043.62, 0, 3),
            Attacker("A-4", "Skyhawk", "USA", 1956, 12.23, 8.38, 24, 4469, 11113, 2467.54, 38, 46.76, 300.92, "NACA 0008-1.1-25", 4784.49, 0, 8),
            Attacker("A-6", "Intruder", "USA", 1963, 16.69, 16.15, 46.14, 12093, 27397, 7257.48, 82, 42.13, 288.06, "NACA 64A009", 11855.09, 0, 6),
            Attacker("A-7", "Corsair", "USA", 1967, 14.06, 11.8, 34.83, 8676, 19050, 6616.1, 66.7, 74.59, 308.64, "NACA 65A007", 13607.77, 0, 6)
         ]

    def getModelName(self, modelName):
        for aircraft in self.aircraftList:
            if aircraft.modelName == modelName:
                return aircraft
        return None

    def getNickName(self, nickName):
        for aircraft in self.aircraftList:
            if aircraft.nickName == nickName:
                return aircraft.nickName
        return None

    def getLightestMTOW(self):
        lightest = None
        for aircraft in self.aircraftList:
            if lightest == None or aircraft.maxTakeOffWeight < lightest.maxTakeOffWeight:
                lightest = aircraft
        return None

    def getHeaviestMTOW(self):
        heaviest = None
        for aircraft in self.aircraftList:
            if heaviest == None or aircraft.maxTakeOffWeight > heaviest.maxTakeOffWeight:
                heaviest = aircraft
        return None

    def getFastedMaxSpeed(self):
        fastest = None
        for aircraft in self.aircraftList:
            if fastest == None or aircraft.maxSpeedSea > fastest.maxSpeedSea:
                fastest = aircraft
        return None

    def getBestUsefulLoad(self):
        BestUsefulLoad = None
        for aircraft in self.aircraftList:
            if BestUsefulLoad == None or (aircraft.maxTakeOffWeight - aircraft.emptyWeight  - aircraft.maxInternalfuel) > (aircraft.maxTakeOffWeight - aircraft.emptyWeight - aircraft.maxInternalfuel):
                BestUsefulLoad = aircraft
        return None

