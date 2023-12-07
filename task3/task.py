import csv
from math import log

def Entropy(csv_line):
    matrix = []
    for r in csv_line.splitlines():
        r_ = []
        for val in r.split(","):
            r_.append(int(val))
        matrix.append(r_)

    ent = 0
    for r in matrix:
        ent_ = 0
        for val in r:
            p = val / (len(matrix) - 1)
            if p <= 0:
                continue
            log_ = log(p, 2)
            ent_ += p * log_
        ent += -ent_

    print(round(ent, 1))

file_=input()
with open(file_, 'r') as file_r:
    csv_r = csv.reader(file_r, delimiter=",")
    L = list(csv_r)
data = ""
for i in L:
    data += ",".join(i)
    data += "\n" 

Entropy(data)
