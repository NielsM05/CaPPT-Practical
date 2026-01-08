from __future__ import annotations

from cryptocourse import shamir
from cryptocourse import basic_bc

def main() -> None:
    # 1) Shamir reconstruct
    p = 19
    shares = [(1, 8), (2, 18), (5, 11), (6, 6)]
    secret_K = shamir.reconstructSecret(shares, p)
    print("Reconstructed secret_K =", secret_K)

    # 2) Identities
    joe = basic_bc.MyIdentity("Joe", 1)
    donald = basic_bc.MyIdentity("Donald", 2)

    # 3) Transaction: Joe pays Donald the secret amount
    tx = basic_bc.MyTransaction(joe, donald, secret_K, timestamp=100000)
    tx.sign()

    # 4) Block: index 0, one tx, timestamp 100010, prev hash = '0'*64, miner="SampleExam"
    block = basic_bc.Block(
        index=0,
        transactions=[tx],
        timestamp=100010,
        previous_hash="0" * 64,
        miner="SampleExam",
    )

    block.mine()
    print("Mined nonce =", block.nonce)
    print("Block hash  =", block.hash)

if __name__ == "__main__":
    main()
