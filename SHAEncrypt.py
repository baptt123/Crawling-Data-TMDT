import hashlib

def hash_sha256(password):
    sha = hashlib.sha256()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()

password = "tantt121"
hashed = hash_sha256(password)
print("SHA-256 hash:", hashed)
