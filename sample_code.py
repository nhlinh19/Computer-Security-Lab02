#!/usr/bin/python3

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

# MSG   = "A message"
# HEX_1 = "aabbccddeeff1122334455"
# HEX_2 = "1122334455778800aabbdd"

MSG = "This is a known message!"
HEX_1 = "a469b1c502c1cab966965e50425438e1bb1b5f9037a4c159"
HEX_2 = "bf73bcd3509299d566c35b5d450337e1bb175f903fafc159"

# Convert ascii string to bytearray
D1 = bytes(MSG, 'utf-8')

# Convert hex string to bytearray
D2 = bytearray.fromhex(HEX_1)
D3 = bytearray.fromhex(HEX_2)

# r1 = xor(D1, D2)
# r2 = xor(D2, D3)
# r3 = xor(D2, D2)
r1 = xor(D2, D3)
r2 = xor(r1, D1)
for i in range(0, len(r2)):
    r2[i] = r2[i]^1
print(r1.hex())
print(r2.decode('utf-8'))
# print(r3.hex())
