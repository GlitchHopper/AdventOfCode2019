class Layer:
    def __init__(self, index, width, height):
        self.index = index
        self.width = width
        self.height = height
        self.matrix = [["2"] * width for i in range(height)]
    
    def PopulateLayer(self, sequence):
        index = 0
        for row in range(self.height):
            for col in range(self.width):
                self.matrix[row][col] = sequence[index]
                index += 1

    def GetWidth(self):
        return self.width

    def __repr__(self):
        imageStr = ""
        for row in range(self.height):
            for elem in self.matrix[row]:
                if elem == "0":
                    elem = " "
                elif elem == "1":
                    elem = "█"
                imageStr += elem
            imageStr += "\n"
        return imageStr      

    @staticmethod
    def Union(*layers):
        layers = list(layers)
        layers.sort(key = lambda e : e.index)
        width = layers[0].GetWidth()
        height = layers[0].height

        unionLayer = Layer(-1, width, height)

        for i in range(len(layers)):
            currentLayer = layers[i]
            for row in range(height):
                for col in range(width):
                    if unionLayer.matrix[row][col] == "2":
                        unionLayer.matrix[row][col] = currentLayer.matrix[row][col]
        
        return unionLayer

file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day8/PuzzleInput.txt")

imageData = file.read()

file.close()

width = 25
height = 6
area = width * height

layers = list()

for layerIndex in range(int(len(imageData) / area)):
    sequence = imageData[layerIndex * area:(layerIndex + 1) * area]

    layer = Layer(layerIndex, width, height)
    layer.PopulateLayer(sequence)
    layers.append(layer)

image = Layer.Union(*layers)

print(image)
