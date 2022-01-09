import sys
import BendingStiffness


def BendingMoment(properties, layup):
    thickness = 0
    innerLayer = layup[3] + layup[int(layup[0]) + 2]
    FS = 0
    for idx in range(int(layup[0])):
        thickness += layup[idx + 3]
    EI = BendingStiffness.BendingStiffness(properties, layup)
    if layup[1] == 1:
        FS = (((EI * 2) / (properties[0] * thickness)) * ((0.85 * properties[2]) / 12))
    if layup[1] == 2:
        if properties[3] == 0:
            print("Fb.minor ASDreference (psi) is not inserted in the inputdata.csv")
            sys.exit()
        FS = ((EI * 2) / (properties[1] * (thickness - innerLayer))) * ((properties[3]) / 12)
    return FS
