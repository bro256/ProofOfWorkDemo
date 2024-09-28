import hashlib


nonce = 0
num_zeros = 0
counter = 0

def bytes_to_hex(bytes_seq):
    hex_string = ""
    for b in bytes_seq:
        hex_string += f'{b:02x}'
    return hex_string

def bytes_to_binary(bytes_seq):
    binary_string = ""
    for b in bytes_seq:
        binary_string += format(b, '08b')
    return binary_string

def count_leading_zeros_binary(binary_string):
    count = 0
    for char in binary_string:
        if char == '0':
            count += 1
        else:
            break
    return count



data = "Demo" + str(nonce)
hashbytes = hashlib.sha256(data.encode()).digest()


print("Hash bytes:", hashbytes)

hex_hash = bytes_to_hex(hashbytes)
print("Hexadecimal Hash:", hex_hash)

binary_hash = bytes_to_binary(hashbytes)
print("Binary Hash:", binary_hash)

leading_zeros_binary = count_leading_zeros_binary(binary_hash)
print("Leading Zeros in Binary:", leading_zeros_binary)

