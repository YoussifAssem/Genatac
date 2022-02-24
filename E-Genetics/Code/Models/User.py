from tracemalloc import Snapshot
from .paternityTest import paternityTest
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


class User:
    __pT = object()
    def __init__(self):
      try:
         cred = credentials.Certificate("../../../paternitytest-7cb8b-firebase-adminsdk-my5mh-786350297b.json")
         firebase_admin.initialize_app(cred,  {'databaseURL': 'https://paternitytest-7cb8b-default-rtdb.firebaseio.com/'})
      except:
        print('Error')
    def Test(self, father, mother, child, rs, chromosome):
        self.__pT = paternityTest(father, mother, child, rs, chromosome)
    
    def Registration(self, username_info, hashed_password):
       ref = db.reference('/Users')
       snapShot = ref.get()
       for key, val in snapShot.items():
          if(val.get('userName') == username_info):
            return False
          else:  
               ref.push({
                'userName': username_info,
                'password': hashed_password
                })
               return True  
   
     
    def saveResults(self, ID, probFather, probNotFather, caseNumber):
        ref = db.reference('/Results')
        ref.push(
          {
            'ID':ID,
            'caseNumber':caseNumber,
            'probabilityFather': probFather,
            'probabilityNotFather':probNotFather
          }
        )
    def checkResults(self, ID, caseNumber):
       ref = db.reference('/Results')
       snapShot = ref.get()
       for key, val in snapShot.items():
         if(val.get('ID') == ID):
           return True 
         if(val.get('caseNumber') == caseNumber):
           return True  
    def logIn(self, userName, password):
      ref = db.reference('/Users')
      snapShot = ref.get()
      for key, val in snapShot.items():
        if(val.get('userName') == userName and val.get('password') == password):
            return True


    '''Similar rs numbers fit the rule'''
    def getRsNumberSimilar(self):
     return self.__pT.getRsNumberSimilar()
    '''Alleles of father that fit the rule'''
    def getFatherSimilar(self):
     return self.__pT.getFatherSimilar()
    '''Alleles of Mother that fit the rule'''
    def getMotherSimilar(self):
     return self.__pT.getMotherSimilar()
    '''Alleles of Child that fit the rule'''
    def getChildSimilar(self):
     return self.__pT.getChildSimilar()
    '''Rs Numbers of father does not fit the rule''' 
    def getRsNumberFather(self):
     return self.__pT.getRsNumberFather()
    '''Rs Numbers of mother does not fit the rule''' 
    def getRsNumberMother(self):
     return self.__pT.getRsNumberMother()
    '''Get Alleles of father does not fit the rule'''
    def getFatherNotSimilar(self):
     return self.__pT.getFatherNotSimilar()
    '''Get Alleles of Mother does not fit the rule'''
    def getMotherNotSimilar(self):
     return self.__pT.getMotherNotSimilar()
    '''Get Alleles of child does not fit the rule with father'''
    def getChildNotSimilarWithFather(self):
     return self.__pT.getChildNotSimilarWithFather()
    '''Get Alleles of child does not fit the rule with Mother'''
    def getChildNotSimilarWithMother(self):
     return self.__pT.getChildNotSimilarWithMother()
    '''Get Chromosomes Fit Father'''   
    def getChromosomesFitFather(self):
     return self.__pT.getChromosomesFitFather()
    '''Get Chromosomes Fit Mother'''   
    def getChromosomesFitMother(self):
     return self.__pT.getChromosomesFitMother()
    '''Get Chromosomes Not Fit Father'''   
    def getChromosomesNotFitFather(self):
     return self.__pT.getChromosomesNotFitFather()
    '''Get Chromosomes Not Fit Mother'''   
    def getChromosomesNotFitMother(self):
     return self.__pT.getChromosomesNotFitMother()
  
    '''Calculate prob Father'''
    def calculateProbability(self):
        return self.__pT.calculateProbability()[0], self.__pT.calculateProbability()[1]
        