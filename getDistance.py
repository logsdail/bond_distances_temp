import re
import numpy as np

#File Input
file = input("AIMS output file to analyse bonds (aims.out by default): ") or "aims.out"

#Unit cell
cell = []
startPattern = '  Input geometry:\n'

with open(file) as f:
    match = False
    l = 0

    for line in f:
        if re.match(startPattern, line):
            match = True
            continue
        elif l > 3:
            match = False
            continue
        elif match:
            if l > 0:
                cell.append(line.split('      '))
            l = l + 1

cell = [float(cell[0][1]), float(cell[1][2]), float(cell[2][3])]

#Atomic Positions
atomsList = []
startPattern = '  Input geometry:\n'
endPattern = '\n'

with open(file) as f:
    match = False
    l = 0

    for line in f:
        if re.match(startPattern, line):
            match = True
            continue
        elif re.match(endPattern, line):
            match = False
            continue
        elif match:
            if l > 5:
                atomsList.append(line.split('       '))
            l = l + 1

#Clean up atomic positions
for i in range(len(atomsList)):
    atomsList[i][0] = atomsList[i][0].replace('|', '')
    atomsList[i][0] = atomsList[i][0].split(':')

#Dictionary of atoms
atomsDict = { i+1 : [float(atomsList[i][1]), float(atomsList[i][2]), float(atomsList[i][3])] for i in range(0,len(atomsList))}

#Repeated input of two atomic distances
endFlag = False

while endFlag == False:
    #Atoms Input
    print("Note: ASE atom index = aims.out index - 1")
    atom1Index, atom2Index = input("ASE atoms indices in the form 'atom1,atom2': ").split(',')

    atom1Index = int(atom1Index)
    atom2Index = int(atom2Index)

    #ASE atom index = Geometry file index - 1 bcs ASE starts at 0
    atom1 = atomsDict[atom1Index+1]
    atom2 = atomsDict[atom2Index+1]

    vector = []
    for i in range(0, 3):
        vector.append(atom1[i] - atom2[i])
        if vector[i] > cell[i]/2:
            vector[i] = cell[i] - vector[i]

    print(vector)
    distance = np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    print(distance)

    ui = input('Get another distance? [y/n] ')
    endFlag = True if ui.lower() == 'n' else False

print("Goodbye!")
