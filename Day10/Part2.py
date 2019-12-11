import math
import time

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(x ** 2 + y ** 2)
        #angle undergoes a transformation to make 0 positive y and rotation clockwise
        test = ((math.degrees(math.acos(self.x / self.magnitude) if self.y < 0 else - math.acos(self.x / self.magnitude)) * 1) + 450) % 360
        # test = math.degrees(math.acos(self.x / self.magnitude) if self.y >= 0 else - math.acos(self.x / self.magnitude))
        self.angle = test

    def __add__(self, other):
        return Vector(self.x + other.x, other.y - self.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, other.y - self.y) 

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ") Angle: " + str(self.angle) + " Mag: " + str(self.magnitude)

file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day10/PuzzleInput.txt")
# file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day10/TestInput.txt")

laser = Vector(23, 19)
# laser = Vector(11, 13)

destroyCount = 200

asteroidField = file.readlines()

asteroidList = list()

debugArray = list(asteroidField)
def UpdateOutput(destructionPoint):
    outputFile = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day10/TestOutput.txt", "w+")

    x = destructionPoint.x
    y = destructionPoint.y
    changeLine = list(debugArray[y])
    changeLine[x] = "*"
    newStr = "".join(changeLine)

    debugArray[y] = newStr
    for line in debugArray:
        outputFile.write(line)

    outputFile.close()
    # yieldInput = input()
    time.sleep(.1)

for row in range(len(asteroidField)):
    for col in range(len(asteroidField[row])):
        if asteroidField[row][col] == "#" and not (col == laser.x and row == laser.y):
            asteroidList.append(Vector(col, row) - laser)

angleDict = dict()

for asteroid in asteroidList:
    angle = asteroid.angle
    if angle not in angleDict:
        angleDict[angle] = list()
    angleDict[angle].append(asteroid)

for asterList in angleDict.values():
    asterList.sort(key = lambda e : e.magnitude)

angleList = list(angleDict.keys())
angleList.sort()

asteroidtoAngleList = list()

for angle in angleList:
    asteroidtoAngleList.append(angleDict[angle])

targetAsteroid = None

destructionIndex = 0

while destructionIndex < destroyCount:
    for asterList in asteroidtoAngleList:
        targetAsteroid = asterList[0]
        UpdateOutput(targetAsteroid + laser)
        # print(str(destructionIndex + 1) + ". " +  str(targetAsteroid + laser))
        asterList.remove(asterList[0])
        destructionIndex += 1
        if destructionIndex == destroyCount:
            break
    for i in range(len(asteroidtoAngleList), 1, -1):
        asterList = asteroidtoAngleList[i-1]
        if len(asterList) <= 0:
            asteroidtoAngleList.remove(asterList)
        
targetAsteroid += laser

answer = (targetAsteroid.x) * 100 + (targetAsteroid.y)

print("The " + str(destroyCount) + "th asteroid to be destroyed is located at " + str(targetAsteroid) + " with a result of " + str(answer))

file.close()