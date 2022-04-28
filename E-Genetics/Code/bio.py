#from ast import For
#from msilib import sequence
from difflib import SequenceMatcher

from typing import Pattern
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from dna import ProcessFile
class Whole:
  def runAlgorithm(self, fileName):
    f= open("23.txt","w+")


    for record in SeqIO.parse(fileName, "fasta"):
      for x in range(60):
          f.write(record.seq[x])

    #f1= open("21.txt","w+")


    #for record in SeqIO.parse("GCA_001292825.2_HS1011_v1.1_genomic.fna", "fasta"):
      
      
     # for y in range(60):
      #    f1.write(record.seq[y])
    
  def getSequence(self):
    return ProcessFile()      
#li = []

#with open('23.txt') as f:
#    li.append(f.readlines())


##Text='TTTT'


##def PATTERNCOUNT (Text, Pattern) :
##    count=0
  ##  Location={}
  ##  for i in range (0, len(Text) - len (Pattern) + 1):
   ##     if Text[i:len (Pattern)+i]  == Pattern:
    ##        Location[count]=i
##            count= count + 1
            
##    return count , Location    
     
##print(PATTERNCOUNT(Text,li)[0])
##print(PATTERNCOUNT(Text,li)[1])   


 ##     print(record.len)

  ##     seq = sequence(open("23.txt","w+"))
    ##   feature = SeqFeature(FeatureLocation(5, 18), type="gene", strand=-1)
   ##    print(FeatureLocation())


##for x in range(len(record.seq)):
      ##print(len(seq.location)



#records = SeqIO.parse("daughter_1.fq", "fastq")
#count = SeqIO.write(records, "23.txt", "fasta")
#print("Converted %i records" % count)      
      
      


##my_snp = 100
##record = SeqIO.read("Homo_sapiens.EGYPT.dna.primary_assembly.fsa", "fasta")
##for feature in record.features:
##    if my_snp in feature:
##         print("%s %s" % (feature.type, feature.qualifiers.get("db_xref")))



##for record in SeqIO.parse("Homo_sapiens.EGYPT.dna.primary_assembly.fsa", "fasta"):
 ##li.append(record.seq)
##with open('23.txt') as f:
  ##  li.append(f.readlines())

    


##print(len(record.seq))

##for x in range(60):

##print(li[0])
##print(type(li))