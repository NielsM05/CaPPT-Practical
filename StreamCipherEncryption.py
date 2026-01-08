# ==========================================================
# 1. DE INVUL-SECTIE
# ==========================================================

# De volledige stream uit de opgave
STREAM_HEX = "1cf1decf64ab6099e45d210358d0e9dff5cf877b36f60636ad23ebd992662fa49213e6b293247cc7661da39301133aa1651beeba32751dcc13320745c34b44bdf3160d0f1ece13b980dddf09ffbea9f43d86e9732cfa0092231af456188c2cb647dacce31fd1078872414a27a1e3cb477398d804530bce3d9460"

# De plaintext uit de opgave
PLAIN_HEX  = "200300400500600700800900100A00B00C00D00E00F00000"

# ==========================================================
# 2. HET SCRIPT
# ==========================================================

def solve_xor_cipher():
    # We hebben maar een stukje van de stream nodig dat even lang is als de plaintext
    lengte = len(PLAIN_HEX)
    relevant_stream = STREAM_HEX[:lengte]

    # Zet beide om naar getallen (base 16)
    stream_int = int(relevant_stream, 16)
    plain_int  = int(PLAIN_HEX, 16)

    # Voer de XOR (^) uit
    cipher_int = stream_int ^ plain_int

    # Zet terug naar hexadecimaal en zorg dat leading zeros blijven staan
    # De '0x' aan het begin halen we weg
    cipher_hex = hex(cipher_int)[2:].zfill(lengte)

    print("-" * 40)
    print(f"De Ciphertext is:\n{cipher_hex}")
    print("-" * 40)

if __name__ == "__main__":
    solve_xor_cipher()