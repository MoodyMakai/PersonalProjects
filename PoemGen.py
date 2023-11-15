import csv
import random
rows = []
lines = []
def form():
    with open('/Users/makaimoody-broen/Downloads/kaggle_poem_dataset.csv','r') as r:
        line = csv.reader(r)
        for row in line:
            rows.append(row[4])
        for x in rows:
            r = x.strip().split('\n')
            for y in r:
                if y.isupper() == True:
                    pass
                else:
                    lines.append(y)
def poem():
    Lnum = int(input('How many lines would you like?   '))
    poem = '\n'
    for x in range(Lnum):
        poem = poem + lines[random.randint(4,len(lines))] + '\n'
    print(poem)
form()
poem()   