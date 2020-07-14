def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

l=2000000
print(sum([x for x in range(1,l)if isPrime(x)]))