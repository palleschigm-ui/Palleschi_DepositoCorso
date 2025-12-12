array=[]

for i in range(3):
    array.append(lambda i=i: print(i))

for a in array:
    a()