



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
              n = 4	# every 2 characters
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
    
    for x in readFile('dad.txt'):
       Test(x)
    print('Before Running Daughter', wholeGenome)
    
    reInitialize(wholeGenome)   
    
    for x in readFile('dau.txt'):
       Test(x)
    print('After Running Daughter', wholeGenome)
