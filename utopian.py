from sys import exit

try:
    T = int(raw_input(''))
except ValueError:
    print "Not a number"
    exit()

if T not in range(1,11):
    print "Wrong number T"
    exit()

alist = []
while T > 0:
    try:
        N = int(raw_input(''))
    except ValueError:
        print "Not a number"
        exit()
    
    if N not in range(0,61):
        print "Wrong number N"
        exit()
    alist.append(N)
    T = T - 1 
    
alist.reverse()
while len(alist) > 0:
    num = alist.pop()

    height = 1
    cycle = 1
    while num > 0:
        if cycle % 2 == 0:
            height = height + 1
        else:
            height = height * 2
        cycle = cycle + 1
        num = num -1

    print height

