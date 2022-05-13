CounterTTTTM = 0
CounterAGATM = 0
CounterAATGM = 0
CounterTGCCM = 0
CounterGATAM = 0
CounterTATCM = 0
CounterAAGGM = 0
CounterAGAAM = 0

with open('dad.txt', 'r') as file:
       data = file.read().rstrip() 
       n = 4	# every 2 characters
split_string = [data[i:i+n] for i in range(0, len(data), n)]
#print(split_string)
for x in split_string:
    if x == "TTTT":
     CounterTTTTM = CounterTTTTM + 1
    if x == "AGAT":
     CounterAGATM = CounterAGATM + 1
    if x == "AATG":
     CounterAATGM = CounterAATGM + 1
    if x == "TGCC":
     CounterTGCCM = CounterTGCCM + 1
    if x == "GATA":
     CounterGATAM = CounterGATAM + 1
    if x == "TATC":
     CounterTATCM = CounterTATCM + 1
    if x == "AAGG":
     CounterAAGGM = CounterAAGGM + 1
    if x == "AGAA":
     CounterAGAAM = CounterAGAAM + 1
TTTT= "TTTT Occurrences: "
AGAT= "AGAT Occurrences: " 
AATG= "AATG Occurrences: " 
TGCC= "TGCC Occurrences: " 
GATA= "GATA Occurrences: " 
TATC= "TATC Occurrences: " 
AAGG= "AAGG Occurrences: " 
AGAA= "AGAA Occurrences: " 

print("Mom: ")
print(TTTT)
print(CounterTTTTM)
print(AGAT)
print(CounterAGATM)
print(AATG)
print(CounterAATGM)
print(TGCC)
print(CounterTGCCM)
print(GATA)
print(CounterGATAM)
print(TATC)
print(CounterTATCM)
print(AAGG)
print(CounterAAGGM)
print(AGAA)
print(CounterAGAAM)
print("#############################")
CounterTTTT = 0
CounterAGAT = 0
CounterAATG = 0
CounterTGCC = 0
CounterGATA = 0
CounterTATC = 0
CounterAAGG = 0
CounterAGAA = 0
with open('dau.txt', 'r') as file:
       data = file.read().rstrip() 
       n = 4	# every 2 characters
split_string = [data[i:i+n] for i in range(0, len(data), n)]
#print(split_string)
for x in split_string:
    if x == "TTTT":
     CounterTTTT = CounterTTTT + 1
    if x == "AGAT":
     CounterAGAT = CounterAGAT + 1
    if x == "AATG":
     CounterAATG = CounterAATG + 1
    if x == "TGCC":
     CounterTGCC = CounterTGCC + 1
    if x == "GATA":
     CounterGATA = CounterGATA + 1
    if x == "TATC":
     CounterTATC = CounterTATC + 1
    if x == "AAGG":
     CounterAAGG = CounterAAGG + 1
    if x == "AGAA":
     CounterAGAA = CounterAGAA + 1
TTTT= "TTTT Occurrences: "
AGAT= "AGAT Occurrences: " 
AATG= "AATG Occurrences: " 
TGCC= "TGCC Occurrences: " 
GATA= "GATA Occurrences: " 
TATC= "TATC Occurrences: " 
AAGG= "AAGG Occurrences: " 
AGAA= "AGAA Occurrences: " 

print("Father: ")
print(TTTT)
print(CounterTTTT)
print(AGAT)
print(CounterAGAT)
print(AATG)
print(CounterAATG)
print(TGCC)
print(CounterTGCC)
print(GATA)
print(CounterGATA)
print(TATC)
print(CounterTATC)
print(AAGG)
print(CounterAAGG)
print(AGAA)
print(CounterAGAA)
print("#############################")


if CounterTTTT == CounterTTTTM:
       print("Match")
else :
       print("No Match")
if CounterAGAT == CounterAGATM:
       print("Match")   
else :
       print("No Match")           
if CounterAATG == CounterAATGM:
       print("Match")   
else :
       print("No Match")          
if CounterTGCC == CounterTGCCM:
       print("Match")       
else :
       print("No Match")
if CounterGATA == CounterGATAM:
       print("Match")        
else :
       print("No Match")
if CounterTATC == CounterTATCM:
       print("Match")
else :
       print("No Match")
if CounterAAGG == CounterAAGGM:
       print("Match")       
else :
       print("No Match")
if CounterAGAA == CounterAGAAM:
       print("Match")       
else :
       print("No Match")       