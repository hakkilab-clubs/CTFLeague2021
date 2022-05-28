# **raccoon_quiz**

Category: pwn

Points: 500

Downloads: http://chal.ctf-league.osusec.org/raccoon_quiz

Access: nc chal.ctf-league.osusec.org 4816

Description:

Welcome to my super-awesome-amazing-raccoon-quiz-program (def no security vulns in here). Do you have what it takes to be the sneakiest raccoon expert of them all?

This resource might be helpful: https://web.ecs.syr.edu/~wedu/Teaching/cis643/LectureNotes_New/Format_String.pdf

## **Reverse Engineering**

We load the raccoon_quiz binary into Ghidra and look at `main`. The bulk of the program is in the function `raccoon_quiz`, which asks a series of questions (that we can see the correct answers for) and if the user gets them all correct, the user can enter a name for the leaderboard. Based on the resource provided, this is a format string challenge. We see that the name entry after the quiz is where can use a string format attack, and looking through other functions note that `super_sneaky_function` is the function to call to print the flag.

We also notice that the first time `exit` is called in the program is as the end of `raccoon_quiz`, which means we can use the format string vulnerability to overwrite the GOT entry for `exit` to be `super_sneaky_function` instead. Using checksec we see that PIE is disabled, so we can get addresses from the local binary and use them. We also found that the offset needed for our format string was 6.

## **Format string exploit**

Using pwntools we write a script to connect to the remote program, complete the quiz, and then send a format string payload to overwrite the exit GOT entry. Running the script (included in this repo here as format_string_raccoon.py) gets us the flag.

osu{tr4a5h_pr0gr4mm1ng_in_4_tr4sh_g4m3}