# **marvin**

Category: rev

Points: 400

Downloads: https://github.com/BobbySinclusto/marvin

Access: https://discord.gg/nvezFTxNJy

Description:

On October first, 2021, during the first ctf-league meeting of the 2021-2022 school year, the ultra stable and super secure marvin was hacked (unintentionally) by one of our very own ctf-league players who had a single quote in their username. Luckily, no sensitive data was exposed and the bug(s) were fixed the same night that they were discovered. Tonight we're taking a step back in time, to find out how much damage the vulnerabilities could have caused if they had been left unchecked. The flag for tonight's challenge has been added to old_marvin's database. Good luck!

Hint: Bot commands in discord.py allow you to pass a string with spaces as an argument to a command when you surround the argument with double quotes.

## **Reverse engineering**

We go the the GitHub repo for marvin and start looking around the source code. We see that Member.py is where the bot handles commands from users. Looking through the methods for the different bot commands, we notice that some commands takes in input from the user to create a SQL command by inserting arguments with a string formatter `'%s'`. Inserting `' UNION` at the beginning of the argument for a command would then allow the user to insert their own SQL command to query the database (since the ' would lead to an empty string which would give no results). Looking through the avialable bot commands, $info is the only command that can take in arguments from a user and return strings to the user based on the results of an SQL query.

## **SQL command for getting flag**

Using the $challenges command, we see that the marvin challenge is in the database, meaning it's flag is stored there as well. The original SQL query being used is `"SELECT name,category,points,download,access,description FROM challenges WHERE name='%s'"`, so if we send a query like this with flag as a column selected and the name equal to marvin we should get the flag. Sending the bot the command `$info "' UNION SELECT flag,category,points,download,access,description FROM challenges WHERE name='marvin';"` gives us our flag.

osu{GOoD_lUCK_F1Nd1nG_7H15_M4rv1N_wOuLd_neVer_lE4k_4_fl4g}