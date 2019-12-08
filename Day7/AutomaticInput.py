class AutomaticInput():
    def __init__(self, fileName):
        self.fileName = fileName

        file = open(self. fileName)

        sequences = list()
        for line in file:
            sequences.append(line.split(","))