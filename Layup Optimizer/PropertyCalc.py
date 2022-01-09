import numpy as np

import  BendingStiffness, BendingMoment, ShearRigidity, ShearCapacity

def PropertyCalc(properties, layup):
    results = np.zeros(8)
    for idx in range(2):
        layup[1] = idx + 1
        results[0 + ((idx%2)*4)] = BendingMoment.BendingMoment(properties, layup)
        results[1 + ((idx%2)*4)] = BendingStiffness.BendingStiffness(properties, layup)
        results[2 + ((idx%2)*4)] = ShearRigidity.ShearRigidity(properties, layup)
        results[3 + ((idx%2)*4)] = ShearCapacity.ShearCapacity(properties, layup)
    return results