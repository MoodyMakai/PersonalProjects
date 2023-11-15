import random
a = []
b = []
def take():
    with open('Proj/haiku.txt', 'r') as r:
        o=1
        x=0
        while x < 5000:
            x= x+1
            if o%2 == 0:
                b.append(r.readline())
            else:
                a.append(r.readline())
            o=o+1
    for x in a:
        if x.isspace() == True:
            a.remove(x)
    for x in b:
        if x.isspace() == True:
            b.remove(x)
take()

print(f'{a[random.randint(0,len(a))]}\n{b[random.randint(0,len(b))]}\n{a[random.randint(0,len(a))]}')