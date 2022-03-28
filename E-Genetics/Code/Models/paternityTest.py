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
  __dic = {
      'rsNumberSimilar': [],
      'father':[],
      'mother': [],
      'child': [],
      'notFather': [],
      'notMother': [],
      'fatherNotSimilarRs': [],
      'motherNotSimilarRs': [],
      'chFather': [],
      'chMother': [],
      'chromosomeFitFather': [],
      'chromosomeNotFitFather': [],
      'chromosomeFitMother': [],
      'chromosomeNotFitMother': [],
    }

  
  def __init__(self, father, mother, child, rs, chromosome):
     self.pT(father, mother, child, rs, chromosome)
      
  def pT(self, father, mother, child, rs, chromosome):
    ch = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y','MT']
    for f, m, c, r, chro in zip(father, mother, child, rs, chromosome):
      '''2 2 2'''
      if(chro in ch):  
        if(len(c) == 2 and len(f) == 2 and len(m) == 2): 
          if(f[0] == c[0] or f[0] == c[1] or f[1] == c[0] or f[1] == c[1]):
             self.__dic['rsNumberSimilar'].append(r)
             self.__dic['father'].append(f)
             self.__dic['child'].append(c)
             self.__dic['chromosomeFitFather'].append(chro)
          if(m[0] == c[0] or m[0] == c[1] or m[1] == c[0] or m[1] == c[1]):
             self.__dic['mother'].append(m)
             self.__dic['chromosomeFitMother'].append(chro)
          
          if(f[0] != c[0] and f[0] != c[1] and f[1] != c[0] and f[1] != c[1]):
            self.__dic['fatherNotSimilarRs'].append(r)
            self.__dic['notFather'].append(f)
            self.__dic['chFather'].append(c)
            self.__dic['chromosomeNotFitFather'].append(chro)
          if(m[0] != c[0] and m[0] != c[1] and m[1] != c[0] and m[1] != c[1]):
            self.__dic['motherNotSimilarRs'].append(r)
            self.__dic['notMother'].append(m)
            self.__dic['chMother'].append(c)
            self.__dic['chromosomeNotFitMother'].append(chro)
         

            '''2 2 1'''
        if(len(c) == 2 and len(f) == 2 and len(m) == 1): 
          if(f[0] == c[0] or f[0] == c[1] or f[1] == c[0] or f[1] == c[1]):
             self.__dic['rsNumberSimilar'].append(r)
             self.__dic['father'].append(f)
             self.__dic['child'].append(c)
             self.__dic['chromosomeFitFather'].append(chro)
          if(m[0] == c[0] or m[0] == c[1]):
             self.__dic['mother'].append(m)
             self.__dic['chromosomeFitMother'].append(chro)
          if(f[0] != c[0] and f[0] != c[1] and f[1] != c[0] and f[1] != c[1]):
            self.__dic['fatherNotSimilarRs'].append(r)
            self.__dic['notFather'].append(f)
            self.__dic['chFather'].append(c)
            self.__dic['chromosomeNotFitFather'].append(chro)
          if(m[0] != c[0] and m[0] != c[1]):
            self.__dic['motherNotSimilarRs'].append(r)
            self.__dic['notMother'].append(m)
            self.__dic['chMother'].append(c)
            self.__dic['chromosomeNotFitMother'].append(chro)
            '''2 1 2'''
        if(len(c) == 2 and len(f) == 1 and len(m) == 2): 
          if(f[0] == c[0] or f[0] == c[1]):
             self.__dic['rsNumberSimilar'].append(r)
             self.__dic['father'].append(f)
             self.__dic['child'].append(c)
             self.__dic['chromosomeFitFather'].append(chro)
          if(m[0] == c[0] or m[0] == c[1] or m[1] == c[0] or m[1] == c[1]):
             self.__dic['mother'].append(m)
             self.__dic['chromosomeFitMother'].append(chro)
          if(f[0] != c[0] and f[0] != c[1]):
            self.__dic['fatherNotSimilarRs'].append(r)
            self.__dic['notFather'].append(f)
            self.__dic['chFather'].append(c)
            self.__dic['chromosomeNotFitFather'].append(chro)
          
          if(m[0] != c[0] and m[0] != c[1] and m[1] != c[0] and m[1] != c[1]):
            self.__dic['motherNotSimilarRs'].append(r)
            self.__dic['notMother'].append(m)
            self.__dic['chMother'].append(c)
            self.__dic['chromosomeNotFitMother'].append(chro)     
          '''2 1 1'''
        if(len(c) == 2 and len(f) == 1 and len(m) == 1): 
          if(f[0] == c[0] or f[0] == c[1]):
             self.__dic['rsNumberSimilar'].append(r)
             self.__dic['father'].append(f)
             self.__dic['child'].append(c)
             self.__dic['chromosomeFitFather'].append(chro)
          if(m[0] == c[0] or m[0] == c[1]):
             self.__dic['mother'].append(m)
             self.__dic['chromosomeFitMother'].append(chro)
         
          if(f[0] != c[0] and f[0] != c[1]):
            self.__dic['fatherNotSimilarRs'].append(r)
            self.__dic['notFather'].append(f)
            self.__dic['chFather'].append(c)
            self.__dic['chromosomeNotFitFather'].append(chro)
         
          if(m[0] != c[0] and m[0] != c[1]):
            self.__dic['motherNotSimilarRs'].append(r)
            self.__dic['notMother'].append(m)
            self.__dic['chMother'].append(c)
            self.__dic['chromosomeNotFitMother'].append(chro)
         
        '''1 2 2'''
        if(len(c) == 1 and len(f) == 2 and len(m) == 2):
          if(f[0] == c[0] or f[1] == c[0]):
             self.__dic['rsNumberSimilar'].append(r)
             self.__dic['father'].append(f)
             self.__dic['child'].append(c)
             self.__dic['chromosomeFitFather'].append(chro)
          if(m[0] == c[0] or m[1] == c[0]):
             self.__dic['mother'].append(m)
             self.__dic['chromosomeFitMother'].append(chro)
         
          if(f[0] != c[0] and f[1] != c[0]):
            self.__dic['fatherNotSimilarRs'].append(r)
            self.__dic['notFather'].append(f)
            self.__dic['chFather'].append(c)
            self.__dic['chromosomeNotFitFather'].append(chro)
         
          if(m[0] != c[0] and m[1] != c[0]):
            self.__dic['motherNotSimilarRs'].append(r)
            self.__dic['notMother'].append(m)
            self.__dic['chMother'].append(c)
            self.__dic['chromosomeNotFitMother'].append(chro)
         
        '''1 2 1'''
        if(len(c) == 1 and len(f) == 2 and len(m) == 1):
          if(f[0] == c[0] or f[1] == c[0]):
             self.__dic['rsNumberSimilar'].append(r)
             self.__dic['father'].append(f)
             self.__dic['child'].append(c)
             self.__dic['chromosomeFitFather'].append(chro)
         
          if(m[0] == c[0]):
             self.__dic['mother'].append(m)
             self.__dic['chromosomeFitMother'].append(chro)
         
          if(f[0] != c[0] and f[1] != c[0]):
            self.__dic['fatherNotSimilarRs'].append(r)
            self.__dic['notFather'].append(f)
            self.__dic['chFather'].append(c)
            self.__dic['chromosomeNotFitFather'].append(chro)
          
          if(m[0] != c[0]):
            self.__dic['motherNotSimilarRs'].append(r)
            self.__dic['notMother'].append(m)
            self.__dic['chMother'].append(c)
            self.__dic['chromosomeNotFitMother'].append(chro)
             
          '''1 1 2'''
        if(len(c) == 1 and len(f) == 1 and len(m) == 2):
          if(f[0] == c[0]):
             self.__dic['rsNumberSimilar'].append(r)
             self.__dic['father'].append(f)
             self.__dic['child'].append(c)
             self.__dic['chromosomeFitFather'].append(chro)
         
          if(m[0] == c[0] or m[1] == c[0]):
             self.__dic['mother'].append(m)
             self.__dic['chromosomeFitMother'].append(chro)
         
          if(f[0] != c[0]):
            self.__dic['fatherNotSimilarRs'].append(r)
            self.__dic['notFather'].append(f)
            self.__dic['chFather'].append(c)
            self.__dic['chromosomeNotFitFather'].append(chro)
         
          if(m[0] != c[0] and m[1] != c[0]):
            self.__dic['motherNotSimilarRs'].append(r)
            self.__dic['notMother'].append(m)
            self.__dic['chMother'].append(c)
            self.__dic['chromosomeNotFitMother'].append(chro)
              
      
        '''1 1 1'''
        if(len(c) == 1 and len(f) == 1 and len(m) == 1): 
          if(f[0] == c[0]):
             self.__dic['rsNumberSimilar'].append(r)
             self.__dic['father'].append(f)
             self.__dic['child'].append(c)
             self.__dic['chromosomeFitFather'].append(chro)
         
          if(m[0] == c[0]):
             self.__dic['mother'].append(m)
             self.__dic['chromosomeFitMother'].append(chro)
         
          if(f[0] != c[0]):
            self.__dic['fatherNotSimilarRs'].append(r)
            self.__dic['notFather'].append(f)
            self.__dic['chFather'].append(c)
            self.__dic['chromosomeNotFitFather'].append(chro)
         
          if(m[0] != c[0]):
            self.__dic['motherNotSimilarRs'].append(r)
            self.__dic['notMother'].append(m)
            self.__dic['chMother'].append(c)
            self.__dic['chromosomeNotFitMother'].append(chro)
         
      else:
         print('Error')

  def getPaternityTest(self):
     return self.__dic


  '''Calculate prob Father'''
  def calculateProbability(self):
        sumSimilar = len(self.getPaternityTest()['rsNumberSimilar'])
        total = (len(self.getPaternityTest()['rsNumberSimilar'])+ len(self.getPaternityTest()['fatherNotSimilarRs']))
        sumNotSimilar = len(self.getPaternityTest()['fatherNotSimilarRs'])
        rule = sumSimilar / total
        ruleNotSimilar = sumNotSimilar / total
        return rule * 100, ruleNotSimilar * 100 
