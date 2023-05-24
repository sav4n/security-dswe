import hashlib
from random import randrange

p = 9719
q = 4867
g = 7
x = 1234
y = pow(g, x, p)

def H(M):
    return int(hashlib.sha256(str(M).encode('utf-8')).hexdigest(), 16)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError('modular inverse does not exist')
    return x % m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def sign(M):
    k = randrange(1, q)
    r = pow(g, k, p)
    s = (H(M) - x*r) * modinv(k, q) % q
    return (r, s)


M = 123456789
print("Message:", M)
signature = sign(M)
print("Signature:", signature)
valid = verify(M, signature, y)
print("Signature is valid:", valid)
