
import hashlib
import firebase_admin
from firebase_admin import credentials, firestore


class User:
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

    def logIn(self, email, password):
        ref = self.__db.collection('Users').stream()
        for doc in ref:
           if(doc.to_dict()['email'] == email and doc.to_dict()['password'] == password):
                return True
        return False    

    def getResults(self, adminName, caseNumber, nationalNumber):
        nationalNumber = hashlib.sha256(nationalNumber.encode('utf-8')).hexdigest()
        caseNumber = hashlib.sha256(caseNumber.encode('utf-8')).hexdigest()
        ref = self.__db.collection('adminUsers').document(adminName).collection('Results').document(nationalNumber)  
        val = ref.get().to_dict()
        if(ref.get().exists):  
            if(val['ID'] == nationalNumber and val['caseNumber'] == caseNumber):
                return True, val['probabilityFather'], val['probabilityNotFather'], val['result'] 
            else:
                 return False, '', '', ''
        else:
              return False, '', '', ''

                       