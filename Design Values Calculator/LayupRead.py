import sys
import numpy as np

def layupread():
    temp = 0
    num = 0
    length = 0
    direction = 0
    MAJOR = 0
    MAJOR2 = 0
    minor = 0
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
    """temp = 0
    while temp == 0:
        direction = input("\nSpecify CLT design orientation:\n1.Major direction\n2.Minor direction\nSelect:")
        direction = int(direction)
        if direction == 1 or direction == 2:
            temp = 1
        else:
            print("\nInvalid input. Try again.")"""
    temp = 0
    while temp == 0:
        length = input("Specify CLT design width (in./ft of width) regarding PRG-320:")
        length = float(length)
        if 1000 >= length >= 1:
            temp = 1
        else:
            print("Invalid input. The value should be above 1in and less than 1000in. Try again.")
    temp = 0
    while temp == 0:
        MAJOR = input("The CLT panel is assumed to be symmetric. Thickness (in) of the out most layer:                 "
                      "<Type CANCEL to exit.>\nThickness:")
        if MAJOR == "CANCEL":
            sys.exit()
        MAJOR = float(MAJOR)
        if 5 >= MAJOR >= 0.5:
            temp += 1
        else:
            print("##ERROR## The thickness should be less than 5in and more than 0.5in. Try again.")
    temp = 0
    while temp == 0 and num != 3:
        MAJOR2 = input("Thickness (in) of the inner plies parallel to the out most layer:                              "
                      "<Type CANCEL to exit.>\nThickness:")
        if MAJOR2 == "CANCEL":
            sys.exit()
        MAJOR2 = float(MAJOR2)
        if 5 >= MAJOR2 >= 0.5:
            temp += 1
        else:
            print("##ERROR## The thickness should be less than 5in and more than 0.5in. Try again.")
    temp = 0
    while temp == 0:
        minor = input("Thickness (in) of the inner plies perpendicular to the out most layer:                          "
                      "<Type CANCEL to exit.>\nThickness:")
        if minor == "CANCEL":
            sys.exit()
        minor = float(minor)
        if 5 >= minor >= 0.5:
            temp += 1
        else:
            print("##ERROR## The thickness should be less than 5in and more than 0.5in. Try again.")
    #Importing the layup thicknesses in layup array.
    layup = np.zeros((num+3))
    layup[0] = num
    layup[1] = 1
    layup[2] = length
    for idx in range(num):
        if idx == 0:
            layup[idx+3] = MAJOR
        elif idx == num-1:
            layup[idx+3] = MAJOR
        elif (idx%2) == 1:
            layup[idx + 3] = minor
        elif (idx%2) == 0:
            layup[idx + 3] = MAJOR2
    return layup