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
      for ID,  family in zip(range(len(merged['ID'])),range(len(merged['family']))):
        father = str(merged['family'][family]).split('|')[0]
        mother = str(merged['family'][family]).split('|')[1]
        childID = merged['ID'][ID]  
        for rs, newChild in zip(range(len(merged['rs'])), range(len(merged['newChild']))):
            rsNumber = merged['rs'][rs]
            child = str(merged['newChild'][newChild]).replace('|','') 
            if(child[0] not in father and  child[1] not in father):
                print(rsNumber)
                print(child)
                print(father)
                print(childID)
                break
   
    #self.__dic['similarIDFather'] = self.checkSimilar(self.__dic['similarIDFather'], self.__dic['notSimilarIDFather'])
   # self.__dic['notSimilarIDFather'] = self.checkSimilar(self.__dic['notSimilarIDFather'], self.__dic['similarIDFather'])
 
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


for key in relevances['Sample (Male/Female/Unknown)']:
    merged['ID'].append(key)


for keyData in lsData:
    for keyRelevance in lsRelevance:
        if(keyData == keyRelevance):
           merged['rs'].append(keyRelevance)
           merged['family'].append(lsData[keyData])

relevances = relevances.drop('Sample (Male/Female/Unknown)', axis=1)
for keyData in lsData:
    for keyRelevance in lsRelevance:
        if(keyData == keyRelevance):
            for i, row in relevances.iterrows():
                merged['newChild'].append(row.values)


print(merged['ID'][0:10])
print(merged['rs'][0:10])
print(merged['family'][0:10])
print(merged['newChild'][0][0:10])
#relev = Relevance()   
#relev.checkRelevances(merged)
#dic = relev.getRelevances()
#print('ID Similar Father', dic['similarIDFather'])
#print('ID NOT Similar Father', dic['notSimilarIDFather'])

