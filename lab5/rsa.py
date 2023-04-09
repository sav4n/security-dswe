import math
from random import randrange

def prime(minn , maxx):
    while(1):
        p = randrange(minn,maxx)
        q = randrange(minn,maxx)
        if( p != q):
            if(isPrime(p) and isPrime(q)):
                return [p, q]
        
        
def isPrime(num):
    if num > 1:
        for i in range(2,int(num/2)+1):
            if(num % i == 0):
                return False
            else:
                return True
    else:
        return False
        
def gcd(a,h):
    temp = 0
    while (1):
        temp = a % h
        if(temp == 0):
            return h
        a = h
        h = temp

# we can use math.gcd too

def finde(phi):
    e=2
    while (e < phi ):
        if(gcd(e, phi) == 1):
            return e
            break
        else:
            e = e +1
            
minn = int(input('enter min :'))
maxx = int(input('enter max :'))


p , q = prime(minn,maxx)

n = p * q

phi = (p-1) * (q-1)
e = finde(phi)

print(f"p = {p}")

print(f"q = {q}")

print(f"n = {n}")


print(f"phi = {phi}")
        
print(f"e = {e}") 

d = 0

for i in range(n):
    if( ((i * e) % phi) == 1 ):
        d = i

print(f"d = {d}")  


print((d * e) % phi == 1)

p = int(input("Message: "))
c = pow(p,e) % n

p = pow(c,d) % n


#
print(f"c = {c}")

print(f"p = {p}")

# charc = chr(c)

# charp = chr(p)

# print(f"c = {charc}")

# print(f"p = {charp}")
