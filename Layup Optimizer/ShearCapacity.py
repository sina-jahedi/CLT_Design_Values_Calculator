
def ShearCapacity(properties, layup):
    thickness = 0
    V = 0
    for idx in range(int(layup[0])):
        thickness += layup[idx + 3]
    if layup[1] == 1:
        V = properties[5] * ( 2 /3) * thickness * layup[2]
    if layup[1] == 2:
        thickness = thickness - layup[3] - layup[int(layup[0] + 2)]
        V = properties[4] * ( 2 /3) * thickness * layup[2]
    return V
