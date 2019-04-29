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

            times.append(int(line.split('[1;32mBUZZ: [0m[1;32m=[0m[1;32m')[1].strip().split('[0m[1;32m]:')[0]))
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
    #path = 'ApatureTests/75/GreenOnly/Green1_Red0_'
    #path = 'ApatureTests/75/RedOnly/Green0_RedNeg1_'
    #path = 'ApatureTests/75/Both/Green1_RedNeg1_'
    path = 'control/c_'
    pl.clf()
    pl.figure(figsize=(10, 5))
    supsetCount = []
    supsetFount = []
    for i in range(25):
        Fname = path + str(i+1) + '.txt'
        set = openContentsAndProcess(Fname)
        #pl.plot(set[0], set[1])
        supsetCount.append(set[0])
        supsetFount.append(set[1])

    a = np.zeros(33)
    for i in range(33):
        l = 0
        for j in range(25):
            try:
                a[i] += supsetCount[j][i]
                l += 1
            except:
                pass

        a[i] = a[i]/l
    #pl.scatter(a,supsetFount[19])
    print(np.polyfit(np.log(a),supsetFount[19], 1))
    xax = range(1,15000)
    yax = 9.94000325*np.log(xax) -67.38994838
    pl.ylim(0,40)
    pl.plot(xax,yax)
    pl.title("Count VS Robots Found Food Graph")
    pl.suptitle("     Control Data")
    pl.xlabel("Count")
    pl.ylabel("Number Of Robots that have Found Food")
    pl.legend()
    pl.show()
    print()