import random

def solve_stream_cipher():
    # 1. Gegeven variabelen
    key = 123456
    plain_hex = "100200300400500600700800900A00B00C00D00E00F00000"

    # 2. Initialiseer de PRNG
    random.seed(key)

    # 3. Genereer 1000 random bits
    stream = random.getrandbits(1000)

    # 4. Zet plaintext om naar een integer
    plain_int = int(plain_hex, 16)

    # 5. Bereken het aantal bits in de plaintext (48 hex chars * 4 bits = 192)
    bits_needed = len(plain_hex) * 4

    # 6. Neem de "eerste" bits van de stream (de 192 meest significante bits)
    # We schuiven de 1000 bits naar rechts zodat we de bovenste 192 overhouden
    keystream = stream >> (1000 - bits_needed)

    # 7. Voer de XOR bewerking uit
    cipher_int = plain_int ^ keystream

    # 8. Zet terug om naar hex (zorg voor leading zeros met :048x)
    cipher_hex = f"{cipher_int:048x}"

    return cipher_hex

print(f"De ciphertext is: {solve_stream_cipher()}")