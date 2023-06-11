import numpy as np

def PAA(TS, n):
    splits = np.array_split(TS, n) # n: number of splits

    paa = [split.mean(axis=0) for split in splits]

    return paa