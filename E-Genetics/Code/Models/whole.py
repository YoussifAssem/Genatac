class wholeGenome:
    __whole = {}
    def __init__(self):
        self.__whole = {
        'TTTT': 0,
        'AGAT': 0,
        'AATG': 0,
        'TGCC': 0,
        'GATA': 0,
        'TATC': 0,
        'AAGG': 0,
        'AGAA': 0
    }
      
    def Test(self, x):
       if x == "TTTT":
              self.__whole['TTTT'] += 1
       elif x == "AGAT":
              self.__whole['AGAT'] += 1
       elif x == "AATG":
              self.__whole['AATG'] += 1
       elif x == "TGCC":
              self.__whole['TGCC'] += 1
       elif x == "GATA":
              self.__whole['GATA'] += 1
       elif x == "TATC":
              self.__whole['TATC'] += 1
       elif x == "AAGG":
              self.__whole['AAGG'] += 1
       elif x == "AGAA":
              self.__whole['AGAA'] += 1


    def readFile(fileName):
       with open(fileName, 'r') as file:
              data = file.read().rstrip()
              n = 4    # every 2 characters
       split_string = [data[i:i+n] for i in range(0, len(data), n)]
       return split_string

    def reInitialize(self):
       for key in self.__whole.keys():
               self.__whole[key] = 0
               
    def selectedFile(self, name):
       for x in self.readFile(name):
            self.Test(x)
    
    def getwholeGenome(self):
           return self.__whole  

    def getResults(self, doc):
        print('Before Running Daughter', self.__whole)
        print('After Running Daughter', self.__whole)
        decision =0
        if (doc['AGAA']>=self.__whole['AGAA']*1.5 and doc['AGAA']<=self.__whole['AGAA']*1.5 ):
              decision = decision+1
              print("Match")
        else :
              print("No Match")

        if (doc['TTTT'] >= self.__whole['TTTT']*1.5 and doc['TTTT'] <= self.__whole['TTTT']*1.5):
              decision = decision+1
              print("Match")
        else :
              print("No Match")
        if (doc['AGAT'] >= self.__whole['AGAT']*1.5 and doc['AGAT'] <= self.__whole['AGAT']*1.5):
              decision = decision+1
              print("Match")   
        else :
              print("No Match")           
        if (doc['AATG'] >= self.__whole['AATG']*1.5 and doc['AATG'] <= self.__whole['AATG']*1.5):
              decision = decision+1
              print("Match")   
        else :
              print("No Match")          
        if (doc['TGCC'] >= self.__whole['TGCC']*1.5 and doc['TGCC'] <= self.__whole['TGCC']*1.5):
              decision = decision+1
              print("Match")       
        else :
              print("No Match")
        if (doc['GATA'] >= self.__whole['GATA']*1.5 and doc['GATA'] <= self.__whole['GATA']*1.5):
              decision = decision+1
              print("Match")        
        else :
              print("No Match")
        if (doc['TATC'] >= self.__whole['TATC']*1.5 and doc['TATC'] <= self.__whole['TATC']*1.5):
              decision = decision+1
              print("Match")
        else :
              print("No Match")
        if (doc['AAGG'] >= self.__whole['AAGG']*1.5 and doc['AAGG'] >= self.__whole['AAGG']*1.5):
              decision = decision+1
              print("Match")       
        else :
              print("No Match")
        if(decision >= 4 ):
              return "According to the whole genome you entered ,the 2 people you entered is RELATED"
        elif(decision <= 2 and decision != 0):     
              return "According to the whole genome you entered, the 2 people you entered has 2 matching repeats but NOT RELATED"
        elif(decision == 0):
              return "According to the whole genome you entered, the 2 people you entered is NOT RELATED"


       

