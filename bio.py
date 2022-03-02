from ast import For
from Bio import SeqIO

f= open("23.txt","w+")


for record in SeqIO.parse("Homo_sapiens.EGYPT.dna.primary_assembly.fsa", "fasta"):
   ## print(record.seq[0])

   for x in range(30):
    f.write(record.seq[x])

     
