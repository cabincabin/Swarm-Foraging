import matplotlib.pyplot as pl


if __name__== "__main__":

    with open("FoodFindRedPoint02InertiaPoint05.csv") as f:
        content1 = f.readlines()

    good1 = [] #ID, count, val
    for line in content1:
        try:
            good1.append([int(line.split(': ')[2].strip().split('-')[0]),int(line.split('=')[1].split(']')[0]),float(line.split(': ')[2].strip().split('-')[1])])
        except:
            pass

    set1 = [[],[]]
    total = 0
    for line in good1:
        #if(line[0]>29 and line[0]<40):
        total += 1
        set1[0].append(line[1])
        set1[1].append(total)

    pl.clf()
    pl.figure(figsize=(10, 5))
    pl.plot(set1[0][:4095], set1[1])
    pl.title("Time to Find Food with .02 repulsion from red and .05 intertia")
    pl.xlabel("Count")
    pl.ylabel("Num Found Food")
    pl.legend()
    pl.show()
    print()