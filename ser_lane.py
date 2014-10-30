
N, T = raw_input().split(" ")

alist = raw_input().split(" ")

for i in range(int(T)):
    i, j = raw_input().split(" ")
    begin = int(i)
    end = int(j)
    
    print min(alist[begin:end+1])

