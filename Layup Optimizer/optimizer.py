import sys

import LayupRead
import PropertyCalc


def optimizer(opt, Diff, layup, Plies, limit, properties, goal, R):
    temp = 0
    if opt == 1:
        while temp == 0:
            layup = LayupRead.layupOrganizer(opt, layup, Plies)
            Results = PropertyCalc.PropertyCalc(properties, layup)
            if Results[R+4] < goal[1]:
                if Plies[2] < limit and (Plies[2] - Plies[1]) < 1 and (Plies[2] - Plies[0]) < 1:
                    Plies[2] += Diff
                elif Plies[1] < limit and (Plies[1] - Plies[2]) < 1 and (Plies[1] - Plies[0]) < 1:
                    Plies[1] += Diff
                elif Plies[0] < limit and (Plies[0] - Plies[1]) < 1 and (Plies[0] - Plies[2]) < 1:
                    Plies[0] += Diff
            elif Results[R] < goal[0]:
                if Plies[0] < limit and (Plies[0] - Plies[1]) < 1 and (Plies[0] - Plies[2]) < 1:
                    Plies[0] += Diff
                elif Plies[1] < limit and (Plies[1] - Plies[2]) < 1 and (Plies[1] - Plies[0]) < 1:
                    Plies[1] += Diff
                elif Plies[2] < limit and (Plies[2] - Plies[1]) < 1 and (Plies[2] - Plies[0]) < 1:
                    Plies[2] += Diff
            if Plies[1] == limit and Plies[0] == limit and Plies[2] == limit:
                print("\nWe have reached the limit. We couldn't find any possible layup for the specified properties.")
                sys.exit()
            elif Results[R] > goal[0] and Results[R+4] > goal[1]:
                return Plies
    if opt == 2:
        while temp == 0:
            layup = LayupRead.layupOrganizer(opt, layup, Plies)
            Results = PropertyCalc.PropertyCalc(properties, layup)
            if (Results[R+4] < goal[1] or Results[R] < goal[0]) and Plies[0] < limit:
                Plies[2] += Diff
                Plies[1] += Diff
                Plies[0] += Diff
            elif Plies[0] == limit:
                print("\nWe have reached the limit. We couldn't find any possible layup for the specified properties.")
                sys.exit()
            else:
                return Plies
    if opt == 3:
        while temp == 0:
            layup = LayupRead.layupOrganizer(opt, layup, Plies)
            Results = PropertyCalc.PropertyCalc(properties, layup)
            if Results[R+4] < goal[1]:
                if Plies[2] < limit and (Plies[2] - Plies[0]) < 1:
                    Plies[2] += Diff
                elif Plies[0] < limit and (Plies[0] - Plies[2]) < 1:
                    Plies[0] += Diff
            elif Results[R] < goal[0]:
                if Plies[0] < limit and (Plies[0] - Plies[2]) < 1:
                    Plies[0] += Diff
                elif Plies[2] < limit and (Plies[2] - Plies[0]) < 1:
                    Plies[2] += Diff
            if Plies[0] == limit and Plies[2] == limit:
                print("\nWe have reached the limit. We couldn't find any possible layup for the specified properties.")
                sys.exit()
            elif Results[R] > goal[0] and Results[R+4] > goal[1]:
                return Plies
