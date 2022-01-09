import numpy as np

def ShearRigidity(properties, layup):
    thickness = 0
    GA = 0
    for idx in range(int(layup[0])):
        thickness += layup[idx + 3]
    if layup[1] == 1:
        Gmajor = properties[0] / 16
        Gminor = properties[1] / (16 * 10)
        lastPly = int(layup[0] + 2)
        temp = (layup[3] / (2 * Gmajor * (layup[2]))) + ((layup[lastPly])/(2 * Gmajor * (layup[2])))
        for idx in range (1, int(layup[0]) - 1):
            if idx % 2 == 0:
                temp += layup[idx + 2] / (Gmajor * layup[2])
            else:
                temp += layup[idx + 2] / (Gminor * layup[2])
        GA = ((thickness - ((layup[3]) / 2) - ((layup[(lastPly)]) / 2)) ** 2) / (temp)
    else:
        Gmajor = properties[0] / (16 * 10)
        Gminor = properties[1] / (16)
        lastPly = int(layup[0] + 2)
        temp = (layup[3] / (2 * Gmajor * (layup[2]))) + ((layup[lastPly]) / (2 * Gmajor * (layup[2])))
        for idx in range(1, int(layup[0]) - 1):
            if idx % 2 == 0:
                temp += layup[idx + 2] / (Gmajor * layup[2])
            else:
                temp += layup[idx + 2] / (Gminor * layup[2])
        GA = ((thickness - ((layup[3]) / 2) - ((layup[(lastPly)]) / 2)) ** 2) / (temp)
    return GA
