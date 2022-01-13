
import pandas as pd
data = pd.read_csv('data.csv')

rsNumbers = []
fatherAle = []
motherAle = []
childAle1 = []
childAle2 = []
childAle3 = []

rsSimilar = []
fatherSimilar = []
motherSimilar = []
childSimilar1 = []
childSimilar2 = []
childSimilar3 = []

def check(father, mother, child1, child2, child3):
  for i, j, ch1, ch2, ch3, x in zip(father, mother, child1, child2, child3, range(len(data['combine']))):
    if(
      (ch1[0] == i[0] or ch1[0] == i[1] or ch1[1] == i[0] or ch1[1] == i[1]) 
      and
      (ch1[0] == j[0] or ch1[0] == j[1] or ch1[1] == j[0] or ch1[1] == j[1])):
      childSimilar1.append(ch1)

    if(
      (ch2[0] == i[0] or ch2[0] == i[1] or ch2[1] == i[0] or ch2[1] == i[1]) 
      and
      (ch2[0] == j[0] or ch2[0] == j[1] or ch2[1] == j[0] or ch2[1] == j[1])):
      childSimilar2.append(ch2)
    
    if(
      (ch3[0] == i[0] or ch3[0] == i[1] or ch3[1] == i[0] or ch3[1] == i[1]) 
      and
      (ch3[0] == j[0] or ch3[0] == j[1] or ch3[1] == j[0] or ch3[1] == j[1])):
      childSimilar3.append(ch3)

    if(
      (not(ch1[0] == i[0] or ch1[0] == i[1] or ch1[1] == i[0] or ch1[1] == i[1]) and (ch1[0] == j[0] or ch1[0] == j[1] or ch1[1] == j[0] or ch1[1] == j[1])
      )or
    not
    (ch2[0] == i[0] or ch2[0] == i[1] or ch2[1] == i[0] or ch2[1] == i[1]) and (ch2[0] == j[0] or ch2[0] == j[1] or ch2[1] == j[0] or ch2[1] == j[1]) 
    or 
    not(ch3[0] == i[0] or ch3[0] == i[1] or ch3[1] == i[0] or ch3[1] == i[1]) and (ch3[0] == j[0] or ch3[0] == j[1] or ch3[1] == j[0] or ch3[1] == j[1])
    ):
      rsNumbers.append(data['combine'][x])
      fatherAle.append(i)
      motherAle.append(j)
      childAle1.append(ch1)
      childAle2.append(ch2)
      childAle3.append(ch3)
    
    rsSimilar.append(data['combine'][x])
    fatherSimilar.append(i)
    motherSimilar.append(j)
     
        
 
       
f = []
m = []
c1 = []
c2 = []
c3= []
singleFather = []
singleMother = []
singleChild1 = []
singleChild2 = []
singleChild3 = []

for i,x in zip(data['father'], range(len(data['father']))):
 if(len(data['father'][x]) == 1):
   singleFather.append(data['father'][x])
 else:
  f.append(i)
for i,x in zip(data['mother'], range(len(data['mother']))):
 if(len(data['mother'][x]) == 1):
   singleMother.append(data['mother'][x])
 else:
  m.append(i)
for i,x in zip(data['child1'], range(len(data['child1']))):
  if(len(data['child1'][x]) == 1):
   singleChild1.append(data['child1'][x])
  else:
   c1.append(i)
for i,x in zip(data['child2'], range(len(data['child2']))):
  if(len(data['child2'][x]) == 1):
   singleChild2.append(data['child2'][x])
  else:
    c2.append(i)
for i,x in zip(data['child3'], range(len(data['child3']))):
  if(len(data['child3'][x]) == 1):
   singleChild3.append(data['child3'][x])
  else:
    c3.append(i)

#print('Father: ', f)
#print('Mother: ', m)
#print('Child 1 : ', c1)
#print('Child 2 : ', c2)
#print('Child 3 : ', c3)
check(f, m, c1, c2, c3)
print('rs Numbers: ', rsSimilar[0:5])
print('Father: ', fatherSimilar[0:5])
print('Mother: ', motherSimilar[0:5])
print('Child 1: ', childSimilar1[0:5])
print('Child 2: ', childSimilar2[0:5])
print('Child 3: ', childSimilar3[0:5])

print('\n\nThere are Alleles not matched in data\n\n')
print('rs Numbers: ', rsNumbers[0:5])
print('Father: ', fatherAle[0:5])
print('Mother: ', motherAle[0:5])
print('Child 1: ', childAle1[0:5])
print('Child 2: ', childAle2[0:5])
print('Child 3: ', childAle3[0:5])
     
