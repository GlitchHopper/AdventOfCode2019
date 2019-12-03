file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/AoC_2019_Day2_PuzzleInput.txt", "r")

intCodes = [int(x) for x in file.readline().split(",")]

intCodes[1] = 12
intCodes[2] = 2

for index in range(0, len(intCodes), 4):

    opCode = int(intCodes[index])
    a = int(intCodes[index + 1])
    b = int(intCodes[index + 2])
    destination = int(intCodes[index + 3])

    if opCode == 1:
        intCodes[destination] = intCodes[a] + intCodes[b]
    elif opCode == 2:
        intCodes[destination] = intCodes[a] * intCodes[b]
    elif opCode == 99:
        print("The value final value at index 0 is " + str(intCodes[0]))
        break
    else:
        print("Error: Invalid OpCode.")
        break

file.close()