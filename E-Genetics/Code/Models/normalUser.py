
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