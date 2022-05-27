from pwn import *
from base64 import b64decode

# connect to process
r = remote('chal.ctf-league.osusec.org', 4646)

# get the enctypted flag and convert from base64
r.recvline()
encrypted_flag = b64decode(r.recvuntil(b"=\n").replace(b"\n", b""))

# send A's string and get back encrypted A's string
r.recvline()
Astring = b"A" * 1024
r.send(Astring)

r.recvline()
encrypted_Astring = b64decode(r.recvuntil(b"=\n").replace(b"\n", b""))

# XOR A's and encrypted A's to get OTP
OTP = b""
for i in range(1024):
	OTP += (encrypted_Astring[i] ^ Astring[i]).to_bytes(1, 'big')

# XOR OTP and encrypted flag to decrypt flag
padded_flag = b""
for i in range(1024):
	padded_flag += (encrypted_flag[i] ^ OTP[i]).to_bytes(1, 'big')

print(padded_flag)