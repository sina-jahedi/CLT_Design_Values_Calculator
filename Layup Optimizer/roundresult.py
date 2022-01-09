def round5(n, decimals=0):
    multiplier = 5 ** decimals
    return round(n * multiplier) / multiplier