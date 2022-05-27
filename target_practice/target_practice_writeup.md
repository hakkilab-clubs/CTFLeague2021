# **target_practice**

Category: misc

Points: 500

Downloads: None

Access: None

Description:

Can you help me find the full name of the person behind the alias "anonhunter26"?
This link might be helpful: https://osintframework.com/
Submit flag as osu{firstname_lastname}

## **Finding a friend**

We are given a username to track down as well as a link to a set of OSINT tools. Using the WhatsMyName tool for the OSINT framework we find that anonhunter26 has a twitter account. In one of their tweets them mention the user hatebav2ropc. Using WhatsMyName again we see this user has a github account.

Using the Github User tool in OSINT framework, we can see that hatebav2ropc has the email anonymousfreak32@gmail.com. Using https://epieos.com/ we search this email address to find the owner is Gabriel Cortney.

## **Finding anonhunter26's name**

Googling Gabriel Cortney brings up a Twitter page for them where it shows they work at opticalsocial. A quick google of opticalsocial then shows us a GitHub account for Oswald Denman. This gives us our flag.

osu{Oswald_Denman}