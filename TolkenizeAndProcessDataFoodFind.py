import matplotlib.pyplot as pl
import numpy as np

def openContentsAndProcess(Fname):
    with open(Fname) as f:
        content = f.readlines()
    f.close()
    content = content[24:]
    times = []
    numComplete = []
    completeCount = 0#'[1;32mBUZZ: [0m[1;32m[=[0m[1;32m335[0m[1;32m]: [0m[1;32m39[0m[1;32m-[0m[1;32m1[0m
    for line in content:
        try:

            times.append(int(line.split('[1;32mBUZZ: [0m[1;32m[=[0m[1;32m')[1].strip().split('[0m[1;32m]:')[0]))
            #good1.append([int(line.split(': ')[2].strip().split('-')[0]), int(line.split('=')[1].split(']')[0]),
                         # float(line.split(': ')[2].strip().split('-')[1])])
            completeCount += 1
            numComplete.append(completeCount)
        except:
            pass
    return [times, numComplete]

if __name__== "__main__":
    #path = 'GreenOnly/Green1Red0_'
    #path = 'RedOnly/Green0RedNeg1_'
    #path = 'ApatureTests/70/GreenOnly/Green1Red0_'
    #path = 'ApatureTests/70/RedOnly/Green0_RedNeg1_'
    #path = 'ApatureTests/70/Both/Green1_RedNeg1_'
    path = 'ApatureTests/75/GreenOnly/Green1_Red0_'
    #path = 'ApatureTests/75/RedOnly/Green0_RedNeg1_'
    #path = 'ApatureTests/75/Both/Green1_RedNeg1_'
    pl.clf()
    pl.figure(figsize=(10, 5))
    for i in range(25):
        Fname = path + str(i+1) + '.txt'
        set = openContentsAndProcess(Fname)
        pl.plot(set[0], set[1])
    pl.title("Count VS Robots Found Food Graph")
    pl.suptitle("     Aperture 88, only Repulsion (Red)")
    pl.xlabel("Count")
    pl.ylabel("Number Of Robots that have Found Food")
    pl.legend()
    pl.show()
    print()