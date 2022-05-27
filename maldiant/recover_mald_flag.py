from itertools import cycle

# get the encrypted PNG bytes
with open('flag.png.MALD', 'rb') as f:
    encrypted = f.read()

# using PNG magic bytes decrypt the PNG bytes
magic_bytes = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]
decrypted = [a ^ b for a, b in zip(encrypted, cycle(magic_bytes))]

# write the decrypted bytes to a PNG file
with open(f"flag.png", 'wb+') as out:
    out.write(bytes(decrypted))
