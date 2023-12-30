import numpy as np
import json

def flatListSize(data) -> int:
    res = 0
    for item in data:
        if isinstance(item, list):
            for l2 in item:
                res += 1
        else:
            res += 1
    return res 

def flatList(data) -> list:
    if (type(data) != list):
        data = json.loads(data)
    res = []
    for item in data:
        if isinstance(item, list):
            item_sum = 0
            for l2 in item:
                item_sum += int(l2)
            value = item_sum/len(item)
            for l2 in item:
                res.append(value)
        else:
            res.append(int(item))
    return res 

def get_hk(data) -> list:
    res = []
    for item in data:
        if isinstance(item, list):
            res.append(len(item))
    return res 

def get_Ts(data) -> int:
    res = 0
    for item in data:
        res += item ** 3 - item
    return res 

def task(*rankings: str) -> float:
    m = len(rankings)
    rL = [json.loads(r) for r in rankings]
    ni = [flatListSize(r) for r in rL]
    n = ni[0]
    matrix = np.array([np.array(flatList(r)) for r in rL]).T
    Xi = np.sum(matrix, axis=1)
    Xavg = Xi.mean()
    S = np.sum(np.square(Xi - Xavg))
    D = S / (n - 1)
    hk = [get_hk(r) for r in rL]
    Ts = [get_Ts(h) for h in hk]
    Dmax = (m ** 2 * (n ** 3 - n) - m * np.sum(Ts)) / (12 * (n - 1))
    W = D / Dmax
    return round(W, 2)


print(task('[1,[2,3],4,[5,6,7],8,9,10]', '[[1,2],[3,4,5],6,7,9,[8,10]]'))

