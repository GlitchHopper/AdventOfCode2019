file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day6/PuzzleInput")

orbits = {}
count = 0

for line in file:
    primary, satellite = line.strip().split(")")
    orbits[satellite] = primary

def GetOrbitCount(orbits, satellite, primary):
    if primary in orbits:
        return 1 + GetOrbitCount(orbits, primary, orbits[primary])
    else:
        return 1
    
for satellite, primary in orbits.items():
    count += GetOrbitCount(orbits, satellite, primary)

print("The total number of direct and indirect orbits is " + str(count))

file.close()
    
