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
   
  def check(self, father, mother, child, rs):
    for f, m, c, r in zip(father, mother, child, rs):
        '''2 2 2'''
        if(len(c) == 2 and len(f) == 2 and len(m) == 2): 
          if(f[0] == c[0] or f[0] == c[1] or f[1] == c[0] or f[1] == c[1]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
          if(m[0] == c[0] or m[0] == c[1] or m[1] == c[0] or m[1] == c[1]):
             self.motherSimilar.append(m)
          
          if(f[0] != c[0] and f[0] != c[1] and f[1] != c[0] and f[1] != c[1]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
          if(m[0] != c[0] and m[0] != c[1] and m[1] != c[0] and m[1] != c[1]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)
           

            '''2 2 1'''
        if(len(c) == 2 and len(f) == 2 and len(m) == 1): 
          if(f[0] == c[0] or f[0] == c[1] or f[1] == c[0] or f[1] == c[1]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
          if(m[0] == c[0] or m[0] == c[1]):
             self.motherSimilar.append(m)
          
          if(f[0] != c[0] and f[0] != c[1] and f[1] != c[0] and f[1] != c[1]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)  
          if(m[0] != c[0] and m[0] != c[1]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)  

            '''2 1 2'''
        if(len(c) == 2 and len(f) == 1 and len(m) == 2): 
          if(f[0] == c[0] or f[0] == c[1]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
          if(m[0] == c[0] or m[0] == c[1] or m[1] == c[0] or m[1] == c[1]):
             self.motherSimilar.append(m)
          
          if(f[0] != c[0] and f[0] != c[1]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
          
          if(m[0] != c[0] and m[0] != c[1] and m[1] != c[0] and m[1] != c[1]):
            self.rsNumbersMother.append(m)
            self.mo.append(m)
            self.chMother.append(c)
                 
          '''2 1 1'''
        if(len(c) == 2 and len(f) == 1 and len(m) == 1): 
          if(f[0] == c[0] or f[0] == c[1]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
          if(m[0] == c[0] or m[0] == c[1]):
             self.motherSimilar.append(m)
          
          if(f[0] != c[0] and f[0] != c[1]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
          if(m[0] != c[0] and m[0] != c[1]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)        

        '''1 2 2'''
        if(len(c) == 1 and len(f) == 2 and len(m) == 2):
          if(f[0] == c[0] or f[1] == c[0]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
          if(m[0] == c[0] or m[1] == c[0]):
             self.motherSimilar.append(m)
          
          if(f[0] != c[0] and f[1] != c[0]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c) 
          if(m[0] != c[0] and m[1] != c[0]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)    
      
        '''1 2 1'''
        if(len(c) == 1 and len(f) == 2 and len(m) == 1):
          if(f[0] == c[0] or f[1] == c[0]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
          if(m[0] == c[0]):
             self.motherSimilar.append(m)
          
          if(f[0] != c[0] and f[1] != c[0]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c) 
          if(m[0] != c[0]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c) 
                
          '''1 1 2'''
        if(len(c) == 1 and len(f) == 1 and len(m) == 2):
          if(f[0] == c[0]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
          if(m[0] == c[0] or m[1] == c[0]):
             self.motherSimilar.append(m)
          
          if(f[0] != c[0]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
          if(m[0] != c[0] and m[1] != c[0]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)
                 
      
        '''1 1 1'''
        if(len(c) == 1 and len(f) == 1 and len(m) == 1): 
          if(f[0] == c[0]):
             self.rsNumberSimilar.append(r)
             self.fatherSimilar.append(f)
             self.childSimilar.append(c)
          if(m[0] == c[0]):
             self.motherSimilar.append(m)
          
          if(f[0] != c[0]):
            self.rsNumbersFather.append(r)
            self.fa.append(f)
            self.chFather.append(c)
          if(m[0] != c[0]):
            self.rsNumbersMother.append(r)
            self.mo.append(m)
            self.chMother.append(c)
    return self.rsNumberSimilar, self.fatherSimilar, self.motherSimilar, self.childSimilar, self.rsNumbersFather, self.rsNumbersMother, self.fa, self.mo, self.chFather, self.chMother                   
      
      