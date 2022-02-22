from .paternityTest import paternityTest
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


class User:
    pT = object()
    def __init__(self):
      try:
         cred = credentials.Certificate("../../../paternitytest-7cb8b-firebase-adminsdk-my5mh-786350297b.json")
         firebase_admin.initialize_app(cred,  {'databaseURL': 'https://paternitytest-7cb8b-default-rtdb.firebaseio.com/'})
      except:
        print('Error')
    def Test(self, father, mother, child, rs, chromosome):
        self.pT = paternityTest(father, mother, child, rs, chromosome)
    
    def Registration(self, username_info, hashed_password):
       ref = db.reference('/Users')
       ref.push(
        {
         'userName': username_info,
         'password': hashed_password
         }
      
     )
     
    def saveResults(self, ID, probFather, probNotFather):
        ref = db.reference('/Results')
        ref.push(
          {
            'ID':ID,
            'probabilityFather': probFather,
            'probabilityNotFather':probNotFather
          }
        )
    def checkResults(self, ID):
       ref = db.reference('/Results')
       snapShot = ref.get()
       for key, val in snapShot.items():
         if(val.get('ID') == ID):
           return True 
    def logIn(self, userName, password):
      ref = db.reference('/Users')
      snapShot = ref.get()
      for key, val in snapShot.items():
        if(val.get('userName') == userName and val.get('password') == password):
            return True


    '''Similar rs numbers fit the rule'''
    def getRsNumberSimilar(self):
     return self.pT.getRsNumberSimilar()
    '''Alleles of father that fit the rule'''
    def getFatherSimilar(self):
     return self.pT.getFatherSimilar()
    '''Alleles of Mother that fit the rule'''
    def getMotherSimilar(self):
     return self.pT.getMotherSimilar()
    '''Alleles of Child that fit the rule'''
    def getChildSimilar(self):
     return self.pT.getChildSimilar()
    '''Rs Numbers of father does not fit the rule''' 
    def getRsNumberFather(self):
     return self.pT.getRsNumberFather()
    '''Rs Numbers of mother does not fit the rule''' 
    def getRsNumberMother(self):
     return self.pT.getRsNumberMother()
    '''Get Alleles of father does not fit the rule'''
    def getFatherNotSimilar(self):
     return self.pT.getFatherNotSimilar()
    '''Get Alleles of Mother does not fit the rule'''
    def getMotherNotSimilar(self):
     return self.pT.getMotherNotSimilar()
    '''Get Alleles of child does not fit the rule with father'''
    def getChildNotSimilarWithFather(self):
     return self.pT.getChildNotSimilarWithFather()
    '''Get Alleles of child does not fit the rule with Mother'''
    def getChildNotSimilarWithMother(self):
     return self.pT.getChildNotSimilarWithMother()
    '''Get Chromosomes Fit Father'''   
    def getChromosomesFitFather(self):
     return self.pT.getChromosomesFitFather()
    '''Get Chromosomes Fit Mother'''   
    def getChromosomesFitMother(self):
     return self.pT.getChromosomesFitMother()
    '''Get Chromosomes Not Fit Father'''   
    def getChromosomesNotFitFather(self):
     return self.pT.getChromosomesNotFitFather()
    '''Get Chromosomes Not Fit Mother'''   
    def getChromosomesNotFitMother(self):
     return self.pT.getChromosomesNotFitMother()
  
    '''Calculate prob Father'''
    def calculateProbability(self):
        return self.pT.calculateProbability()[0], self.pT.calculateProbability()[1]
        