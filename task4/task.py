import numpy as np

def task():
    k = 6
    res = np.zeros((k * 2 + 1, k ** 2 + 1))
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            res[i + j, i * j] += 1
    res /= 36

    HAs = np.sum(res, axis=1)
    HA = -np.sum(HAs * np.log2(HAs, where=np.abs(HAs) > 1e-5))

    HBs = np.sum(res, axis=0)
    HB = -np.sum(HBs * np.log2(HBs, where=np.abs(HBs) > 1e-5))

    HAB = -np.sum(res * np.log2(res, where=np.abs(res) > 1e-5))

    HaB = HAB - HA

    I = HB - HaB

    ret = [HAB, HA, HB, HaB, I]
    return [round(el, 2) for el in ret]

print(task())
