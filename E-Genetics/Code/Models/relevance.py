from heapq import merge
from os import remove
from numpy import empty
import pandas as pd
class Relevance:
   __dic = {
        'childIDSimilar': [],
        'childIDNotSimilar': [],
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
       if(father[0] == child[0] or father[0] == child[1] or father[1] == child[0] or father[1] == child[1]):
        self.__dic['rsSimilar'].append(merged['rs'][rs])
        self.__dic['Father'].append(father)
        self.__dic['Child'].append(child)
        self.__dic['childIDSimilar'].append(childID)
       if(mother[0] == child[0] or mother[0] == child[1] or mother[1] == child[0] or mother[1] == child[1]):
        self.__dic['childIDSimilar'].append(childID)
        self.__dic['rsSimilar'].append(merged['rs'][rs])
        self.__dic['Child'].append(child)
        self.__dic['Mother'].append(mother) 
       
       else:
           if(father[0] != child[0] or father[0] != child[1] or father[1] != child[0] or father[1] != child[1]):    
            self.__dic['rsNotSimilar'].append(merged['rs'][rs])
            self.__dic['fatherNotSimilar'].append(father)
            self.__dic['childNotSimilar'].append(child)
            self.__dic['childIDNotSimilar'].append(childID)
            
           if(mother[0] != child[0] or mother[0] != child[1] or mother[1] != child[0] or mother[1] != child[1]):    
            self.__dic['rsNotSimilar'].append(merged['rs'][rs])
            self.__dic['motherNotSimilar'].append(father)
            self.__dic['childNotSimilar'].append(child)
            self.__dic['childIDNotSimilar'].append(childID)
        
    self.__dic['rsSimilar'] =list(dict.fromkeys(self.__dic['rsSimilar']))
    self.__dic['childIDSimilar'] =list(dict.fromkeys(self.__dic['childIDSimilar']))
    self.__dic['rsNotSimilar'] =list(dict.fromkeys(self.__dic['rsNotSimilar']))
    self.__dic['childIDNotSimilar'] =list(dict.fromkeys(self.__dic['childIDNotSimilar']))
    self.__dic['Father'] =list(dict.fromkeys(self.__dic['Father']))
    self.__dic['Mother'] =list(dict.fromkeys(self.__dic['Mother']))
    self.__dic['Child'] =list(dict.fromkeys(self.__dic['Child']))
    self.__dic['fatherNotSimilar'] =list(dict.fromkeys(self.__dic['fatherNotSimilar']))
    self.__dic['motherNotSimilar'] =list(dict.fromkeys(self.__dic['motherNotSimilar']))
    self.__dic['childNotSimilar'] =list(dict.fromkeys(self.__dic['childNotSimilar']))
    
    self.__dic['childIDSimilar'] = self.checkSimilar(self.__dic['childIDSimilar'], self.__dic['childIDNotSimilar'])
    self.__dic['childIDNotSimilar'] = self.checkSimilar(self.__dic['childIDNotSimilar'], self.__dic['childIDSimilar'])
    self.__dic['rsSimilar'] = self.checkSimilar(self.__dic['rsSimilar'], self.__dic['rsNotSimilar'])
    self.__dic['rsNotSimilar'] = self.checkSimilar(self.__dic['rsNotSimilar'], self.__dic['rsSimilar'])
  

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
print('ID Similar', dic['childIDSimilar'][0:5])
print('ID NOT Similar', dic['childIDNotSimilar'][0:5])
print('Rs Numbers Similar', dic['rsSimilar'][0:5])
print('Rs Numbers NOT Similar', dic['rsNotSimilar'][0:5])
print('Alleles Father', dic['Father'][0:5])
print('Alleles Mother', dic['Mother'][0:5])
print('Alleles Child', dic['Child'][0:5])
print('Alleles Father NOT Similar', dic['fatherNotSimilar'][0:5])
print('Alleles Mother NOT Similar', dic['motherNotSimilar'][0:5])
print('Alleles Child NOT Similar', dic['childNotSimilar'][0:5])
    
    
