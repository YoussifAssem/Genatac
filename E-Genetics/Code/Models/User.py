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
          if(probFather > probNotFather):
            ref.set({
              'ID':ID,
              'caseNumber':caseNumber,
              'probabilityFather': probFather,
              'probabilityNotFather':probNotFather,
              'result':'So, This child is related to this Father'
          })
          else:
              ref.set({
              'ID':ID,
              'caseNumber':caseNumber,
              'probabilityFather': probFather,
              'probabilityNotFather':probNotFather,
              'result':'So, This child is NOT related to this Father'
          })
          return False
    def __checkResults(self, ID, userName):
       ref = self.__db.collection('adminUsers').document(userName).collection('Results').document(ID)
       if(ref.get().exists):
            return True
       else:
         return False 

    def getPaternityResults(self):
      return self.__pT.getPaternityTest()
  
  
  
     
    '''Calculate prob Father'''
    def calculateProbability(self):
        return self.__pT.calculateProbability()[0], self.__pT.calculateProbability()[1]
        