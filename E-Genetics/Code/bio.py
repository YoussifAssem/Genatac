from Bio import SeqIO

from dna import ProcessFile 

class Whole:
  def getSequence(self):
      return ProcessFile()
  def runAlgorithm(self, name):
    f= open("23.txt","w+")
    for record in SeqIO.parse(name, "fasta"):
      for x in range(50):
        f.write(record.seq[x])

