'''
c f m
2 2 2 Done
2 2 1 Done
2 1 2 Done
2 1 1 Done
1 2 2 Done
1 2 1 Done
1 1 2 Done
1 1 1 Done  
'''


class paternityTest:
  __rsNumberSimilar = []
  __fatherSimilar = []
  __motherSimilar = []
  __childSimilar = []
  __rsNumbersFather = []
  __rsNumbersMother = []
  __fa = []
  __mo = []
  __chFather = []
  __chMother = []
  __chromosomeFitFather = []
  __chromosomeNotFitFather = []
  __chromosomeNotFitMother = []
  __chromosomeFitMother = []

  
  def __init__(self, father, mother, child, rs, chromosome):
     self.pT(father, mother, child, rs, chromosome)
      
  def pT(self, father, mother, child, rs, chromosome):
    ch = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y','MT']
    for f, m, c, r, chro in zip(father, mother, child, rs, chromosome):
      '''2 2 2'''
      if(chro in ch):  
        if(len(c) == 2 and len(f) == 2 and len(m) == 2): 
          if(f[0] == c[0] or f[0] == c[1] or f[1] == c[0] or f[1] == c[1]):
             self.__rsNumberSimilar.append(r)
             self.__fatherSimilar.append(f)
             self.__childSimilar.append(c)
             self.__chromosomeFitFather.append(chro)
          if(m[0] == c[0] or m[0] == c[1] or m[1] == c[0] or m[1] == c[1]):
             self.__motherSimilar.append(m)
             self.__chromosomeFitMother.append(chro)
          
          if(f[0] != c[0] and f[0] != c[1] and f[1] != c[0] and f[1] != c[1]):
            self.__rsNumbersFather.append(r)
            self.__fa.append(f)
            self.__chFather.append(c)
            self.__chromosomeNotFitFather.append(chro)
          if(m[0] != c[0] and m[0] != c[1] and m[1] != c[0] and m[1] != c[1]):
            self.__rsNumbersMother.append(r)
            self.__mo.append(m)
            self.__chMother.append(c)
            self.__chromosomeNotFitMother.append(chro)
         

            '''2 2 1'''
        if(len(c) == 2 and len(f) == 2 and len(m) == 1): 
          if(f[0] == c[0] or f[0] == c[1] or f[1] == c[0] or f[1] == c[1]):
             self.__rsNumberSimilar.append(r)
             self.__fatherSimilar.append(f)
             self.__childSimilar.append(c)
             self.__chromosomeFitFather.append(chro)
          if(m[0] == c[0] or m[0] == c[1]):
             self.__motherSimilar.append(m)
             self.__chromosomeFitMother.append(chro)  
          if(f[0] != c[0] and f[0] != c[1] and f[1] != c[0] and f[1] != c[1]):
            self.__rsNumbersFather.append(r)
            self.__fa.append(f)
            self.__chFather.append(c)  
            self.__chromosomeNotFitFather.append(chro)
          if(m[0] != c[0] and m[0] != c[1]):
            self.__rsNumbersMother.append(r)
            self.__mo.append(m)
            self.__chMother.append(c)  
            self.__chromosomeNotFitMother.append(chro)
            '''2 1 2'''
        if(len(c) == 2 and len(f) == 1 and len(m) == 2): 
          if(f[0] == c[0] or f[0] == c[1]):
             self.__rsNumberSimilar.append(r)
             self.__fatherSimilar.append(f)
             self.__childSimilar.append(c)
             self.__chromosomeFitFather.append(chro)
          if(m[0] == c[0] or m[0] == c[1] or m[1] == c[0] or m[1] == c[1]):
             self.__motherSimilar.append(m)
             self.__chromosomeNotFitMother.append(chro)  
          if(f[0] != c[0] and f[0] != c[1]):
            self.__rsNumbersFather.append(r)
            self.__fa.append(f)
            self.__chFather.append(c)
            self.__chromosomeNotFitFather.append(chro)
          
          if(m[0] != c[0] and m[0] != c[1] and m[1] != c[0] and m[1] != c[1]):
            self.__rsNumbersMother.append(m)
            self.__mo.append(m)
            self.__chMother.append(c)
            self.__chromosomeNotFitMother.append(chro)     
          '''2 1 1'''
        if(len(c) == 2 and len(f) == 1 and len(m) == 1): 
          if(f[0] == c[0] or f[0] == c[1]):
             self.__rsNumberSimilar.append(r)
             self.__fatherSimilar.append(f)
             self.__childSimilar.append(c)
             self.__chromosomeFitFather.append(chro)
       
          if(m[0] == c[0] or m[0] == c[1]):
             self.__motherSimilar.append(m)
             self.__chromosomeFitMother.append(chro)
         
          if(f[0] != c[0] and f[0] != c[1]):
            self.__rsNumbersFather.append(r)
            self.__fa.append(f)
            self.__chFather.append(c)
            self.__chromosomeNotFitFather.append(chro)
         
          if(m[0] != c[0] and m[0] != c[1]):
            self.__rsNumbersMother.append(r)
            self.__mo.append(m)
            self.__chMother.append(c)        
            self.__chromosomeNotFitMother.append(chro)
         
        '''1 2 2'''
        if(len(c) == 1 and len(f) == 2 and len(m) == 2):
          if(f[0] == c[0] or f[1] == c[0]):
             self.__rsNumberSimilar.append(r)
             self.__fatherSimilar.append(f)
             self.__childSimilar.append(c)
             self.__chromosomeFitFather.append(chro)
         
          if(m[0] == c[0] or m[1] == c[0]):
             self.__motherSimilar.append(m)
             self.__chromosomeFitMother.append(chro)
         
          if(f[0] != c[0] and f[1] != c[0]):
            self.__rsNumbersFather.append(r)
            self.__fa.append(f)
            self.__chFather.append(c) 
            self.__chromosomeNotFitFather.append(chro)
         
          if(m[0] != c[0] and m[1] != c[0]):
            self.__rsNumbersMother.append(r)
            self.__mo.append(m)
            self.__chMother.append(c)    
            self.__chromosomeNotFitMother.append(chro)
         
        '''1 2 1'''
        if(len(c) == 1 and len(f) == 2 and len(m) == 1):
          if(f[0] == c[0] or f[1] == c[0]):
             self.__rsNumberSimilar.append(r)
             self.__fatherSimilar.append(f)
             self.__childSimilar.append(c)
             self.__chromosomeFitFather.append(chro)
         
          if(m[0] == c[0]):
             self.__motherSimilar.append(m)
             self.__chromosomeFitMother.append(chro)
         
          if(f[0] != c[0] and f[1] != c[0]):
            self.__rsNumbersFather.append(r)
            self.__fa.append(f)
            self.__chFather.append(c)
            self.__chromosomeNotFitFather.append(chro)
          
          if(m[0] != c[0]):
            self.__rsNumbersMother.append(r)
            self.__mo.append(m)
            self.__chMother.append(c) 
            self.__chromosomeNotFitMother.append(chro)
             
          '''1 1 2'''
        if(len(c) == 1 and len(f) == 1 and len(m) == 2):
          if(f[0] == c[0]):
             self.__rsNumberSimilar.append(r)
             self.__fatherSimilar.append(f)
             self.__childSimilar.append(c)
             self.__chromosomeFitFather.append(chro)
         
          if(m[0] == c[0] or m[1] == c[0]):
             self.__motherSimilar.append(m)
             self.__chromosomeFitMother.append(chro)
         
          if(f[0] != c[0]):
            self.__rsNumbersFather.append(r)
            self.__fa.append(f)
            self.__chFather.append(c)
            self.__chromosomeNotFitFather.append(chro)
         
          if(m[0] != c[0] and m[1] != c[0]):
            self.__rsNumbersMother.append(r)
            self.__mo.append(m)
            self.__chMother.append(c)
            self.__chromosomeNotFitMother.append(chro)
              
      
        '''1 1 1'''
        if(len(c) == 1 and len(f) == 1 and len(m) == 1): 
          if(f[0] == c[0]):
             self.__rsNumberSimilar.append(r)
             self.__fatherSimilar.append(f)
             self.__childSimilar.append(c)
             self.__chromosomeFitFather.append(chro)
         
          if(m[0] == c[0]):
             self.__motherSimilar.append(m)
             self.__chromosomeFitMother.append(chro)
         
          if(f[0] != c[0]):
            self.__rsNumbersFather.append(r)
            self.__fa.append(f)
            self.__chFather.append(c)
            self.__chromosomeNotFitFather.append(chro)
         
          if(m[0] != c[0]):
            self.__rsNumbersMother.append(r)
            self.__mo.append(m)
            self.__chMother.append(c)
            self.__chromosomeNotFitMother.append(chro)
         
      else:
         print('Error')

  '''Similar rs numbers fit the rule'''
  def getRsNumberSimilar(self):
     return self.__rsNumberSimilar
  '''Alleles of father that fit the rule'''
  def getFatherSimilar(self):
     return self.__fatherSimilar
  '''Alleles of Mother that fit the rule'''
  def getMotherSimilar(self):
     return self.__motherSimilar
  '''Alleles of Child that fit the rule'''
  def getChildSimilar(self):
     return self.__childSimilar
  '''Rs Numbers of father does not fit the rule''' 
  def getRsNumberFather(self):
     return self.__rsNumbersFather
  '''Rs Numbers of mother does not fit the rule''' 
  def getRsNumberMother(self):
     return self.__rsNumbersMother
  '''Get Alleles of father does not fit the rule'''
  def getFatherNotSimilar(self):
     return self.__fa
  '''Get Alleles of Mother does not fit the rule'''
  def getMotherNotSimilar(self):
     return self.__mo
  '''Get Alleles of child does not fit the rule with father'''
  def getChildNotSimilarWithFather(self):
     return self.__chFather
  '''Get Alleles of child does not fit the rule with Mother'''
  def getChildNotSimilarWithMother(self):
     return self.__chMother
  '''Get Chromosomes Fit Father'''   
  def getChromosomesFitFather(self):
     return self.__chromosomeFitFather
  '''Get Chromosomes Fit Mother'''   
  def getChromosomesFitMother(self):
     return self.__chromosomeFitMother
  '''Get Chromosomes Not Fit Father'''   
  def getChromosomesNotFitFather(self):
     return self.__chromosomeNotFitFather
  '''Get Chromosomes Not Fit Mother'''   
  def getChromosomesNotFitMother(self):
     return self.__chromosomeNotFitMother
  
  '''Calculate prob Father'''
  def calculateProbability(self):
        sumSimilar = len(self.getRsNumberSimilar())
        total = (len(self.getRsNumberSimilar())+ len(self.getRsNumberFather()))
        sumNotSimilar = len(self.getRsNumberFather())
        rule = sumSimilar / total
        ruleNotSimilar = sumNotSimilar / total
        return rule * 100, ruleNotSimilar * 100 
