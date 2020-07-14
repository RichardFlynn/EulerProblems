from functools import reduce
num=""
for i in range(20):
    num+=input()
#print(len(num))
l=13

print(max(reduce(lambda x,y:x*y,[int(num[i+x])for x in range(l)])for i in range(len(num)-l+1)))