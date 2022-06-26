class wholeGenome:
      CounterTTTT = 0
      CounterAGAT = 0
      CounterAATG = 0
      CounterTGCC = 0
      CounterGATA = 0
      CounterTATC = 0
      CounterAAGG = 0
      CounterAGAA = 0
      __wholeGenome = {
        'TTTT': CounterTTTT,
        'AGAT': CounterAGAT,
        'AATG': CounterAATG,
        'TGCC': CounterTGCC,
        'GATA': CounterGATA,
        'TATC': CounterTATC,
        'AAGG': CounterAAGG,
        'AGAA': CounterAGAA
    }
      def Test(self, x):
            if x == "TTTT":
                  self.__wholeGenome['TTTT'] += 1
            elif x == "AGAT":
                  self.__wholeGenome['AGAT'] += 1
            elif x == "AATG":
                  self.__wholeGenome['AATG'] += 1
            elif x == "TGCC":
                  self.__wholeGenome['TGCC'] += 1
            elif x == "GATA":
                  self.__wholeGenome['GATA'] += 1
            elif x == "TATC":
                  self.__wholeGenome['TATC'] += 1
            elif x == "AAGG":
                  self.__wholeGenome['AAGG'] += 1
            elif x == "AGAA":
                  self.__wholeGenome['AGAA'] += 1


      def readFile(fileName):
            with open(fileName, 'r') as file:
                  data = file.read().rstrip()
                  n = 4    # every 2 characters
            split_string = [data[i:i+n] for i in range(0, len(data), n)]
            return split_string


      def reInitialize(self):
            for key in self.__wholeGenome.keys():
                  self.__wholeGenome[key] = 0

      def getResults(self, doc):
            decision = 0
            if ( self.__wholeGenome['AGAA']-100000 <= doc['AGAA'] <=  self.__wholeGenome['AGAA']+100000):
                  decision = decision+1
                  print("Match")
            if ( self.__wholeGenome['TTTT']-100000 <= doc['TTTT'] <=  self.__wholeGenome['TTTT']+100000):
                  decision = decision+1
                  print("Match")
            if ( self.__wholeGenome['AGAT']-100000 <= doc['AGAT'] <=  self.__wholeGenome['AGAT']+100000):
                  decision = decision+1
                  print("Match")
            if ( self.__wholeGenome['AATG']-100000 <= doc['AATG'] <=  self.__wholeGenome['AATG']+100000):
                  decision = decision+1
                  print("Match")
            if ( self.__wholeGenome['TGCC']-100000 <= doc['TGCC'] <=  self.__wholeGenome['TGCC']+100000):
                  decision = decision+1
                  print("Match")
            if ( self.__wholeGenome['GATA']-100000 <= doc['GATA'] <=  self.__wholeGenome['GATA']+100000):
                  decision = decision+1
                  print("Match")
            if ( self.__wholeGenome['TATC']-100000 <= doc['TATC'] <=  self.__wholeGenome['TATC']+100000):
                  decision = decision+1
                  print("Match")
            if ( self.__wholeGenome['AAGG']-100000 <= doc['AAGG'] <=  self.__wholeGenome['AAGG']+100000):
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
