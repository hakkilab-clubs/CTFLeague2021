# **hash_browns**
Category: web

Points: 200

Downloads: None

Access: http://chal.ctf-league.osusec.org:31337/

Description:

Welcome to the OSUSEC CTF League! The goal of each of these challenges is to find a flag that will be in the form osu{n0t_a_fL4g}. When you capture the flag, submit it in this channel using $submit flag. To start, open the linked website in your browser. Good luck!

## **Initial Observations**

When we go to the provided link we see a web page with a short bit of text referencing the weirdness of the submit button and recommending we **inspect** it.

## **Inspecting the button**

When we inspect the button, we see it has `clickevent = check_password()`. We find this function in `<script>...</script>` and see that it is just grabbing the text from the text box, computing a SHA256 hash of this text, and comparing it to `b0fef621727ff82a7d334d9f1f047dc662ed0e27e05aa8fd1aefd19b0fff312c`.

## **Cracking the hash**

The website text also makes reference to https://crackstation.net/. Going to this website shows a password hash cracker. How convenient!

Entering in the hash we got earlier gives the password `pineapple`.

## **Playing flag tag**

When we enter this password into the website and click submit, we get a prompt to "Catch me if you can!" followed by text bouncing around the screen.

Luckily, we don't really need to catch this. Using inspect again, we can see the text is a link with id "bouncyLink" where the bouncing is due to the styling of the link. Editing the HTML in our browser to remove all the styling other than `display: block;` causes the link to stop moving and go to the top left corner, where we click it and get out flag.


osu{p1n34ppl3_h45h_Br0wN5_4r3_g00D}