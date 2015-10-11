import csv
import json



files = {1: '../data/train.csv',
	 2: '../data/test.csv',
	 3: '../data/store.csv',
	 4: '../data/sample_submission.csv'
	}

for i in files:
    print(str(i) + ': ' + files[i])

fnumber = input('Enter file number from above: ')
fname = files[fnumber]

csvreader = csv.DictReader(open(fname))

data = {}

i = 0
for row in csvreader:
    if i < 1:
        header = row.keys()
        i += 1
    for h in header:
        if h not in data:
            data[h] = [row[h]]
        else:
            data[h].append(row[h])

json.dump(data, open(fname[0:-4]+'.json', 'w'), indent = 4)

for h in data:
    print(h + ': ' + str(data[h][1:5]))



