def bit_stuff(data):
    count = 0
    stuffed = ''
    for bit in data:
        stuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                # Insert a '0' after five consecutive '1's
                stuffed += '0'
                count = 0
        else:
            count = 0
    return stuffed

def bit_unstuff(stuffed_data):
    count = 0
    unstuffed = ''
    i = 0
    while i < len(stuffed_data):
        bit = stuffed_data[i]
        unstuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                # Skip the stuffed '0'
                i += 1
                count = 0
        else:
            count = 0
        i += 1
    return unstuffed

# Input binary data
data = input("Enter binary data to stuff: ")

stuffed_data = bit_stuff(data)
print("Stuffed data:", stuffed_data)

unstuffed_data = bit_unstuff(stuffed_data)
print("Unstuffed data:", unstuffed_data)

