from ast import For
from Bio import SeqIO

f= open("23.txt","w+")


for record in SeqIO.parse("GCA_001292825.2_HS1011_v1.1_genomic.fna", "fasta"):
  
   for x in range(60):
      
    f.write(record.seq[x])

from dna import ProcessFile 
ProcessFile()