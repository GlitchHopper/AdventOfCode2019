#Given a range of 128392-643281

def IsOrdered(numStr):
    for i in range(len(numStr) - 1):
        if numStr[i] > numStr[i+1]:
            return False
    return True

def HasDouble(numStr):
    for i in range(len(numStr) - 1):
        if numStr[i] == numStr[i+1]:
            if (i == 0 and numStr[i+1] != numStr[i+2]):
                return True
            if (i + 1 == len(numStr) - 1 and numStr[i-1] != numStr[i]):
                return True
            if (numStr[i-1] != numStr[i] and numStr[i+1] != numStr[i+2]):
                return True
    return False

min = 128392
max = 643281

passwords = []

for n in range(min, max + 1):
    numStr = str(n)
    
    if IsOrdered(numStr) and HasDouble(numStr):
        print(numStr)
        passwords.append(n)

print("The number of possible passwords is " + str(len(passwords)))
