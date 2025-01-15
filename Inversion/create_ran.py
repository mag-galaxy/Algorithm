import random

def CreateRandom(n):
    path = 'testdata.txt'
    f = open(path, 'w')
    f.write(str(n) + '\n')
    for i in range(n):
        f.write(str(int(random.random() * 10**6)) + '\n')

CreateRandom(950)