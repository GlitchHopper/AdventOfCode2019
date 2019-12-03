file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/AoC_2019_Day2/AoC_2019_Day2_PuzzleInput.txt", "r")

originalIntCodes = [int(x) for x in file.readline().split(",")]
intCodes = list(originalIntCodes)

for i in range(100):
    for j in range(100):
        intCodes = list(originalIntCodes)
        intCodes[1] = i
        intCodes[2] = j
        for index in range(0, len(intCodes), 4):

            opCode = int(intCodes[index])
            noun = int(intCodes[index + 1])
            verb = int(intCodes[index + 2])
            destination = int(intCodes[index + 3])

            if opCode == 1:
                intCodes[destination] = intCodes[noun] + intCodes[verb]
            elif opCode == 2:
                intCodes[destination] = intCodes[noun] * intCodes[verb]
            elif opCode == 99:
                if intCodes[0] == 19690720:
                    print("The input that produces 19690720 is:")
                    print("\tNoun - " + str(i))
                    print("\tVerb - " + str(j))
                    print("\tInput - " + str(100 * i + j))
                break
            else:
                print("Error: Invalid OpCode.")
                break

file.close()