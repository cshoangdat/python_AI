for i in range(10,0,-1):
    print (i)
#range(start,stop,step)
list_sample = ["Dat",1,True,9.5]
for x in list_sample:
    print(x)
for x in range(len(list_sample)):
    print(x, list_sample[x])

j = 0
while j<6:
    print(j)
    j += 1

while True:
    if j>7:
        print (j)
        break
    else:
        j+=1

k = 0
while k<5:
    k+=1
    if k == 3:
        continue
    print (k)