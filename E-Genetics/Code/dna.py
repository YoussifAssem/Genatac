import csv
from itertools import count
import sys


def ProcessFile():
   
 
   ## if len(sys.argv) != 3:
     ##   print("Usage: python data.csv sequence.txt")
       ## sys.exit()

    data = csv.DictReader(open("large.csv"))

    dna_file = "23.txt"
    with open(dna_file) as f:
        sequence = f.read()

 
    counts = {}


    str_keys = data.fieldnames[1:]

    for sub_str in str_keys:
        counts[sub_str] = max_consecutive_matches(sequence, sub_str)


    for row in data:
        extracted_db_row = [int(row[sub_str]) for sub_str in counts]
        target = [int(counts[sub_str]) for sub_str in counts]

       
        if target == extracted_db_row:
            #print(row['name'])
           return 


    ##print("No match")
    return counts
   

def max_consecutive_matches(sequence, sub_str):
    match_counter = 0
    length = len(sub_str)

    for i in range(len(sequence)):
        count = 0 
        while True: 
            start = i + length * count
            end = start + length
            if sequence[start:end] == sub_str:
                count += 1
            else:

                break
        if count > match_counter:
            match_counter = count

    return match_counter


