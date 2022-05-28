# **deprecated_echo**

Category: misc

Points: 400

Downloads: http://chal.ctf-league.osusec.org/nft.jpg

Access: nc chal.ctf-league.osusec.org 6969

Description:

Top level software determined that this image is suspicious. We cannot find out why, so we ask you to find out what information it holds. We think it is the source code for an antiquated echo service which we have discovered here:
http://chal.ctf-league.osusec.org/nft.jpg

The program that detected that this image is suspicious also spit out the information:

Bits=3

Flag is in flag.txt

TOOLS:
Some sort of LSB Stego tool, recommended: https://github.com/Aqcurate/lsb-steganography

## **Analyzing the image**

Using the provided LSB Stego tool, we extract an image from the provided nft.jpg with `python steglsb.py -d nft.jpg 3 output.jpg` since the prompt gives us Bits=3. Looking at the extracted image we see the link https://pastebin.com/9bRN2Eah, which links us to python code. This python code is what is running at the access location provided, as we can see from the matching output.

## **Exploiting python2 input()**

Looking at the python code, there is a try/except block where the code tries to open a user specified file and write user specified text to it, and if this fails, prompts for a file to write information on the exception to. In the except portion, the code uses `input()` instead of `raw_input()`, which means we can enter code to evaluate and get a shell. We create a small script to do this (included in this repo here as get_input_shell.py) and run it to get the flag.

osu{m1sc_CTF_b35t_cTF}