arr = []
for i in range(2000,3200):
    if(i%7 == 0):
        if(i%5==0): continue
        arr.append(i)

print(arr)
        
        