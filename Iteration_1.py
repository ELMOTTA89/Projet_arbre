import csv
Lines=[]
filename='trees.csv'
with open (filename,newline='') as csvfile:
    csvreader=csv.reader(csvfile)

    for row in csvreader:
        Lines.append(row)
    

print(Lines[0],"\n",Lines[1])

