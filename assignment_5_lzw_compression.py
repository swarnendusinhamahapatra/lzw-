# assignment_5_lzw_compression.py

def compress(text):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    w = ''
    result = []

    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = c

    if w:
        result.append(dictionary[w])
    return result


def decompress(data):
    if not data:
        return ''

    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    w = chr(data[0])
    result = w

    for k in data[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == next_code:
            entry = w + w[0]
        else:
            raise ValueError('Invalid compressed data')

        result += entry
        dictionary[next_code] = w + entry[0]
        next_code += 1
        w = entry

    return result


# Execution and Validation
text = 'ABABABAABABA'
compressed = compress(text)
decompressed = decompress(compressed)

print('Original Data:', text)
print('Compressed Data:', compressed)
print('Decompressed Data:', decompressed)
print('Compression Successful:', text == decompressed)