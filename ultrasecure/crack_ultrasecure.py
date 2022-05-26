from pwn import *

# connect to process
r = remote('chal.ctf-league.osusec.org', 4545)

# extract the nonce from process output and send it back
nonce = r.recvline().split()[-1]
r.sendline(nonce)

# receive instruction to unlock and send magic
r.recvline()
r.sendline(str(int("-0x21524cc1", 16)).encode())

# print the flag
print(r.recvline())