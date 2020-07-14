def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

m=int(input())
p=0
n=0
while p<m:
    n+=1
    if isPrime(n):
        p+=1
print(n)