def round5(n, decimals=0):
    if n > 2500:
        multiplier = 25 ** decimals
        return round(n * multiplier) / multiplier
    elif 2500 <= n <= 1000:
        multiplier = 10 ** decimals
        return round(n * multiplier) / multiplier
    else:
        multiplier = 5 ** decimals
        return round(n * multiplier) / multiplier


def round1(n, decimals=0):
    if n > 10:
        multiplier = 1 ** decimals
        return round(n * multiplier) / multiplier
    elif 1 <= n <= 10:
        multiplier = 0.1 ** decimals
        return round(n * multiplier) / multiplier
    else:
        multiplier = 0.01 ** decimals
        return round(n * multiplier) / multiplier
