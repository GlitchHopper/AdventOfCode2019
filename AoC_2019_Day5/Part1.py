def GetOpCode(instruction):
    if len(str(instruction)) > 2:
        return int(str(instruction)[-2:])
    else:
        return instruction

def GetParamMode(instruction, argIndex):
    powerOfTen = 10 ** (argIndex + 1)
    mode = int(instruction / powerOfTen) % 10
    return mode

file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/AoC_2019_Day5/PuzzleInput")

originalIntCodes = [int(x) for x in file.readline().split(",")]
memory = list(originalIntCodes)

iPtr = 0

while True:
    instruction = memory[iPtr]
    #print(instruction)
    opCode = GetOpCode(instruction)

    if opCode == 1: #addition
        arg1 = memory[iPtr + 1]
        arg2 = memory[iPtr + 2]
        dest = memory[iPtr + 3]
        
        if GetParamMode(instruction, 1) == 0: arg1 = memory[arg1]

        if GetParamMode(instruction, 2) == 0: arg2 = memory[arg2]

        memory[dest] = arg1 + arg2
        iPtr += 4
    elif opCode == 2: #subtraction
        arg1 = memory[iPtr + 1]
        arg2 = memory[iPtr + 2]
        dest = memory[iPtr + 3]
        
        if GetParamMode(instruction, 1) == 0: arg1 = memory[arg1]

        if GetParamMode(instruction, 2) == 0: arg2 = memory[arg2]

        memory[dest] = arg1 * arg2
        iPtr += 4
    elif opCode == 3: #input
        dest = memory[iPtr + 1]
        
        userInput = int(input("> "))
        memory[dest] = userInput
        iPtr += 2
    elif opCode == 4: #output
        arg1 = memory[iPtr + 1]

        # print(instruction)
        # userInput = input("> ")

        if GetParamMode(instruction, 1) == 0: arg1 = memory[arg1]
        
        print(arg1)
        iPtr += 2
    elif opCode == 99: #termination
        break
    else:
        print("Error: Invalid OpCode.")
        break

file.close()