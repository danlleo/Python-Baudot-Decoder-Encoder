from map import baudot_map as bmp


def decrypt(string):
    sentence = ""

    for i in range(0, len(string)):
        sentence += bmp[string[i].upper()] + ' '

    return sentence


def encrypt(string):
    arr = string.split()
    sentence = ""

    for i in range(0, len(arr)):
        if list(bmp.keys())[list(bmp.values()).index(arr[i])]:
            sentence += list(bmp.keys())[list(bmp.values()).index(arr[i])]

    return sentence


print(
    decrypt("Infinite striving to be the best is mans duty; it is its own reward. Everything else is in God's hands."))
print(encrypt("01100 00110 10110 01100 00110 01100 00001 10000 00010 10100 00001 01010 01100 01111 01100 00110 01011 00010 00001 00011 00010 10011 10000 00010 00001 00101 10000 00010 10011 10000 10100 00001 00010 01100 10100 00010 00111 11000 00110 10100 00010 10010 11100 00001 10101 01111 00010 01100 00001 00010 01100 10100 00010 01100 00001 10100 00010 00011 11001 00110 00010 01010 10000 11001 11000 01010 10010 00111 00010 10000 01111 10000 01010 10101 00001 00101 01100 00110 01011 00010 10000 01001 10100 10000 00010 01100 10100 00010 01100 00110 00010 01011 00011 10010 11010 10100 00010 00101 11000 00110 10010 10100 00111"))
