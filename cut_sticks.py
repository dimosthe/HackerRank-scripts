##### Cut the sticks #####
from sys import exit

N = input()
alist = map(int, raw_input().split(" "))

if len(alist) != N:
    print "Invalid number N"
    exit()

minimum = min(alist)
length = len(alist)
while True:
    cuts = 0
    for i in range(length):
        if alist[i] > minimum:
            alist[i] -= minimum
        else:
            alist[i] = 0
        cuts += 1

    print cuts
    alist = filter(lambda a: a != 0, alist)
    length = len(alist)
    if length == 0:
        break
    minimum = min(alist)
