# Mohammad Qureshi
# PSID 1789301
# LAB 9.10



import csv

# INPUT FILE NAME
# OPEN FILE AND READ CONTENTS
input_file = input()
my_file = open(input_file,'r')
file_contents = csv.reader(my_file)

# CREATE A SET TO REMOVE DUPLICATES
# GO THROUGH THE FILE USING A NESTED FOR STATEMENT
# USING AN IF STATEMENT, CREATE A  COUNTER TO KEEP TRACK OF THE SET
freq = {}
for row in file_contents:
    for w in row:
        if w in freq.keys():
            freq[w] = freq[w] + 1
        else:
            freq[w] = 1

# GO THROUGH THE COMPLETED SET USING THE FOR STATEMENT
# PRINT EACH WORD AND IT'S COUNTER
for test in freq.keys():
    print(test, freq[test])