import math

def GetLeg(path, position, instruction):
    direction = instruction[0]
    distance = int(instruction[1:])
    for i in range(distance):
        if direction == "L":
            position[0] -= 1
        elif direction == "R":
            position[0] += 1
        elif direction == "D":
            position[1] -= 1
        elif direction == "U":
            position[1] += 1
        else:
            print("Invalid Leg Instruction")
        path.add(tuple(position))

file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/AoC_2019_Day3/PuzzleInput.txt")

cables = []
for line in file:
    cables.append(line.split(","))

cablePaths = []

for cable in cables:
    position = [0, 0]
    path = set()
    for node in cable:
        GetLeg(path, position, node)
    cablePaths.append(path)

cableIntersections = list(set.intersection(cablePaths[0], cablePaths[1]))
distances = []

for intersection in cableIntersections:
    distances.append(abs(intersection[0]) + abs(intersection[1]))

distances.sort()
print("Shortest Manhattan distances is " + str(distances[0]))