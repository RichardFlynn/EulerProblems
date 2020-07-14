def sumsquare(n):
    if n==1:
        return 1
    return (n**2)+sumsquare(n-1)
def squaresum(n):
    return (n*(n+1)/2)**2

x=100
print(squaresum(x)-sumsquare(x))