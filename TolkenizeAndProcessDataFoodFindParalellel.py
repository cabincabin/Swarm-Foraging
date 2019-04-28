import matplotlib.pyplot as pl
import numpy as np

def openContentsAndProcess(Fname):
    with open(Fname) as f:
        content = f.readlines()
    f.close()
    content = content[23:(5000*40)]
    times = []
    RobotDict = {}
    #'[1;32mBUZZ: [0m[1;32m[=[0m[1;32m335[0m[1;32m]: [0m[1;32m39[0m[1;32m-[0m[1;32m1[0m
    for line in content:
        try:
            Rnum = int(line.split('[0m[1;32m]: [0m[1;32m')[1].strip().split('[0m')[0])
            Count = int(line.split('[1;32mBUZZ: [0m[1;32m[=[0m[1;32m')[1].strip().split('[0m[1;32m]:')[0])
            Dist = float(line.split('-[0m[1;32m')[1].strip().split('[0m')[0])
            if Rnum not in RobotDict:
                RobotDict[Rnum]=[[],[]]
            RobotDict[Rnum][0].append(Count)
            RobotDict[Rnum][1].append(Dist)
            #times.append(int(line.split('=')[1].strip().split(']')[0]))
            #good1.append([int(line.split(': ')[2].strip().split('-')[0]), int(line.split('=')[1].split(']')[0]),
                         # float(line.split(': ')[2].strip().split('-')[1])])
            # completeCount += 1
            # numComplete.append(completeCount)
        except:
            pass
    return RobotDict

if __name__== "__main__":
    #path = 'Converge22/Conv00_'
    path = 'Converge00/Conv00_'
    #path = 'Converge7322/Conv00_'
    #path = 'Converge7300/Conv00_'
    #path = 'ApatureTests/70/GreenOnly/Green1Red0_'
    pl.clf()
    pl.figure(figsize=(10, 5))
    for i in range(10):
        Fname = path + str(i+1) + ".txt"
        set = openContentsAndProcess(Fname)
        colr = "C"+str(i)
        for id in range(40):
            pl.plot(set[id][0], set[id][1], colr)#, label="Robot " + str(id) + ":test "+ str(i+1))
    pl.title("Count VS Robots Found Food Graph")
    pl.suptitle("     Robot Convergence Tests")
    pl.xlabel("Count")

    pl.ylabel("Distance to 0,0")
    pl.legend()
    pl.show()
    print()