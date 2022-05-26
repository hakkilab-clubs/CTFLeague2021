# **ultrasecure**

Category: rev

Points: 200

Downloads: http://chal.ctf-league.osusec.org:1337/static/ultrasecure

Access: nc chal.ctf-league.osusec.org 4545

Description:

Use pwntools and ghidra to reverse engineer and break into the ultrasecure(tm) vault!

## **Reverse Engineering**

We load the `ultrasecure` binary into Ghidra and investigate `main` to find that the bulk of the program's logic is in a function called `password_check`. This function asks the user to repeat a random nonce back to the program within .05 seconds and if the user does so, asks for the user to enter a number and compares it to `-0x21524cc1`. If the numbers are equal, the program prints the flag.

## **Solution Script**

Using pwntools we write a script to connect to the remote program, read in the random nonce, send the nonce back, and then send the value `-0x21524cc1`. Running the script (included in this repo here as crack_ultrasecure.py) gets us the flag.

osu{d3c0mp1ler_go_brrrr}