# **secure-encryptor**

Category: crypto

Points: 400

Downloads: http://chal.ctf-league.osusec.org:1337/static/secure-encryptor

Access: nc chal.ctf-league.osusec.org 4646

Description:

Someone took the flag and encrypted it! Fortunately for us, they don't know that a one time pad shouldn't be used more than. Can you break the secure-encryptor and retrieve the flag? I've heard it might have something to do with the answer to life, the universe, and everything...

## **Reverse Engineering**

We load the secure-encryptor binary into Ghidra and look at `main`. The program generates a random 1024 byte one time pad with `get_otp` and generates random padding around the flag to make it 1024 bytes long with `random_pad`. The program then encrypts the padded flag in the `encrypt` function by XORing each byte with 42, then XORin each byte of the padded flag with the corresponding byte from the OTP, and finally converting it to base64. This encrypted text is what is shown when you connect to the remote instance of the program

After the encrypted text is shown, we get the chance to send our text to encrypt and then get the encryption back. This encryption uses the same padding method and OTP as the flag encryption, which is how we will break the encryption.

## **Getting the OTP**

XORing has a nice property in that if you have something like `a = b XOR c` where `a` and `b` are known, you can calculate `c` with `c = a XOR b`. In this program `a` would be the encrypted byte, `b` would be the original text byte, and `c` would be the OTP byte. The `random_pad` function pads text up to 1024 bytes, so if we send something with exactly 1024 bytes (like a string of 1024 A's), the padding will not occur and we will just get the OTP XORed with our text and 42, and we will then know two of the three operands exactly. In short, when we XOR the encrypted text and original text we have `encrypted = text XOR 42 XOR OTP => encrypted XOR text = OTP XOR 42`, and we can use this to get the flag since `encrypted = flag XOR 42 XOR OTP => flag = encrypted XOR 42 XOR OTP`.

## **Decrypting the flag**

Using pwntools we write a script to connect to the remote program, read in the encrypted flag, send our string of 1024 A's, read back the encrypted A string and get the OTP, and then use the OTP to decrypt and display the flag. Running the script (included in this repo here as crack_secure-encryptor.py) gets us the flag.

osu{d0n7_u5e_4_1_71m3_p4d_m0r3_th4n_0nc3}