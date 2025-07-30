def xor(a, b):
    """Perform XOR between two binary strings."""
    result = ''
    for i in range(1, len(b)):
        result += '0' if a[i] == b[i] else '1'
    return result

def mod2div(dividend, divisor):
    """Perform Mod-2 division and return the remainder."""
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    # Last step
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def sender(data, divisor):
    """Sender function that generates the CRC code and sends data."""
    print("=== Sender ===")
    print(f"Original Data: {data}")
    print(f"Divisor (Generator): {divisor}")

    # Append zeros
    padded_data = data + '0' * (len(divisor) - 1)
    remainder = mod2div(padded_data, divisor)
    crc = remainder
    transmitted = data + crc

    print(f"CRC: {crc}")
    print(f"Transmitted Data: {transmitted}")
    return transmitted

def receiver(data, divisor):
    """Receiver function that checks for errors using CRC."""
    print("\n=== Receiver ===")
    print(f"Received Data: {data}")
    remainder = mod2div(data, divisor)
    print(f"Remainder: {remainder}")

    if '1' in remainder:
        print("Error detected in received data.")
    else:
        print("No error detected. Data is correct.")

# Example usage
data = input("Enter binary data: ")
divisor = input("Enter divisor (generator polynomial): ")

# Simulate sender
transmitted_data = sender(data, divisor)

# Simulate receiver (you can modify transmitted_data to test errors)
receiver(transmitted_data, divisor)
