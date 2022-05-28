# **secure-encryptor**

Category: crypto

Points: 500

Downloads: http://chal.ctf-league.osusec.org/really_secure_algorithm.zip

Access: Run client.py

Description:

I've created a **R**eally**S**ecure**A**lgorithm to encrypt secret messages. According to NIST, my 2048 bit keys should be good to use until at least 2030, so good luck cracking it!

## **Reverse Engineering**

Based on the bolding and name of this challenge, we are looking at a protocol similar to RSA. Looking through the `server.py` file we notice that there is a `decrypt` function that we can copy to decrypt what we get from the remote server. The server gives us n_bits, e, N, and ctxt when we connect. The decrypt function requires ctxt, d, N, and n_bits, so all we are missing is d. Looking at the code, d is calculated as `d = pow(self.e, -1, carmichael_N)` where `carmichael_N = int((p-1)*(q-1)//GCD(p-1, q-1))`. So now we need p and q. Here is where we find our vulnerability: p and q are consecutive primes! Since `N=p*q`, we can find the square root N and then step up and down from this value checking for primes until we get q and p. We can then use these to crack the cipher using the `decrypt` frrm the server.

## **Cracking the cipher

We write a script to connect to the remote program and read the parameters from the server, then calculate p and q from the square root of N, and use this to decrypt the flag. Running the script (included in this repo here as bad_RSA_crack.py) gets us the flag.

osu{d0n7_ch0O5e_pR1m3s_7h4t_R_5imIl4r}