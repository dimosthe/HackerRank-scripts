##### list comprehensions #####
inputs = []
for i in range(4):
    inputs.append(input())

alist = [[i,j,k] for i in range(inputs[0]+1) for j in range(inputs[1]+1) for k in
        range(inputs[2]+1) if i+j+k != inputs[3] ]
print alist
	
	
