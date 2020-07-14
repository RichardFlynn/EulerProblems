from math import ceil
def isprime(x):
    for n in range(2,ceil(x**0.5)):
        if x%n==0:
            return False
    return True

smallfactors=[]
bigfactors=[]
primes=[]
for i in range(2,ceil(600851475143**0.5)):
    if 600851475143%i==0:
        smallfactors.append(i)
for i in smallfactors:
    if isprime(i):
        primes.append(i)
    bigfactors.append(int(600851475143/i))
for i in bigfactors:
    if isprime(i):
        primes.append(i)
#print(smallfactors,bigfactors)
print(max(primes))
#print(isprime(3))
# num=600851475143
# primefactors=[]
# p=2
# while num>1:
#     if num%p==0:
#         primefactors.append(p)
#         num=num/p
#     else:
#         p+=1
# print(primefactors)