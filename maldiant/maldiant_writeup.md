# **maldiant**

Category: malware

Points: 400

Downloads: http://chal.ctf-league.osusec.org/maldiant.tar.gz

Access: None

Description:

Someone at our company got their flag png image encrypted by 'opening a pdf' of our quarterly report!?! Can you help us recover our flag? (btw you'll want to use pyinstxtractor (https://github.com/extremecoders-re/pyinstxtractor) and python-uncompyle6 (https://github.com/rocky/python-uncompyle6))

## **Extracting the malware**

When we look at the files provided, we see what looks like a maliciously encrypted flag PNG and a PDF containing malware. Using pyinstxtractor we extract the executable from the PDF and start looking through the contents. One particular file `not_odysseus.pyc` looks suspicious, so we use python-uncompyle6 on it to get the python source code.

## **Decrypting the flag**

Looking at the source code for the malware, we see that it collects the magic bytes for a file and then goes through all of the bytes of the file and does a XOR with a magic byte, cycling the magic bytes as it goes. So, in order to recover the file, we need to know the magic bytes for a PNG and then XOR these magic bytes with the encrypted file since XOR is a reversible operation.

The magic bytes for a PNG are `89 50 4E 47 0D 0A 1A 0A` and so we write a script (included in this repo here as recover_mald_flag.py) to decrypt the PNG and open the image to get our flag.

osu{M@G1C_ByT3S_AR3_N3At}