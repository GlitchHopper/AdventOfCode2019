file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day6/PuzzleInput")
#file = open("/Users/nathanielgugel/Desktop/AdventOfCode2019/Day6/TestInput")

class Node:
    def __init__(self, name, satelliteName):
        self.children = list()
        self.descendants = set()
        self.name = name
        self.descendants.add(satelliteName)    

    def HasDescendant(self, node):
        if node.name in self.descendants:
            return True
        else:
            return False

    def HasChild(self, node):
        for child in self.children:
            if child.name == node.name:
                return True    
        return False

    def AddChild(self, node):
        self.children.append(node)
        self.descendants.update(node.descendants)

    def AddDescendant(self, node):
        ancestor = None
        flag = False
        for child in self.children:
            if self.HasDescendant(node):
                ancestor = child
                flag = child.AddDescendant(node)
                break
        if ancestor == None:
            return True
        if flag:
            self.AddChild(node)

    def Print(self):
        print(self.name)
        
    def PrintChildren(self):
        for child in self.children:
            print(child.name)
    def PrintDescendants(self):
        for descendant in self.descendants:
            print(descendant)


# directOrbitCount = len(file.readlines())
# print(directOrbitCount)

# tree = {"A" : {"B" : {}, "C" : {}}, "B" : {"F" : {}, "E" : {}}, "D" : {"A" : {}, "X" : {}}}
# tree = {"D" : {"A" : {"B" : {"F" : {}, "E" : {}}, "C" : {}}, "X" : {}}

orbits = list()

orbitMap = list()

for line in file:
    primaryStr, satelliteStr = line.split(")")
    primary = Node(primaryStr, satelliteStr.strip("\n"))
    
    orbits.append(primary)

for orbit in orbits:
    ancestor = None
    child = None
    for path in orbitMap:
        if path.HasDescendant(orbit) or path.name == orbit.name:
            ancestor = path
        elif orbit.HasDescendant(path):
            child = path
    if child:
        orbit.AddChild(child)
        orbitMap.remove(child)
    if ancestor:
        if ancestor.name == orbit.name:
            ancestor.AddChild(Node(orbit.name, None))
        else:
            ancestor.AddDescendant(orbit)
    else:
        orbitMap.append(orbit)

orbitMap[0].Print()
print("\nChildren:")
orbitMap[0].PrintChildren()
print("\nDescendants:")
orbitMap[0].PrintDescendants()

file.close()
    
