file = open("InputStream.txt", "w")



def recurse(fileRef, buildStr, nums, length):
    if length == 0:
        fileRef.write(buildStr + "\n")
        return
    for i in range(length):
        tempStr = buildStr
        buildStr += str(nums[i]) + ","
        temp = list(nums)
        nums.remove(nums[i])
        recurse(fileRef, buildStr, nums, length - 1)
        buildStr = tempStr
        nums = temp

stringName = ""

numList = [0, 1, 2, 3, 4]
numList2 = []
recurse(file, stringName, numList, 5)

file.close()