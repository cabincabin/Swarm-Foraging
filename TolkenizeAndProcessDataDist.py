import matplotlib.pyplot as pl


if __name__== "__main__":

    with open("ConvergeAp80.csv") as f:
        content1 = f.readlines()

    good1 = [] #ID, count, val
    content1 = content1[1:]
    for line in content1:
        try:
            good1.append([int(line.split(': ')[1].strip().split('-')[0]),int(line.split('=')[1].split(']')[0]),float(line.split(': ')[1].strip().split('-')[1])])
        except:
            pass

    set1 = [[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]]]
    for line in good1:
        if(line[0]>29 and line[0]<40):
            set1[line[0]-30][0].append(line[1])
            set1[line[0]-30][1].append(line[2])

    pl.clf()
    pl.figure(figsize=(10, 5))
    pl.plot(set1[0][0][:4095], set1[0][1][:4095], 'o', label='ID 30, Dist', markersize=1)
    pl.plot(set1[1][0][:4095], set1[1][1][:4095], '+', label='ID 31, Dist', markersize=1)
    pl.plot(set1[2][0][:4095], set1[2][1][:4095], 'x', label='ID 32, Dist', markersize=1)
    pl.plot(set1[3][0][:4095], set1[3][1][:4095], '^', label='ID 33, Dist', markersize=1)
    pl.plot(set1[4][0][:4095], set1[4][1][:4095], '_', label='ID 34, Dist', markersize=1)
    pl.plot(set1[5][0][:4095], set1[5][1][:4095], '*', label='ID 35, Dist', markersize=1)
    pl.plot(set1[6][0][:4095], set1[6][1][:4095], '<', label='ID 36, Dist', markersize=1)
    pl.plot(set1[7][0][:4095], set1[7][1][:4095], '|', label='ID 37, Dist', markersize=1)
    pl.plot(set1[8][0][:4095], set1[8][1][:4095], 'd', label='ID 38, Dist', markersize=1)
    pl.plot(set1[9][0][:4095], set1[9][1][:4095], '4', label='ID 39, Dist', markersize=1)
    pl.xlabel("Count")
    pl.ylabel("Distance Value (m)")
    pl.legend()
    pl.show()
    print()