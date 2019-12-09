def GetOpCode(instruction):
    if len(str(instruction)) > 2:
        return int(str(instruction)[-2:])
    else:
        return instruction

def GetParamMode(instruction, argIndex):
    powerOfTen = 10 ** (argIndex + 1)
    mode = int(instruction / powerOfTen) % 10
    return mode

file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day9/PuzzleInput.txt")
# file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day9/TestInput.txt")

originalIntCodes = [int(x) for x in file.readline().split(",")]
memory = list(originalIntCodes) + [0] * 100000

iPtr = 0
relativeBase = 0

while True:
    instruction = memory[iPtr]
    opCode = GetOpCode(instruction)

    if opCode == 1: #addition
        arg1 = memory[iPtr + 1]
        arg2 = memory[iPtr + 2]
        dest = memory[iPtr + 3]
        
        paramMode1 = GetParamMode(instruction, 1)
        if paramMode1 == 0: arg1 = memory[arg1]
        elif paramMode1 == 2: arg1 = memory[relativeBase + arg1]

        paramMode2 = GetParamMode(instruction, 2)
        if paramMode2 == 0: arg2 = memory[arg2]
        elif paramMode2 == 2: arg2 = memory[relativeBase + arg2]

        paramMode3 = GetParamMode(instruction, 3)
        if paramMode3 == 2: dest = relativeBase + dest

        memory[dest] = arg1 + arg2
        iPtr += 4
    elif opCode == 2: #subtraction
        arg1 = memory[iPtr + 1]
        arg2 = memory[iPtr + 2]
        dest = memory[iPtr + 3]
        
        paramMode1 = GetParamMode(instruction, 1)
        if paramMode1 == 0: arg1 = memory[arg1]
        elif paramMode1 == 2: arg1 = memory[relativeBase + arg1]

        paramMode2 = GetParamMode(instruction, 2)
        if paramMode2 == 0: arg2 = memory[arg2]
        elif paramMode2 == 2: arg2 = memory[relativeBase + arg2]

        paramMode3 = GetParamMode(instruction, 3)
        if paramMode3 == 2: dest = relativeBase + dest

        memory[dest] = arg1 * arg2
        iPtr += 4
    elif opCode == 3: #input
        dest = memory[iPtr + 1]

        paramMode2 = GetParamMode(instruction, 1)
        if paramMode2 == 2: dest = relativeBase + dest
        
        userInput = int(input("> "))
        memory[dest] = userInput
        iPtr += 2
    elif opCode == 4: #output
        arg1 = memory[iPtr + 1]

        paramMode1 = GetParamMode(instruction, 1)
        if paramMode1 == 0: arg1 = memory[arg1]
        elif paramMode1 == 2: arg1 = memory[relativeBase + arg1]
        
        print(arg1)
        iPtr += 2
    elif opCode == 5:
        arg1 = memory[iPtr + 1]

        paramMode1 = GetParamMode(instruction, 1)
        if paramMode1 == 0: arg1 = memory[arg1]
        elif paramMode1 == 2: arg1 = memory[relativeBase + arg1]

        if arg1 != 0:
            arg2 = memory[iPtr + 2]
            paramMode2 = GetParamMode(instruction, 2)
            if paramMode2 == 0: arg2 = memory[arg2]
            elif paramMode2 == 2: arg2 = memory[relativeBase + arg2]
            iPtr = arg2
        else:
            iPtr += 3
    elif opCode == 6:
        arg1 = memory[iPtr + 1]

        paramMode1 = GetParamMode(instruction, 1)
        if paramMode1 == 0: arg1 = memory[arg1]
        elif paramMode1 == 2: arg1 = memory[relativeBase + arg1]

        if arg1 == 0:
            arg2 = memory[iPtr + 2]
            paramMode2 = GetParamMode(instruction, 2)
            if paramMode2 == 0: arg2 = memory[arg2]
            elif paramMode2 == 2: arg2 = memory[relativeBase + arg2]
            iPtr = arg2
        else:
            iPtr += 3
    elif opCode == 7:
        arg1 = memory[iPtr + 1]
        arg2 = memory[iPtr + 2]
        dest = memory[iPtr + 3]
        
        paramMode1 = GetParamMode(instruction, 1)
        if paramMode1 == 0: arg1 = memory[arg1]
        elif paramMode1 == 2: arg1 = memory[relativeBase + arg1]

        paramMode2 = GetParamMode(instruction, 2)
        if paramMode2 == 0: arg2 = memory[arg2]
        elif paramMode2 == 2: arg2 = memory[relativeBase + arg2]

        paramMode3 = GetParamMode(instruction, 3)
        if paramMode3 == 2: dest = relativeBase + dest

        memory[dest] = 1 if arg1 < arg2 else 0
        iPtr += 4
    elif opCode == 8:
        arg1 = memory[iPtr + 1]
        arg2 = memory[iPtr + 2]
        dest = memory[iPtr + 3]
        
        paramMode1 = GetParamMode(instruction, 1)
        if paramMode1 == 0: arg1 = memory[arg1]
        elif paramMode1 == 2: arg1 = memory[relativeBase + arg1]

        paramMode2 = GetParamMode(instruction, 2)
        if paramMode2 == 0: arg2 = memory[arg2]
        elif paramMode2 == 2: arg2 = memory[relativeBase + arg2]

        paramMode3 = GetParamMode(instruction, 3)
        if paramMode3 == 2: dest = relativeBase + dest

        memory[dest] = 1 if arg1 == arg2 else 0
        iPtr += 4
    elif opCode == 9: #relative base
        arg1 = memory[iPtr + 1]

        paramMode1 = GetParamMode(instruction, 1)
        if paramMode1 == 0: arg1 = memory[arg1]
        elif paramMode1 == 2: arg1 = memory[relativeBase + arg1]
        
        relativeBase += arg1
        iPtr += 2
    elif opCode == 99: #termination
        break
    else:
        print("Error: Invalid OpCode.")
        break

file.close()