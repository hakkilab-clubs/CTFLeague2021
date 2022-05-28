# **flfickr**

Category: web

Points: 500

Downloads: http://chal.ctf-league.osusec.org/flfickr.tar.gz

Access: http://flfickr.ctf-league.osusec.org/

Description:

Welcome to the latest and greatest image sharing platform, flfickr!

## **Reverse Engineering**

We look at the code in the provided `index.php` and `upload.php` files. We see that `upload.php` only allows us to upload .gif, .jpg, .jpeg, or .png file types, and uses validation to ensure this is the case. We also see in `index.php` that if we add `?language=` and then a path to the end of the website url, the website will attempt to load that file! Thus, we have a mechanism for uploading and then loading our own files. We can use this to upload a PHP script to the server and have it execute code to find the flag.

## **Running a PHP script**

Since the server validates that an uploaded file is actually an image, we need to embed our PHP script somehow. We can sue the EXIF data to do so. Using an image called `payload.png` we can run `exiftool -comment="<?php $output1 = exec('find / -name flag.txt'); echo $output1; ?>" > fl3.png` to set the photo comment to be a PHP script. We then upload this file to the website and navigate to http://flfickr.ctf-league.osusec.org/?language=../uploads/fl3.png to see the path for the flag. We go to this path using http://flfickr.ctf-league.osusec.org/?language=../../../../var/www/html/secrets/flag/i/bet/you/want/the/flag/well/its/in/this/directory/but/how/far/down/is/it/oooh/i/think/you/might/be/getting/close/oh/here/it/is/flag.txt/haha/just/kidding/that/was/a/directory/too/ok/fine/here/you/go/flag.txt to get our flag.

osu{LFI-L00K1nG_F0R_InFoRMa71oN}