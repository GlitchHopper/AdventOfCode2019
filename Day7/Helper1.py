file = open("InputStream.txt", "w")



def recurse(fileRef, buildStr, nums):
    if len(nums) == 0:
        fileRef.write(buildStr.rstrip(",") + "\n")
        return
    for i in range(len(nums)):
        tempStr = buildStr
        buildStr += str(nums[i]) + ","
        temp = list(nums)
        nums.remove(nums[i])
        recurse(fileRef, buildStr, nums)
        buildStr = tempStr
        nums = temp

stringName = ""

numList = [0, 1, 2, 3, 4]
numList2 = []
recurse(file, stringName, numList)

file.close()