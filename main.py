import sys

# Code for pythagoras triplet
def pythagoreanTriplet(n):
    result=[]
    for a in range(1, n):
        denom = 2*(n-a)
        num = 2*a**2 + n**2 - 2*n*a
        if denom > 0 and num % denom == 0:
          c = num // denom
          b = n - a - c
          if b > a:
            result.append((a*b*c))
    if len(result)>0:
        print(max(result))
    else:
        print(-1)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    pythagoreanTriplet(n)
