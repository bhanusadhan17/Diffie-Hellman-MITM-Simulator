import secrets

# Public parameters
p = 23
g = 5

# Generate private keys
alice_private = secrets.randbelow(p - 2) + 1
bob_private = secrets.randbelow(p - 2) + 1

# Generate public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

# Calculate shared secrets
alice_shared = pow(
    bob_public, alice_private, p
)

bob_shared = pow(
    alice_public, bob_private, p
)

# Verify shared secrets
print("Alice Shared Key:", alice_shared)
print("Bob Shared Key:", bob_shared)

print("Key Exchange Successful:",
      alice_shared == bob_shared)
