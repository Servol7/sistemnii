import numpy as np

def task():
    k = 6
    res = np.zeros((k * 2 + 1, k ** 2 + 1))
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            res[i + j, i * j] += 1
    res /= 36

    H_As = np.sum(res, axis=1)
    H_A = -np.sum(H_As * np.log2(H_As, where=np.abs(H_As) > 1e-5))

    H_Bs = np.sum(res, axis=0)
    H_B = -np.sum(H_Bs * np.log2(H_Bs, where=np.abs(H_Bs) > 1e-5))

    H_AB = -np.sum(res * np.log2(res, where=np.abs(res) > 1e-5))

    Ha_B = H_AB - H_A

    I_AB = H_B - Ha_B

    ret = [H_AB, H_A, H_B, Ha_B, I_AB]
    return [round(el, 2) for el in ret]

print(task())
