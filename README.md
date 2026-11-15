
# Diffie-Hellman Key Exchange with Man-in-the-Middle Simulator

## Project Overview

This project demonstrates the Diffie-Hellman Key Exchange algorithm and its vulnerability to a Man-in-the-Middle (MITM) attack.

It uses Python to simulate secure key agreement between Alice and Bob and demonstrates how an attacker (Eve) can intercept and replace public keys to establish separate shared secrets with both parties.

## Objectives

- Understand the Diffie-Hellman Key Exchange algorithm.
- Generate private and public keys.
- Calculate a common shared secret.
- Simulate a Man-in-the-Middle attack.
- Demonstrate the importance of authentication in key exchange.

## Technologies Used

- Python 3
- Python secrets module
- Modular Exponentiation

## Project Modules

### 1. Normal Diffie-Hellman Key Exchange
Demonstrates how Alice and Bob independently calculate the same shared secret.

### 2. Man-in-the-Middle Attack
Demonstrates how Eve intercepts and replaces public keys, establishing separate shared secrets with Alice and Bob.

## Project Files

- `dh_normal.py` – Normal Diffie-Hellman key exchange.
- `dh_mitm.py` – Man-in-the-Middle attack simulation.

## How to Run

Make sure Python 3 is installed.

Run the normal key exchange:

```bash
python dh_normal.py
```

Run the MITM simulation:

```bash
python dh_mitm.py
```

## Security Note

The simulation uses small example parameters (p = 23, g = 5) for educational purposes only. These parameters are not secure for real-world cryptographic applications.

## Conclusion

This project illustrates how Diffie-Hellman establishes a shared secret and why authentication is necessary to protect against Man-in-the-Middle attacks.
