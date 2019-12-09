file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day8/PuzzleInput.txt")

width = 25
height = 6
area = width * height

layers = list()


pictureData = file.read()

for layerIndex in range(int(len(pictureData) / area)):
    layers.append(dict())
    frequencyDict = layers[layerIndex]
    for pixel in pictureData[layerIndex * area:(layerIndex + 1) * area]:
        if pixel not in frequencyDict:
            frequencyDict[pixel] = 1
        else:
            frequencyDict[pixel] += 1

layers.sort(key = lambda x : x["0"])
leastZerosLayer = layers[0]

product = leastZerosLayer["1"] * leastZerosLayer["2"]

print("The number of 1s multiplied by the number of 2s on the layer with the least 0s is " + str(product))

file.close()