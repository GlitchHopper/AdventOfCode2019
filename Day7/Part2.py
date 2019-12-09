def GetOpCode(instruction):
    if len(str(instruction)) > 2:
        return int(str(instruction)[-2:])
    else:
        return instruction

def GetParamMode(instruction, argIndex):
    powerOfTen = 10 ** (argIndex + 1)
    mode = int(instruction / powerOfTen) % 10
    return mode

file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day7/PuzzleInput")

sourceProgram = tuple(int(x) for x in file.readline().split(","))
program = list(sourceProgram)

testInput = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/InputStream2.txt")

inputStream = []

for line in testInput:
    inputStream.append([int(x) for x in line.strip("\n").split(",")])



amplifierCount = 5

amplifiers = []

isInitializing = True

for i in range(5):
    amplifiers.append(list(sourceProgram))

signalStrengths = []


for test in inputStream:
    signal = 0
    amplifiers.clear()
    for i in range(5):
        amplifiers.append(list([list(sourceProgram), 0]))
    # iPtr = 0
    # i = 0
    amplifierPointer = 0
    inputState = "phase_setting"
    # for i in range(amplifierCount):
    #     inputState = "phase_setting"
    while True:
        currentAmplifier = amplifierPointer
        program = amplifiers[currentAmplifier][0]
        iPtr = amplifiers[currentAmplifier][1]
        
        instruction =  program[iPtr]
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
            if len(test) > 0:
                userInput = test[0]
                test.remove(test[0])
                amplifierPointer = (amplifierPointer + 1) % amplifierCount
            else:
                userInput = signal

            program[dest] = userInput
            iPtr += 2
        elif opCode == 4: #output
            arg1 = program[iPtr + 1]

            if GetParamMode(instruction, 1) == 0: arg1 = program[arg1]
            signal = arg1
            amplifierPointer = (amplifierPointer + 1) % amplifierCount
            # print(arg1)
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
            if amplifierPointer == 0:
                signalStrengths.append(signal)
                break
        else:
            print("Error: Invalid OpCode.")
            break
        amplifiers[currentAmplifier][0] = program
        amplifiers[currentAmplifier][1] = iPtr
        
    

signalStrengths.sort(reverse = True)
print("The strongest possible signal is " + str(signalStrengths[0]))

file.close()