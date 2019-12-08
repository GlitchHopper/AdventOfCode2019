file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day6/PuzzleInput")

orbits = {}
count = 0

for line in file:
    primary, satellite = line.strip().split(")")
    orbits[satellite] = primary

def GetOrbitToCOM(orbits, satellite):
    
    distance = 0

    satellite = orbits[satellite] #Gets us past ourselves // prevents OBO
    path = {satellite : distance}

    while satellite in orbits:
        satellite = orbits[satellite]
        distance += 1
        path[satellite] = distance
        

    return path
    

youPath = GetOrbitToCOM(orbits, "YOU")
sanPath = GetOrbitToCOM(orbits, "SAN")

transferCount = 0

for primary in youPath:
    if primary in sanPath:
        transferCount = youPath[primary] + sanPath[primary]
        break

print("The total number of orbit transfers is " + str(transferCount))

file.close()
    
