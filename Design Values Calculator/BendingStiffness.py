import copy


def ZCalc(n, layup):
    mid = int((layup[0] + 1) / 2)
    if n == mid:
        z = 0
        return z
    if n > mid:
        z = ZCalc(mid - (n - mid), layup)
        return z
    z = layup[n + 2] / 2
    for idx in range((n + 1), (mid)):
        z += layup[idx + 2]
    z += layup[mid + 2] / 2
    return z


def BendingStiffness(properties, layup):
    if properties[0] == 0 or properties[0] == "0" or properties[1] == 0 or properties[1] == "0":
        print("Missing essential input data. Module of Elasticity missing.")
        return 0
    EI = 0
    temp = copy.deepcopy(properties)
    if layup[1] == 1:
        temp[1] = temp[1] / 30
    else:
        temp[0] = temp[0] / 30
    for idx in range(int(layup[0])):
        z = ZCalc(idx + 1, layup)
        if layup[1] == 1:
            EI += ((temp[idx % 2] * layup[2]) * (((layup[idx + 3] ** 3) / 12) + (layup[idx + 3] * (z ** 2))))
        else:
            if idx != 0 and idx != int(layup[0]) - 1:
                EI += ((temp[idx % 2] * layup[2]) * (((layup[idx + 3] ** 3) / 12) + (layup[idx + 3] * (z ** 2))))
    return EI
