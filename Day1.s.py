import math

def GetBaseFuel(mass):
    return math.floor(int(mass) / 3) - 2

def GetAdjustedFuel(mass):
    fuelMass = GetBaseFuel(mass)
    totalAdjusted = fuelMass
    #sumStr = str(fuelMass)
    while GetBaseFuel(fuelMass) > 0:
        fuelMass = GetBaseFuel(fuelMass)
        totalAdjusted += fuelMass
        #sumStr += " + " + str(fuelMass)
    #sumStr += " = " + str(totalAdjusted)

    #print(sumStr)
    return totalAdjusted

file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day1.pi.txt", "r")

baseFuelSum = 0
adjustedFuelSum = 0

for mass in file.readlines():
    baseFuel = GetBaseFuel(mass)
    baseFuelSum += baseFuel

    adjustedFuel = GetAdjustedFuel(mass)
    adjustedFuelSum += adjustedFuel    

print("Base Fuel Sum: " + str(baseFuelSum))
print("Adjusted Fuel Sum: " + str(adjustedFuelSum))

#print("TEST: " + str(GetAdjustedFuel(100756)))

file.close