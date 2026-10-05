p = int(input("enter prime number (p):"))
g = int(input("enter primitive root (g):"))
a = int(input("enter private key of A:"))
b = int(input("enter private key of B:"))

A = (g ** a) % p
B = (g ** b) % p

keyA = (B ** a) % p
keyB = (A ** b) % p

print("Public key of A:", A)
print("Public key of B:", B)
print("Shared key of A:", keyA)
print("Shared key of B:", keyB)
