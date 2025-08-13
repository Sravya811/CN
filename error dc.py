def calc_parity_bits_length(data_length):
    # Number of parity bits needed
    r = 0
    while (2 ** r) < (data_length + r + 1):
        r += 1
    return r

def generate_hamming_code(data):
    m = len(data)
    r = calc_parity_bits_length(m)
    total_length = m + r

    # Initialize hamming code array (1-based indexing)
    hamming_code = ['0'] * (total_length + 1)

    # Place data bits in positions that are not powers of 2
    j = 0
    for i in range(1, total_length + 1):
        if i & (i - 1) != 0:  # Not a power of 2
            hamming_code[i] = data[j]
            j += 1

    # Calculate parity bits
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for bit_pos in range(1, total_length + 1):
            if bit_pos & parity_pos:
                parity ^= int(hamming_code[bit_pos])
        hamming_code[parity_pos] = str(parity)

    return ''.join(hamming_code[1:])

def detect_and_correct(hamming_code):
    n = len(hamming_code)
    hamming_code = ['0'] + list(hamming_code)  # 1-based indexing
    r = calc_parity_bits_length(n - calc_parity_bits_length(n))

    # Find error position
    error_pos = 0
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for bit_pos in range(1, n + 1):
            if bit_pos & parity_pos:
                parity ^= int(hamming_code[bit_pos])
        if parity != 0:
            error_pos += parity_pos

    if error_pos != 0:
        print(f"Error detected at position: {error_pos}")
        # Correct the error
        hamming_code[error_pos] = '1' if hamming_code[error_pos] == '0' else '0'
        print(f"Corrected Hamming code: {''.join(hamming_code[1:])}")
    else:
        print("No error detected.")

    return ''.join(hamming_code[1:])

# Example usage
data_bits = input("Enter binary data bits: ")
hamming_code = generate_hamming_code(data_bits)
print(f"Hamming code: {hamming_code}")

# Simulate error (optional)
error_code = list(hamming_code)
error_code[3] = '1' if error_code[3] == '0' else '0'  # Flip bit at pos 3
print(f"Received code with error: {''.join(error_code)}")

# Detect & correct
corrected = detect_and_correct(''.join(error_code))
