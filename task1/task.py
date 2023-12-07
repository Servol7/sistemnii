import csv

file_=input()
r=int(input())
c=int(input())

with open(file_, 'r') as file_r:
    csv_r = csv.reader(file_r, delimiter=',')
    print(list(csv_r)[r][c])
