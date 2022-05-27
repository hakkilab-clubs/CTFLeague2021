# **babypwn**

Category: pwn

Points: 400

Downloads: http://chal.ctf-league.osusec.org/static/babypwn

Access: nc chal.ctf-league.osusec.org 4747

Description:

Can you exploit this vulnerable 64 bit program?

## **Reverse Engineering**

We load the babypwn binary into Ghidra and look at `main`. The bulk of the program is in the `user_input` program, which prompts the user to enter some text. We also notice that the program is using `fgets` to read in up to 200 characters and store them in `local_18`. This means the buffer can hold up to 16 characters, and so we can cause a buffer overflow. Looking at the other functions we see one called `print_flag`, so we will want to overwrite the return address to redirect program flow to this function. Since the buffer can contain 16 bytes, we will need to overflow the buffer with 24 bytes (16 bytes for buffer + 8 bytes for saved RBP) followed by bytes for the address of `print_flag`. Using checksec we also see this binary does not use a stack canary or PIE, so we will not need to work about the stack canary and can use memory locations we find with pwntools locally to exploit the remote instance.

## **Buffer overflow**

Using pwntools we write a script to connect to the remote program and send bytes to overflow the buffer and call `print_flag`. Running the script (included in this repo here as babypwn_overflow.py) gets us the flag.

osu{c0ngr4tz_on_F1r5T_pwn}