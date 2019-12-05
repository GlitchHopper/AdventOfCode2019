#Given a range of 128392-643281

import re

min = 128392
max = 643281

passwords = []

for n in range(min, max + 1):
    numStr = str(n)
    numList1 = list(numStr)
    numList2 = numList1.copy()
    numList2.sort()
    if numList1 == numList2 and re.search(r"(\d)\1+", numStr):
        passwords.append(n)
        print(n)

print("The number of possible passwords is " + str(len(passwords)))


# test = "123536"
# testList = list(test)
# testListOriginal = testList.copy()
# testList.sort()
# print(testList)
# print(testListOriginal)
# if re.search(r"(\d)\1+", test):
#     print("YEYEYEYE")
# if testList == testListOriginal and re.search(r"(\d)\1+", test):
#     print("true")
# else:
#     print("false")