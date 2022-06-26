

CounterTTTT = 0
CounterAGAT = 0
CounterAATG = 0
CounterTGCC = 0
CounterGATA = 0
CounterTATC = 0
CounterAAGG = 0
CounterAGAA = 0


def Test(x):
    if x == "TTTT":
        wholeGenome['TTTT'] += 1
    elif x == "AGAT":
        wholeGenome['AGAT'] += 1
    elif x == "AATG":
        wholeGenome['AATG'] += 1
    elif x == "TGCC":
        wholeGenome['TGCC'] += 1
    elif x == "GATA":
        wholeGenome['GATA'] += 1
    elif x == "TATC":
        wholeGenome['TATC'] += 1
    elif x == "AAGG":
        wholeGenome['AAGG'] += 1
    elif x == "AGAA":
        wholeGenome['AGAA'] += 1


def readFile(fileName):
    with open(fileName, 'r') as file:
        data = file.read().rstrip()
        n = 4    # every 2 characters
    split_string = [data[i:i+n] for i in range(0, len(data), n)]
    return split_string


def reInitialize(wholeGenome):
    for key in wholeGenome.keys():
        wholeGenome[key] = 0


if __name__ == '__main__':
    wholeGenome = {
        'TTTT': CounterTTTT,
        'AGAT': CounterAGAT,
        'AATG': CounterAATG,
        'TGCC': CounterTGCC,
        'GATA': CounterGATA,
        'TATC': CounterTATC,
        'AAGG': CounterAAGG,
        'AGAA': CounterAGAA
    }


for x in readFile('dad2.txt'):
    Test(x)
    doc = wholeGenome.copy()

print('Before Running Daughter', wholeGenome)


reInitialize(wholeGenome)

for x in readFile('dau2.txt'):
    Test(x)

print('After Running Daughter', wholeGenome)
print(doc['TTTT'])
print(wholeGenome['TTTT'])


decision = 0

if (wholeGenome['AGAA']-100000 <= doc['AGAA'] <= wholeGenome['AGAA']+100000):
    decision = decision+1
    print("Match")
else:
    print("No Match")

if (wholeGenome['TTTT']-100000 <= doc['TTTT'] <= wholeGenome['TTTT']+100000):
    decision = decision+1
    print("Match")
else:
    print("No Match")
if (wholeGenome['AGAT']-100000 <= doc['AGAT'] <= wholeGenome['AGAT']+100000):
    decision = decision+1
    print("Match")
else:
    print("No Match")
if (wholeGenome['AATG']-100000 <= doc['AATG'] <= wholeGenome['AATG']+100000):
    decision = decision+1
    print("Match")
else:
    print("No Match")
if (wholeGenome['TGCC']-100000 <= doc['TGCC'] <= wholeGenome['TGCC']+100000):
    decision = decision+1
    print("Match")
else:
    print("No Match")
if (wholeGenome['GATA']-100000 <= doc['GATA'] <= wholeGenome['GATA']+100000):
    decision = decision+1
    print("Match")
else:
    print("No Match")
if (wholeGenome['TATC']-100000 <= doc['TATC'] <= wholeGenome['TATC']+100000):
    decision = decision+1
    print("Match")
else:
    print("No Match")
if (wholeGenome['AAGG']-100000 <= doc['AAGG'] <= wholeGenome['AAGG']+100000):
    decision = decision+1
    print("Match")
else:
    print("No Match")


if(decision >= 4):
    print("According to the whole genome you entered ,the 2 people you entered is RELATED")
elif(decision <= 2 and decision != 0):
    print("According to the whole genome you entered, the 2 people you entered has 2 matching repeats but NOT RELATED")
elif(decision == 0):
    print("According to the whole genome you entered, the 2 people you entered is NOT RELATED")
