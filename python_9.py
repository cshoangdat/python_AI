#dict
x = {}
y = []
z = ()
s= set()
print(type (x), type (y), type(z), type(s))

x = {'key': [31, 8, 90]}
#trong kieu dict: {key: value}
print(x)

y = {'key': 1}
print (y)

z = {'key': "Dat"}
print (z)
print(z['key'], x['key']) #in ra value voi ten key
z[2] = 8
z['key2'] = 69
print (z)
print ('key' in z)
print(z.keys())
print(list(z.keys()))
print(list(z.values()))
del z['key']
print (z)

for key, value in z.items():
    print(key, value)

for key in z.keys():
    print(key, z[key])