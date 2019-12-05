import math

def GetLeg(position, node, posToDistance, cableIndex, distance):
    direction = node[0]
    legDistance = int(node[1:])
    for i in range(legDistance):
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
            break
        distance += 1
        if tuple(position) not in posToDistance:
            posToDistance[tuple(position)] = {}
        if cableIndex not in posToDistance[tuple(position)]:
            posToDistance[tuple(position)][cableIndex] = distance
    return distance

file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/AoC_2019_Day3/PuzzleInput.txt")

cables = []
for line in file:
    cables.append(line.split(","))

posToDistance = {}

for cableIndex in range(len(cables)):
    position = [0, 0]
    distance = 0
    for node in cables[cableIndex]:
        distance = GetLeg(position, node, posToDistance, cableIndex, distance)

intersectionDistances = []

for position in posToDistance:
    distances = posToDistance[position]
    if len(distances) > 1:
        intersectionDistances.append(sum(distances.values()))

intersectionDistances.sort()
print("The shortest signal distance is " + str(intersectionDistances[0]))