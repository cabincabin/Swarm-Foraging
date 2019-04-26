import matplotlib.pyplot as pl


if __name__== "__main__":

    with open("Control1.csv") as f:
        content1 = f.readlines()
    with open("Control12.csv") as f2:
        content2 = f2.readlines()
    with open("Control123.csv") as f3:
        content3 = f3.readlines()

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

    good2 = []  # ID, count, val
    for line in content2:
        try:
            good2.append([int(line.split(': ')[2].strip().split('-')[0]), int(line.split('=')[1].split(']')[0]),
                          float(line.split(': ')[2].strip().split('-')[1])])
        except:
            pass

    set2 = [[], []]
    total = 0
    for line in good2:
        # if(line[0]>29 and line[0]<40):
        total += 1
        set2[0].append(line[1])
        set2[1].append(total)

    good3 = []  # ID, count, val
    for line in content3:
        try:
            good3.append([int(line.split(': ')[2].strip().split('-')[0]), int(line.split('=')[1].split(']')[0]),
                          float(line.split(': ')[2].strip().split('-')[1])])
        except:
            pass

    set3 = [[], []]
    total = 0
    for line in good3:
        # if(line[0]>29 and line[0]<40):
        total += 1
        set3[0].append(line[1])
        set3[1].append(total)

    pl.clf()
    pl.figure(figsize=(10, 5))
    pl.plot(set1[0][:20], set1[1][:20], "b")
    pl.plot(set2[0][:20], set2[1][:20], "r")
    pl.plot(set3[0][:20], set3[1][:20], "y")
    pl.title("Control: Time to First 20 Robots Finding food with random walks")

    pl.xlabel("Count")
    pl.ylabel("Num Found Food")
    pl.legend()
    pl.show()
    print()