import sys
import numpy as np


def layupread():
    temp = 0
    num = 0
    direction = 0
    while temp == 0:
        num = input("Define the number of CLT plies. You can select either 3, 5, or 7.                        <Type "
                    "CANCEL to exit.>\nNumber of "
                    "layers:")
        if num == "CANCEL":
            sys.exit()
        num = int(num, base=8)
        if num == 3 or num == 5 or num == 7:
            temp = 1
        else:
            print("Invalid input. Try again.")
    # Importing the layup thicknesses in layup array.
    layup = np.zeros((num + 3))
    layup[0] = num
    layup[1] = direction
    layup[2] = 12
    return layup


def layupOrganizer(opt, layup, Plies):
    if opt == 1:
        for idx in range(int(layup[0])):
            if idx == 0:
                layup[idx + 3] = Plies[0]
            elif idx == int(layup[0]) - 1:
                layup[idx + 3] = Plies[0]
            elif (idx % 2) == 1:
                layup[idx + 3] = Plies[2]
            elif (idx % 2) == 0:
                layup[idx + 3] = Plies[1]
        return layup
    elif opt == 2:
        for idx in range(int(layup[0])):
            if idx == 0:
                layup[idx + 3] = Plies[0]
            elif idx == int(layup[0]) - 1:
                layup[idx + 3] = Plies[0]
            elif (idx % 2) == 1:
                layup[idx + 3] = Plies[2]
            elif (idx % 2) == 0:
                layup[idx + 3] = Plies[1]
        return layup
    elif opt == 3:
        for idx in range(int(layup[0])):
            if idx == 0:
                layup[idx + 3] = Plies[0]
            elif idx == int(layup[0]) - 1:
                layup[idx + 3] = Plies[0]
            elif (idx % 2) == 1:
                layup[idx + 3] = Plies[2]
            elif (idx % 2) == 0:
                layup[idx + 3] = Plies[0]
        return layup
