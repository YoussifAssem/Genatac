import pandas as pd
class Relevance: 
  _done = {
    'similarID': [],
    'notSimilarID': [],
  }
  _relevances = object()
  def __init__(self, relevances):
       self._relevances = relevances
       self._runRelevances()

  def _checkSimilar(self, similar, notSimilar):
         for j in range(len(notSimilar)):
                if(notSimilar[j] in similar):
                   similar.remove(notSimilar[j])
         return similar
  
  def _runRelevances(self):  
    father = self._relevances.iloc[0]
    father.pop('ID')
    father = father.values    
    for i in range(len(self._relevances)):
      if(i == 0 or i == 1):
        i += 1
      else:      
        child = self._relevances.iloc[i]
        id = child.pop('ID')
        child = child.values
        for fa, ch in zip(range(len(father)), range(len(child))):
            chil = str(child[ch]).replace('|', '')
            if(father[fa][0] == chil[0] or 
               father[fa][0] == chil[1] or
               father[fa][1] == chil[0] or
               father[fa][1] == chil[1]):
                    self._done['similarID'].append(id)
            elif(father[fa][0] != chil[0] and 
                 father[fa][0] != chil[1] and
                 father[fa][1] != chil[0] and
                 father[fa][1] != chil[1]):
                        self._done['notSimilarID'].append(id)
    
    self._done['similarID'] = list(dict.fromkeys(self._done['similarID']))
    self._done['notSimilarID'] = list(dict.fromkeys(self._done['notSimilarID']))
    self._done['similarID'] = self._checkSimilar(self._done['similarID'], self._done['notSimilarID'])
  
  def getDone(self):
      return self._done  
  
relevances = pd.read_csv('../DataSets/PaternityTest/relevance.csv')
obj = Relevance(relevances)
done = obj.getDone()   
print('Similar ID', done['similarID'][0:5])
print('NOT Similar ID', done['notSimilarID'][0:5])

print('No of people Related to this Family', len(done['similarID']))
print('No of people is Not Related to this Family', len(done['notSimilarID']))
