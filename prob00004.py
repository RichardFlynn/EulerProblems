def pal(n):
    for i in range(int(len(n)/2)):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True
pals=[]
for i in range(100,999):
    for j in range(100,999):
        if pal(str((1099-i)*(1099-j))):
            pals.append((1099-i)*(1099-j))
print(pals)