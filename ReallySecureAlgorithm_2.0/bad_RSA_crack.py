import math
import json
from Crypto.Util.number import GCD, isPrime
from Crypto.Util.Padding import unpad
from pwn import *

# connect to remote instance
r = remote("chal.ctf-league.osusec.org", 5128)

# get parameters from the server
RSA_params = json.loads(r.recv(2600))
n_bits = RSA_params["n_bits"]
e = RSA_params["e"]
N = RSA_params["N"]
ctxt = RSA_params["ctxt"]

# calculate p and q from N
sqrt_N = math.isqrt(N)
p = sqrt_N
q = sqrt_N

while not isPrime(p):
	p -= 1

while not isPrime(q):
	q += 1

# calculate d from p and q
carmichael_N = int((p-1)*(q-1)//GCD(p-1, q-1))
d = pow(e, -1, carmichael_N)

# decrypt flag and print
bytes_flag = pow(ctxt, d, N).to_bytes(n_bits//8, "big")
flag = str(unpad(bytes_flag, n_bits//8), "utf-8")
print(flag)