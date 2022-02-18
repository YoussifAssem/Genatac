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
  rsNumberSimilar = []
  fatherSimilar = []
  motherSimilar = []
  childSimilar = []
  rsNumbersFather = []
  rsNumbersMother = []
  fa = []
  mo = []
  chFather = []
  chMother = []
  chromosomeFitFather = []
  chromosomeNotFitFather = []
  chromosomeNotFitMother = []
  chromosomeFitMother = []

  
  def __init__(self, father, mother, child, rs, chromosome):
     self.pT(father, mother, child, rs, chromosome)
      
  def pT(self, father, mother, child, rs, chromosome):
    ch = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y','MT']
    for f, m, c, r, chro in zip(father, mother, child, rs, chromosome):
      '''2 2 2'''
      if(chro in ch):  
        if(len(c) == 2 and len(f) == 2 and len(m) == 2): 
          if(f[0] == c[0] or f[0] == c[1] or f[1] == c[0] or f[1] == c[1]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
             self.chromosomeFitFather.append(chro)
          if(m[0] == c[0] or m[0] == c[1] or m[1] == c[0] or m[1] == c[1]):
             self.motherSimilar.append(m)
             self.chromosomeFitMother.append(chro)
          
          if(f[0] != c[0] and f[0] != c[1] and f[1] != c[0] and f[1] != c[1]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
            self.chromosomeNotFitFather.append(chro)
          if(m[0] != c[0] and m[0] != c[1] and m[1] != c[0] and m[1] != c[1]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)
            self.chromosomeNotFitMother.append(chro)
         

            '''2 2 1'''
        if(len(c) == 2 and len(f) == 2 and len(m) == 1): 
          if(f[0] == c[0] or f[0] == c[1] or f[1] == c[0] or f[1] == c[1]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
             self.chromosomeFitFather.append(chro)
          if(m[0] == c[0] or m[0] == c[1]):
             self.motherSimilar.append(m)
             self.chromosomeFitMother.append(chro)  
          if(f[0] != c[0] and f[0] != c[1] and f[1] != c[0] and f[1] != c[1]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)  
            self.chromosomeNotFitFather.append(chro)
          if(m[0] != c[0] and m[0] != c[1]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)  
            self.chromosomeNotFitMother.append(chro)
            '''2 1 2'''
        if(len(c) == 2 and len(f) == 1 and len(m) == 2): 
          if(f[0] == c[0] or f[0] == c[1]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
             self.chromosomeFitFather.append(chro)
          if(m[0] == c[0] or m[0] == c[1] or m[1] == c[0] or m[1] == c[1]):
             self.motherSimilar.append(m)
             self.chromosomeNotFitMother.append(chro)  
          if(f[0] != c[0] and f[0] != c[1]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
            self.chromosomeNotFitFather.append(chro)
          
          if(m[0] != c[0] and m[0] != c[1] and m[1] != c[0] and m[1] != c[1]):
            self.rsNumbersMother.append(m)
            self.mo.append(m)
            self.chMother.append(c)
            self.chromosomeNotFitMother.append(chro)     
          '''2 1 1'''
        if(len(c) == 2 and len(f) == 1 and len(m) == 1): 
          if(f[0] == c[0] or f[0] == c[1]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
             self.chromosomeFitFather.append(chro)
       
          if(m[0] == c[0] or m[0] == c[1]):
             self.motherSimilar.append(m)
             self.chromosomeFitMother.append(chro)
         
          if(f[0] != c[0] and f[0] != c[1]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
            self.chromosomeNotFitFather.append(chro)
         
          if(m[0] != c[0] and m[0] != c[1]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)        
            self.chromosomeNotFitMother.append(chro)
         
        '''1 2 2'''
        if(len(c) == 1 and len(f) == 2 and len(m) == 2):
          if(f[0] == c[0] or f[1] == c[0]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
             self.chromosomeFitFather.append(chro)
         
          if(m[0] == c[0] or m[1] == c[0]):
             self.motherSimilar.append(m)
             self.chromosomeFitMother.append(chro)
         
          if(f[0] != c[0] and f[1] != c[0]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c) 
            self.chromosomeNotFitFather.append(chro)
         
          if(m[0] != c[0] and m[1] != c[0]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)    
            self.chromosomeNotFitMother.append(chro)
         
        '''1 2 1'''
        if(len(c) == 1 and len(f) == 2 and len(m) == 1):
          if(f[0] == c[0] or f[1] == c[0]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
             self.chromosomeFitFather.append(chro)
         
          if(m[0] == c[0]):
             self.motherSimilar.append(m)
             self.chromosomeFitMother.append(chro)
         
          if(f[0] != c[0] and f[1] != c[0]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
            self.chromosomeNotFitFather.append(chro)
          
          if(m[0] != c[0]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c) 
            self.chromosomeNotFitMother.append(chro)
             
          '''1 1 2'''
        if(len(c) == 1 and len(f) == 1 and len(m) == 2):
          if(f[0] == c[0]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
             self.chromosomeFitFather.append(chro)
         
          if(m[0] == c[0] or m[1] == c[0]):
             self.motherSimilar.append(m)
             self.chromosomeFitMother.append(chro)
         
          if(f[0] != c[0]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
            self.chromosomeNotFitFather.append(chro)
         
          if(m[0] != c[0] and m[1] != c[0]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)
            self.chromosomeNotFitMother.append(chro)
              
      
        '''1 1 1'''
        if(len(c) == 1 and len(f) == 1 and len(m) == 1): 
          if(f[0] == c[0]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
             self.chromosomeFitFather.append(chro)
         
          if(m[0] == c[0]):
             self.motherSimilar.append(m)
             self.chromosomeFitMother.append(chro)
         
          if(f[0] != c[0]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
            self.chromosomeNotFitFather.append(chro)
         
          if(m[0] != c[0]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)
            self.chromosomeNotFitMother.append(chro)
         
      else:
         print('Error')

  '''Similar rs numbers fit the rule'''
  def getRsNumberSimilar(self):
     return self.rsNumberSimilar
  '''Alleles of father that fit the rule'''
  def getFatherSimilar(self):
     return self.fatherSimilar
  '''Alleles of Mother that fit the rule'''
  def getMotherSimilar(self):
     return self.motherSimilar
  '''Alleles of Child that fit the rule'''
  def getChildSimilar(self):
     return self.childSimilar
  '''Rs Numbers of father does not fit the rule''' 
  def getRsNumberFather(self):
     return self.rsNumbersFather
  '''Rs Numbers of mother does not fit the rule''' 
  def getRsNumberMother(self):
     return self.rsNumbersMother
  '''Get Alleles of father does not fit the rule'''
  def getFatherNotSimilar(self):
     return self.fa
  '''Get Alleles of Mother does not fit the rule'''
  def getMotherNotSimilar(self):
     return self.mo
  '''Get Alleles of child does not fit the rule with father'''
  def getChildNotSimilarWithFather(self):
     return self.chFather
  '''Get Alleles of child does not fit the rule with Mother'''
  def getChildNotSimilarWithMother(self):
     return self.chMother
  '''Get Chromosomes Fit Father'''   
  def getChromosomesFitFather(self):
     return self.chromosomeFitFather
  '''Get Chromosomes Fit Mother'''   
  def getChromosomesFitMother(self):
     return self.chromosomeFitMother
  '''Get Chromosomes Not Fit Father'''   
  def getChromosomesNotFitFather(self):
     return self.chromosomeNotFitFather
  '''Get Chromosomes Not Fit Mother'''   
  def getChromosomesNotFitMother(self):
     return self.chromosomeNotFitMother
  
  '''Calculate prob Father'''
  def calculateProbability(self):
        sumSimilar = len(self.getRsNumberSimilar())
        total = (len(self.getRsNumberSimilar())+ len(self.getRsNumberFather()))
        sumNotSimilar = len(self.getRsNumberFather())
        rule = sumSimilar / total
        ruleNotSimilar = sumNotSimilar / total
        return rule * 100, ruleNotSimilar * 100 
