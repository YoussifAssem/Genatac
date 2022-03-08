from xmlrpc.client import DateTime
from .paternityTest import paternityTest
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import sys
class User:
    __pT = object()
    __db = object()

    def __init__(self):
      try:
          cred = credentials.Certificate("../../../fireStore.json")
          firebase_admin.initialize_app(cred)
          self.connection()  
      except:
        print('Error')
    def connection(self):
        self.__db = firestore.client()
        
    def Test(self, father, mother, child, rs, chromosome):
        self.__pT = paternityTest(father, mother, child, rs, chromosome)
   
   
    def sendMessage(self, Sender, Receiver, Message):
      self.__db.collection('Chatting').add({
        'Sender': Sender,
        'Receiver': Receiver,
        'Message': Message,
        'Time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      })
    
    def getSenders(self):
      ref = self.__db.collection('Chatting').stream()
      li = []
      for doc in ref:
        if(doc.to_dict()['Receiver'] == sys.argv[1].replace(" ", "")):
          li.append(doc.to_dict()['Sender'])
      li = list(dict.fromkeys(li))
      return li
    
    
    def getSenderMessages(self, sender, receiver):
      ref = self.__db.collection('Chatting').stream()
      li = []
      for doc in ref:
          if (doc.to_dict()['Sender'] == sender and doc.to_dict()['Receiver'] == receiver):
            li.append(doc.to_dict()['Message'])
      return li
    
    def getReceiverMessages(self, receiver, sender):
      ref = self.__db.collection('Chatting').stream()
      li = []
      for doc in ref:
          if (doc.to_dict()['Sender'] == receiver and doc.to_dict()['Receiver'] == sender):
            li.append(doc.to_dict()['Message'])
      return li    
    def Registration(self, username_info, hashed_password):
        ref = self.__db.collection('adminUsers').document(username_info).get()
        if(ref.exists):
            return True 
        else:
              print('In Else')  
              self.__db.collection('adminUsers').document(username_info).set({
                 'userName': username_info,
                 'password': hashed_password
               })
              return False 
    
    def logIn(self, userName, password):
     if(self.__checkUser(userName=userName, password=password)):
       return True
     else:
       return False   

    def __checkUser(self, userName, password):
      if(userName == ''):
        return False
      else:
        docs = self.__db.collection('adminUsers').document(userName)
        val = docs.get().to_dict()
        if(docs.get().exists):  
         if(val['userName'] == userName and val['password'] == password):
            return True
         else:
          return False
        else:
          return False  

    def saveResults(self, ID, probFather, probNotFather, caseNumber, userName):
        if(self.__checkResults(ID, userName)):
          return True
        else:  
          ref = self.__db.collection('adminUsers').document(userName).collection('Results').document(ID)
          ref.set({
            'ID':ID,
            'caseNumber':caseNumber,
            'probabilityFather': probFather,
            'probabilityNotFather':probNotFather
          })
          return False
    def __checkResults(self, ID, userName):
       ref = self.__db.collection('adminUsers').document(userName).collection('Results').document(ID)
       if(ref.get().exists):
            return True
       else:
         return False 


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
        