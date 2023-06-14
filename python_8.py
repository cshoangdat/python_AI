#set -> chua cac phan tu mang k trung nhau
s = {8,9,5,6,4,5,2,6,8,9}
#print(type (s))
print(s)
s.add(1)
print(s)
s.remove(8)
print(s)
#s.clear()
#print(s)
print (1 in s)
s2 = {2, 3, 10, 11}
print (s.union(s2))
#ket hop 2 set voi nhau
print (s.difference(s2))
#lay phan khac giua s va s2
print(s.intersection(s2))
#lay 2 set giao nhau