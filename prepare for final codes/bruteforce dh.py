# I. Cryptanalysis of the Diffie-Hellman protocol.

print()
print("---------------------------------------------------------------")
print("    Cryptanalysis of the Diffie-Hellman public key protocol    ")
print("---------------------------------------------------------------")
print()

# 1. Collect public information, i.e., the prime, generator and sendings.
p = input("Confirm the prime: ")
p = int(p)
g = input("Confirm the generator: ")
g = int(g)
print()
A = input("A sent: ")
A = int(A) # A = g^{a} mod p where a is the secret integer of Alice
B = input("B sent: ")
B = int(B) # B = g^{b} mod p where b is the secret integer of Bob

print()

# 2. Find an integer x in [1,p-1] s.t. g^{x} = A mod p and g^{x} = B mod p.
# Note that the complexity of this computation is exponential as it is the discrete logarithm problem.
for x in range(1,p) :
    if (g**x)%p == A :
        #print(x)
        a = x
    if (g**x)%p == B :
        #print(x)
        b = x
print("Password for A:",a)
print("Password for B:",b)

print()

# 3. Compute the secrete common key.
k_a = (B**a)%p
k_b = (A**b)%p
#print(k_a,k_b)
k = k_a # Note that k = k_a = k_b
print("Their secret common key:",k)

print()