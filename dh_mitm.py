import secrets

# Public parameters
p = 23
g = 5

# Alice and Bob private keys
a = secrets.randbelow(p - 2) + 1
b = secrets.randbelow(p - 2) + 1

# Alice and Bob public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Eve generates two private keys
eve_a = secrets.randbelow(p - 2) + 1
eve_b = secrets.randbelow(p - 2) + 1

# Eve generates replacement public keys
E_A = pow(g, eve_a, p)
E_B = pow(g, eve_b, p)

# Alice and Bob calculate secrets with Eve
alice_secret = pow(E_A, a, p)
bob_secret = pow(E_B, b, p)

# Eve calculates corresponding secrets
eve_secret_a = pow(A, eve_a, p)
eve_secret_b = pow(B, eve_b, p)

print("Alice-Eve Secret:", alice_secret)
print("Eve-Alice Secret:", eve_secret_a)

print("Bob-Eve Secret:", bob_secret)
print("Eve-Bob Secret:", eve_secret_b)

print("Alice-Eve Match:",
      alice_secret == eve_secret_a)

print("Bob-Eve Match:",
      bob_secret == eve_secret_b)
