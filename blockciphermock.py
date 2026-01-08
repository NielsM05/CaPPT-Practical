###########################################
        #ECB 64 BITS TOPKAAS#
###########################################

from cryptocourse import permute

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def encrypt_block_after_sbox(sbox_output, subkey1, subkey2):
    # XOR met subkey 1
    state = xor_bytes(sbox_output, subkey1)

    # Permutatie (byte-niveau)
    state_int = int.from_bytes(state, "big")
    permuted = permute.permute(
        state_int,
        [2,3,1,4,6,7,0,5]
    )
    state = permuted.to_bytes(8, "big")

    # XOR met subkey 2
    state = xor_bytes(state, subkey2)

    return state

# =========================
# INVULLEN (handmatig!)
# =========================

# S-box output van P1 (8 bytes!)
SBOX_P1 = bytes.fromhex("2D 02 BA C1 41 65 20 27")  # <-- JIJ invullen

# S-box output van P2 (8 bytes!)
SBOX_P2 = bytes.fromhex("C4 34 0E 0F 3F 06 8B 43")  # <-- JIJ invullen

# =========================
# Sleutels
# =========================
key = bytes.fromhex(
    "1234567890ABCDEFFEDCBA0987654321FEDCBA09876543211234567890ABCDEF"
)

subkey1 = key[0:8]
subkey2 = key[8:16]

# =========================
# Encryptie
# =========================

C1 = encrypt_block_after_sbox(SBOX_P1, subkey1, subkey2)
C2 = encrypt_block_after_sbox(SBOX_P2, subkey1, subkey2)


print("C1 =", C1.hex())
print("C2 =", C2.hex())

# # ==========================================================
# # CBC BEREKENING (gecorrigeerd)
# # ==========================================================
# plaintext = bytes.fromhex("11223344556677888877665544332211")
# P1 = plaintext[0:8]
# P2 = plaintext[8:16]
#
# # Stap 1: Bereken de input voor de S-box (P2 XOR C1)
# INPUT3 = xor_bytes(P2, C1)
# print("INPUT3 (voor S-box opzoeken) =", INPUT3.hex())
#
# # Stap 2: Vul hier de S-box output in die je handmatig hebt opgezocht voor INPUT3
# # (Komt overeen met SBOX3 uit de afbeelding: 28c6687543b4bf30)
# SBOX_P3 = bytes.fromhex("28 C6 68 75 43 B4 BF 30")
#
# # Stap 3: Gebruik je functie om de rest van de encryptie te doen
# # Deze functie doet: XOR subkey1 -> Permute -> XOR subkey2
# C3 = encrypt_block_after_sbox(SBOX_P3, subkey1, subkey2)
#
# print("C3 =", C3.hex())