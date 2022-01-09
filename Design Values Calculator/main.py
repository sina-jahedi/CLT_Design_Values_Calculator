import numpy as np

import CSVread, LayupRead, BendingStiffness, BendingMoment, ShearRigidity, ShearCapacity, roundresult

properties = CSVread.CSVread('inputdata.csv')
# Reading CLT layup. To opt out from this remove/comment-out the following line and un-comment line 9, 11,
# or 13. You can modify those layups manually. The layup should be symmetric.
#layup = LayupRead.layupread()
# 7 plies CLT
layup = np.array([7., 1., 12., 1.375, 1.375, 1.375, 1.375, 1.375, 1.375, 1.375])
# 5 plies CLT
#layup = np.array([5., 1., 12., 1.375, 1.375, 1.375, 1.375, 1.375])
# 3 plies CLT
#layup = np.array([3., 2., 12., 1.375, 1.375, 1.375])
print(layup)
temp = 0
opt = 0
while temp == 0:
    opt = input("\nSelect the property you desire to calculate:\n1.Flatwise Bending Stiffness\n2.Flatwise Bending "
                "Moment\n3.Flatwise Shear Rigidity\n4.Flatwise (Rolling) Shear Capacity\n5.All\nSelect:")
    if opt == "1" or opt == "2" or opt == "3" or opt == "4" or opt == "5":
        temp = 1
    else:
        print("Invalid input. Try again.")
bendingstiffness = 0
bendingmoment = 0
shearrigidity = 0
shearcapacity = 0
for idx in range(2):
    layup[1] = idx + 1
    if opt == "1":
        bendingstiffness = BendingStiffness.BendingStiffness(properties, layup)
    elif opt == "2":
        bendingmoment = BendingMoment.BendingMoment(properties, layup)
    elif opt == "3":
        shearrigidity = ShearRigidity.ShearRigidity(properties, layup)
    elif opt == "4":
        shearcapacity = ShearCapacity.ShearCapacity(properties, layup)
    else:
        bendingstiffness = BendingStiffness.BendingStiffness(properties, layup)
        bendingmoment = BendingMoment.BendingMoment(properties, layup)
        shearrigidity = ShearRigidity.ShearRigidity(properties, layup)
        shearcapacity = ShearCapacity.ShearCapacity(properties, layup)
    if idx == 0:
        direction = "major"
    else:
        direction = "minor"
    print("Fb in", direction, " direction (lbf-ft/ft): ", roundresult.round5(bendingmoment, -1))
    print("EI in ", direction, " direction (Mpsi): ", roundresult.round1(bendingstiffness, -1))
    print("GA in ", direction, " direction (lbf/ft): ", roundresult.round1(shearrigidity, -1))
    print("Vs in ", direction, " direction (lbf/ft): ", roundresult.round5(shearcapacity, -1))
    #print(roundresult.round5(bendingmoment, -1),"\n", roundresult.round1(bendingstiffness, -1),"\n", roundresult.round1(shearrigidity, -1),"\n", roundresult.round5(shearcapacity, -1))