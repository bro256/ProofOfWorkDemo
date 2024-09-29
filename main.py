import hashlib
import time

nonce = 0
max_binary_leading_zeros = 0
counter = 0
start_time = time.time()

def bytes_to_hex(bytes_seq):
    return ''.join(f'{b:02x}' for b in bytes_seq)

def bytes_to_binary(bytes_seq):
    return ''.join(format(b, '08b') for b in bytes_seq)

def count_leading_zeros_binary(binary_string):
    count = 0
    for char in binary_string:
        if char == '0':
            count += 1
        else:
            break
    return count

def count_leading_zeros_hex(hex_string):
    count = 0
    for char in hex_string:
        if char == '0':
            count += 1
        else:
            break
    return count

def get_elapsed_time(start_time):
    return int((time.time() - start_time) * 1000)

while counter <= 1000000:
    data = "Demo" + str(nonce)
    hashbytes = hashlib.sha256(data.encode()).digest()
    binary_hash = bytes_to_binary(hashbytes)
    leading_zeros_binary = count_leading_zeros_binary(binary_hash)

    if leading_zeros_binary > max_binary_leading_zeros:
        print("Hash bytes:", hashbytes)

        hex_hash = bytes_to_hex(hashbytes)
        print("Hexadecimal Hash:", hex_hash)

        print("Binary Hash:", binary_hash)

        print("Leading Zeros in Binary:", leading_zeros_binary)

        leading_zeros_hex = count_leading_zeros_hex(hex_hash)
        print("Leading Zeros in Hex:", leading_zeros_hex)

        print("Iterations:", counter)

        print('Elapsed Time:', get_elapsed_time(start_time), 'ms')
        print("------------------------------------------")

        max_binary_leading_zeros = leading_zeros_binary
    
    nonce += 1
    counter += 1
