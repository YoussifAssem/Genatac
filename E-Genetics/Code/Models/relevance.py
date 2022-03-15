from heapq import merge
from os import remove
from numpy import empty
import pandas as pd
class Relevance:
   __dic = {
        'childIDSimilar': [],
        'childIDNotSimilarFather': [],
        'childIDNotSimilarMother': [],
        'rsSimilar':[],
        'rsNotSimilarFather':[],
        'rsNotSimilarMother':[],
        'Father': [],
        'Mother': [],
        'Child': [],
        'fatherNotSimilar':[],
        'motherNotSimilar':[],
        'childNotSimilar':[],
    }

   def __checkSimilar(self, similarID, notSimilarFather, notSimilarMother):
    for s in similarID:
        for nF in notSimilarFather:
            if(s == nF):
                similarID.remove(s)

    for s in similarID:
        for nM in notSimilarMother:
            if(s == nM):
                similarID.remove(s)
    return similarID    
   
   def getRelevances(self):
       return self.__dic
   
   def checkRelevances(self, merged):
    for j, rs, family, newChild in zip(range(len(merged['ID'])), range(len(merged['rs'])), range(len(merged['family'])), range(len(merged['newChild']))):
     father = str(merged['family'][family]).split('|')[0]
     mother = str(merged['family'][family]).split('|')[1]
     for i in range(len(merged['newChild'][newChild])):  
      child = str(merged['newChild'][newChild][i]).replace('|','') 
      childID = merged['ID'][j]  
     if((father[0] == child[0] or father[0] == child[1] or father[1] == child[0] or father[1] == child[1]) and mother[0] == child[0] or mother[0] == child[1] or mother[1] == child[0] or mother[1] == child[1]):
        self.__dic['rsSimilar'].append(merged['rs'][rs])
        self.__dic['Father'].append(father)
        self.__dic['Child'].append(child)
        self.__dic['Mother'].append(mother) 
        self.__dic['childIDSimilar'].append(childID)
    
     elif(father[0] != child[0] and father[0] != child[1] and father[1] != child[0] and father[1] != child[1]):    
        self.__dic['rsNotSimilarFather'].append(merged['rs'][rs])
        self.__dic['fatherNotSimilar'].append(father)
        self.__dic['childNotSimilar'].append(child)
        self.__dic['childIDNotSimilarFather'].append(childID)
        
     elif(mother[0] != child[0] and mother[0] != child[1] and mother[1] != child[0] and mother[1] != child[1]):    
        self.__dic['rsNotSimilarMother'].append(merged['rs'][rs])
        self.__dic['motherNotSimilar'].append(father)
        self.__dic['childNotSimilar'].append(child)
        self.__dic['childIDNotSimilarMother'].append(childID)
      
    self.__dic['childIDSimilar'] = list(dict.fromkeys(self.__dic['childIDSimilar']))
    self.__dic['childIDNotSimilarFather'] = list(dict.fromkeys(self.__dic['childIDNotSimilarFather']))
    self.__dic['childIDNotSimilarMother'] = list(dict.fromkeys(self.__dic['childIDNotSimilarMother']))
    self.__dic['rsSimilar'] = list(dict.fromkeys(self.__dic['rsSimilar']))
    self.__dic['rsNotSimilarFather'] = list(dict.fromkeys(self.__dic['rsNotSimilarFather']))
    self.__dic['rsNotSimilarMother'] = list(dict.fromkeys(self.__dic['rsNotSimilarMother']))
    
    self.__dic['childIDSimilar'] = self.__checkSimilar(self.__dic['childIDSimilar'], self.__dic['childIDNotSimilarFather'], self.__dic['childIDNotSimilarMother'])   
    self.__dic['rsSimilar'] = self.__checkSimilar(self.__dic['rsSimilar'], self.__dic['rsNotSimilarFather'], self.__dic['rsNotSimilarMother'])
    

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
print('ID NOT Similar Father', dic['childIDNotSimilarFather'][0:5])
print('ID NOT Similar Mother', dic['childIDNotSimilarMother'][0:5])
print('Rs Numbers Similar', dic['rsSimilar'][0:5])
print('Rs Numbers NOT Similar Father', dic['rsNotSimilarFather'][0:5])
print('Rs Numbers NOT Similar Mother', dic['rsNotSimilarMother'][0:5])
print('Alleles Father', dic['Father'][0:5])
print('Alleles Mother', dic['Mother'][0:5])
print('Alleles Child', dic['Child'][0:5])
print('Alleles Child NOT Similar', dic['childNotSimilar'][0:5])
    
    
