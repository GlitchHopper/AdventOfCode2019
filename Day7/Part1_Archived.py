from AutomaticInput import AutomaticInput

def GetOpCode(instruction):
    if len(str(instruction)) > 2:
        return int(str(instruction)[-2:])
    else:
        return instruction

def GetParamMode(instruction, argIndex):
    powerOfTen = 10 ** (argIndex + 1)
    mode = int(instruction / powerOfTen) % 10
    return mode

# def GetInputMode():
#     while True:
#         userInput = input("Input Mode > ").lower()

#         helpSet = frozenset({"h", "help"})
#         manualSet = frozenset({"m", "manual"})
#         automaticSet = frozenset({"a", "auto", "automatic"})
#         if userInput in helpSet:
#             print("Valid inputs are: \"manual\", \"automatic\"")
#             continue
#         elif userInput in manualSet:
#             return "manual"
#         elif userInput in automaticSet:
#             return "automatic"
#         else:
#             print("Invalid input. Type \"help\" for valid input")

file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day7/PuzzleInput")

sourceProgram = tuple(int(x) for x in file.readline().split(","))
program = list(sourceProgram)

iPtr = 0

# inputMode = GetInputMode()

# autoInputStream = AutomaticInput("InputStream.txt")


while True:
    instruction = program[iPtr]
    opCode = GetOpCode(instruction)

    if opCode == 1: #addition
        arg1 = program[iPtr + 1]
        arg2 = program[iPtr + 2]
        dest = program[iPtr + 3]
        
        if GetParamMode(instruction, 1) == 0: arg1 = program[arg1]

        if GetParamMode(instruction, 2) == 0: arg2 = program[arg2]

        program[dest] = arg1 + arg2
        iPtr += 4
    elif opCode == 2: #subtraction
        arg1 = program[iPtr + 1]
        arg2 = program[iPtr + 2]
        dest = program[iPtr + 3]
        
        if GetParamMode(instruction, 1) == 0: arg1 = program[arg1]

        if GetParamMode(instruction, 2) == 0: arg2 = program[arg2]

        program[dest] = arg1 * arg2
        iPtr += 4
    elif opCode == 3: #input
        dest = program[iPtr + 1]
        userInput = ""

        if inputMode == "automatic":
            phaseSetting = autoInputStream.Next()
            outputSignal
        else: #manual
            userInput = int(input("> "))

        program[dest] = userInput
        iPtr += 2
    elif opCode == 4: #output
        arg1 = program[iPtr + 1]

        if GetParamMode(instruction, 1) == 0: arg1 = program[arg1]
        
        print(arg1)
        iPtr += 2
    elif opCode == 5: #jump-if-true
        arg1 = program[iPtr + 1]

        if GetParamMode(instruction, 1) == 0: arg1 = program[arg1]

        if arg1 != 0:
            arg2 = program[iPtr + 2]
            if GetParamMode(instruction, 2) == 0: arg2 = program[arg2]
            iPtr = arg2
        else:
            iPtr += 3
    elif opCode == 6: #jump-if-false
        arg1 = program[iPtr + 1]

        if GetParamMode(instruction, 1) == 0: arg1 = program[arg1]

        if arg1 == 0:
            arg2 = program[iPtr + 2]
            if GetParamMode(instruction, 2) == 0: arg2 = program[arg2]
            iPtr = arg2
        else:
            iPtr += 3
    elif opCode == 7: #less than
        arg1 = program[iPtr + 1]
        arg2 = program[iPtr + 2]
        dest = program[iPtr + 3]
        
        if GetParamMode(instruction, 1) == 0: arg1 = program[arg1]

        if GetParamMode(instruction, 2) == 0: arg2 = program[arg2]

        program[dest] = 1 if arg1 < arg2 else 0
        iPtr += 4
    elif opCode == 8: #equals
        arg1 = program[iPtr + 1]
        arg2 = program[iPtr + 2]
        dest = program[iPtr + 3]
        
        if GetParamMode(instruction, 1) == 0: arg1 = program[arg1]

        if GetParamMode(instruction, 2) == 0: arg2 = program[arg2]

        program[dest] = 1 if arg1 == arg2 else 0
        iPtr += 4
    elif opCode == 99: #termination
        break
    else:
        print("Error: Invalid OpCode.")
        break

file.close()