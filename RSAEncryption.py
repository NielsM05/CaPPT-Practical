#in te vullen
p = 16049261
q = 11253433

n = p * q
phi = (p - 1) * (q - 1)

#Gegeven encryption key invullen
e = 65537

# Bereken d
d = pow(e, -1, phi)

# Deel A: Plain in te geven hier -> Cipher
msg_a = 123456
cipher_a = pow(msg_a, e, n)
print(f"Cipher: {cipher_a}")

print("Check zelfde plain uitkomst")
print(pow(cipher_a,d,n))

# Deel B: Cipher in te geven hier -> Plain
cipher_b = 654321
plain_b = pow(cipher_b, d, n)
print(f"Plain: {plain_b}")

print("Check zelfde cipher uitkomst")
print(pow(plain_b,e,n))