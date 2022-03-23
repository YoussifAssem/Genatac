from heapq import merge
from os import remove
from numpy import empty
import pandas as pd
class Relevance:
   __dic = {
       'similarIDFather': [],
       'similarIDMother': [],
       'notSimilarIDFather': [],
       'notSimilarIDMother': [],
       
       'rsSimilar':[],
       'rsNotSimilar':[],
       'Father': [],
       'Mother': [],
       'Child': [],
       'fatherNotSimilar':[],
       'motherNotSimilar':[],
       'childNotSimilar':[],
    }

   def getRelevances(self):
       return self.__dic
   def checkSimilar(self, similar, notSimilar):
       for i in similar:
           for j in notSimilar:
               if(i == j):
                   similar.remove(j)
       return similar


   def checkRelevances(self, merged):
    for j, rs, family, newChild in zip(range(len(merged['ID'])), range(len(merged['rs'])), range(len(merged['family'])), range(len(merged['newChild']))):
      father = str(merged['family'][family]).split('|')[0]
      mother = str(merged['family'][family]).split('|')[1]
      for i in range(len(merged['newChild'][newChild])):
       child = str(merged['newChild'][newChild][i]).replace('|','') 
       childID = merged['ID'][j]  
       if(father[0] == child[0] or 
           father[0] == child[1] or 
           father[1] == child[0] or 
           father[1] == child[1]):
        self.__dic['similarIDFather'].append(childID)
        #self.__dic['rsSimilar'].append(merged['rs'][rs])
        #self.__dic['Father'].append(father)
        #self.__dic['Mother'].append(mother) 
        #self.__dic['Child'].append(child)
     #  if(mother[0] == child[0] or 
      #     mother[0] == child[1] or 
       #    mother[1] == child[0] or 
        #   mother[1] == child[1]):
         #  self.__dic['similarIDMother'].append(childID)
        #self.__dic['similarID'].append(childID)
        #self.__dic['rsSimilar'].append(merged['rs'][rs])
        #self.__dic['Mother'].append(mother) 
        #self.__dic['Child'].append(child)
       if(father[0] != child[0] and 
               father[0] != child[1] and 
               father[1] != child[0] and 
               father[1] != child[1]):    
            self.__dic['notSimilarIDFather'].append(childID)
            if(childID in self.__dic['similarIDFather']): 
                self.__dic['similarIDFather'].remove(childID)
            #self.__dic['rsNotSimilar'].append(merged['rs'][rs])
            #self.__dic['fatherNotSimilar'].append(father)
         #  if (mother[0] != child[0] and 
          #      mother[0] != child[1] and 
           #     mother[1] != child[0] and 
            #    mother[1] != child[1]):
             #   self.__dic['notSimilarIDMother'].append(childID)
            #self.__dic['motherNotSimilar'].append(father)
            #self.__dic['childNotSimilar'].append(child)
          
    self.__dic['similarIDFather'] =list(dict.fromkeys(self.__dic['similarIDFather']))
    self.__dic['notSimilarIDFather'] =list(dict.fromkeys(self.__dic['notSimilarIDFather']))
   # self.__dic['similarIDMother'] =list(dict.fromkeys(self.__dic['similarIDMother']))
   # self.__dic['notSimilarIDMother'] =list(dict.fromkeys(self.__dic['notSimilarIDMother']))
    
    #self.__dic['rsSimilar'] =list(dict.fromkeys(self.__dic['rsSimilar']))
    #self.__dic['rsNotSimilar'] =list(dict.fromkeys(self.__dic['rsNotSimilar']))
    
   # self.__dic['Father'] =list(dict.fromkeys(self.__dic['Father']))
    #self.__dic['Mother'] =list(dict.fromkeys(self.__dic['Mother']))
    #self.__dic['Child'] =list(dict.fromkeys(self.__dic['Child']))
    #self.__dic['fatherNotSimilar'] =list(dict.fromkeys(self.__dic['fatherNotSimilar']))
    #self.__dic['motherNotSimilar'] =list(dict.fromkeys(self.__dic['motherNotSimilar']))
    #self.__dic['childNotSimilar'] =list(dict.fromkeys(self.__dic['childNotSimilar']))
  
    #self.__dic['rsSimilar'] = self.checkSimilar(self.__dic['rsSimilar'], self.__dic['rsNotSimilar'])
    #self.__dic['rsNotSimilar'] = self.checkSimilar(self.__dic['rsNotSimilar'], self.__dic['rsSimilar'])
    self.__dic['similarIDFather'] = self.checkSimilar(self.__dic['similarIDFather'], self.__dic['notSimilarIDFather'])
    self.__dic['notSimilarIDFather'] = self.checkSimilar(self.__dic['notSimilarIDFather'], self.__dic['similarIDFather'])
   # self.__dic['similarIDMother'] = self.checkSimilar(self.__dic['similarIDMother'], self.__dic['notSimilarIDMother'])
    #self.__dic['notSimilarIDMother'] = self.checkSimilar(self.__dic['notSimilarIDMother'], self.__dic['similarIDMother'])
    
relevances = pd.read_csv('../DataSets/PaternityTest/relevanceRsNumbers.csv')
data = pd.read_csv('../DataSets/PaternityTest/data.csv')
lsRelevance = {}
lsData = {}
merged = {
    'ID': [],
    'rs': [],
    'family': [],
    'newChild': [],

}
for colName, colData in relevances.iteritems():
    lsRelevance[colName] = colData

for rs, fa, mo in zip(data['combine'], data['father'], data['mother']):
    lsData[rs] = fa + '|' + mo
  
for keyData in lsData:
    for keyRelevance in lsRelevance:
        if(keyData == keyRelevance):
           merged['rs'].append(keyRelevance)
           merged['family'].append(lsData[keyData])
           merged['newChild'].append(lsRelevance[keyRelevance])


for key in relevances['Sample (Male/Female/Unknown)']:
    merged['ID'].append(key)


relev = Relevance()   
relev.checkRelevances(merged)
dic = relev.getRelevances()
print('ID Similar Father', dic['similarIDFather'])
print('ID Similar Mother', dic['similarIDMother'])
print('ID NOT Similar Father', dic['notSimilarIDFather'])
print('ID NOT Similar Mother', dic['notSimilarIDMother'])

#print('Rs Numbers Similar', dic['rsSimilar'][0:5])
#print('Rs Numbers NOT Similar', dic['rsNotSimilar'][0:5])
print('Alleles Father', dic['Father'][0:5])
print('Alleles Mother', dic['Mother'][0:5])
print('Alleles Child', dic['Child'][0:5])
print('Alleles Father NOT Similar', dic['fatherNotSimilar'][0:5])
print('Alleles Mother NOT Similar', dic['motherNotSimilar'][0:5])
print('Alleles Child NOT Similar', dic['childNotSimilar'][0:5])
    
    
