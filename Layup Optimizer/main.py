import sys
import CSVread, LayupRead, PropertyCalc
import optimizer

properties = CSVread.CSVread('inputdata.csv')
goal = CSVread.CSVread('goal.csv')
# Applying adjust factor suggested by PRG 320 and CLT handbook page 16 chapter 3.
layup = LayupRead.layupread()
# Iteration step in (in).
Diff = 0.125
# Starting layup. The values are Major, Major2, and minor directions in order (in).
Plies = [0.625, 0.625, 0.625]
# limit will define the maximum allowable thickness for each ply in CLT.
limit = 5
temp = 0
opt = 0
while temp == 0:
    opt = input("Select optimization method:\n1. Symmetric but un-uniform thicknesses of plies.\n2. All of the plies "
                "have the same thickness.\n3. Plies parallel to each other have the same thickness.\nSelect:")
    if opt == "CANCEL":
        sys.exit()
    opt = int(opt, base=8)
    if opt == 1 or opt == 2 or opt == 3:
        temp = 1
    else:
        print("Invalid input. Try again.")
# This function calculates the optimized plies thicknesses based on given input. "opt" is the option for method used.
# "Diff" is the iteration step. "layup" is the input layup arrangement. "Plies" is the thickness of each ply which
# will be converted to layup arrangement. "properties" is the mechanical properties of plies. "goal" is the min value
# for the property to be optimized. "R" specifies the type of property in question. R=0 is FbS, R=1 is EI,
# R=2 is GA and R=3 is V.
for R in range(4):
    Plies = optimizer.optimizer(opt, Diff, layup, Plies, limit, properties, [goal[R], goal[R + 4]], R)
layup = LayupRead.layupOrganizer(opt, layup, Plies)

print("\nResult found!\nThe thickness of plies from top layer to bottom.", layup[3:])
Results = PropertyCalc.PropertyCalc(properties, layup)
print("Fb in major direction (lbf-ft/ft) is equal to: ", round(Results[0], 2))
print("Fb in minor direction (lbf-ft/ft) is equal to: ", round(Results[4], 2))
print("EI in major direction (Mpsi) is equal to: ", round(Results[1], 2))
print("EI in minor direction (Mpsi) is equal to: ", round(Results[5], 2))
print("GA in major direction (lbf/ft) is equal to: ", round(Results[2], 2))
print("GA in minor direction (lbf/ft) is equal to: ", round(Results[6], 2))
print("V in minor direction (lbf/ft) is equal to: ", round(Results[3], 2))
print("V in minor direction (lbf/ft) is equal to: ", round(Results[7], 2))


