class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def Slope(self, other):
        slope = (other.y - self.y) / (other.x - self.x) if (other.x - self.x) != 0 else "inf"
        polarity =  "0"
        if other.y > self.y or (other.y == self.y and other.x > self.x):
            polarity = "+"
        else:
            polarity = "-"
        return (slope, polarity)

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

# file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day10/PuzzleInput.txt")
file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day10/TestInput.txt")

asteroidField = file.readlines()

asteroidCoord = dict()

for row in range(len(asteroidField)):
    for col in range(len(asteroidField[row])):
        if asteroidField[row][col] == "#":
            asteroidCoord[Coordinate(col, row)] = 0

for aster1 in asteroidCoord:
    sightSet = set()
    for aster2 in asteroidCoord:
        if aster1 == aster2: continue
        slope = aster1.Slope(aster2)
        if slope not in sightSet:
            sightSet.add(slope)
    asteroidCoord[aster1] = len(sightSet)

sightCounts = list(asteroidCoord.items())
sightCounts.sort(reverse = True, key = lambda e : e[1])

print("The best location is " + str(sightCounts[0][0]) + " with " + str(sightCounts[0][1]) + " other asteroids detected.")
file.close()