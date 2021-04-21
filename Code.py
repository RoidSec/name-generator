import random

# Declare Variables
filename1 = "f1.txt"
filename2 = "f2.txt"


# Open each .txt file using a loop into a list(s) named wordList#. Strip the new lines from each word.
with open(filename1) as f1:
    wordList1 = [line.rstrip('\n') for line in f1]

with open(filename2) as f2:
    wordList2 = [line.rstrip('\n') for line in f2]


# Close the .txt files.
f1.close()
f2.close()


# Randomly select a index value in each list using the choice module within Random.
# Concatenate the string using a simple print statement. 
print(random.choice(wordList1) + "_" + random.choice(wordList2))
