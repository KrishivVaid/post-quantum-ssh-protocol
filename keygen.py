from dilithium_py.dilithium import Dilithium2

def generate_dilithium_keys():
    # Generate a Dilithium keypair (public key pk, secret key sk)
    pk, sk = Dilithium2.keygen()
    # Write keys to files
    with open("server_public.key", "wb") as f:
        f.write(pk)
    with open("server_private.key", "wb") as f:
        f.write(sk)
    print("Dilithium key pair generated (server_public.key, server_private.key).")

if __name__ == "__main__":
    generate_dilithium_keys()
