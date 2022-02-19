import mysql.connector
from .paternityTest import paternityTest
class User:
    pT = object()
    def Test(self, father, mother, child, rs, chromosome):
        self.pT = paternityTest(father, mother, child, rs, chromosome)
    
    def InsertData(self, username_info, hashed_password):
     conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="paternityTest")
     myCursor = conn.cursor()
     myCursor.execute("INSERT INTO Users (userName, password) VALUES (%s, %s)", (str(username_info), str(hashed_password)))
     conn.commit()
     conn.close()
    
    def readData(self, userName, password):
      conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="paternityTest")
      myCursor = conn.cursor()
      myCursor.execute("SELECT * FROM Users")
      records = myCursor.fetchall()
      for f in records:
        if(userName in f and password in f):
            return True
      conn.commit()
      conn.close()


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
        