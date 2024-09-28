import hashlib


nonce = 0
num_zeros = 0
counter = 0

def bytes_to_hex(bytes_seq):
    hex_string = ""
    for b in bytes_seq:
        hex_string += f'{b:02x}'
    return hex_string

data = "Demo" + str(nonce)
hashbytes = hashlib.sha256(data.encode()).digest()
print(hashbytes)
print(bytes_to_hex(hashbytes))

