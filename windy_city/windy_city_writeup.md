# **windy_city**

Category: osint

Points: 500

Downloads: None

Access: None

Description:

Can you give the name of the artist who painted the mural that now resides on the left side of this white building? The flag is in the format osu{first_last}

http://chal.ctf-league.osusec.org/windy_city.png

## **Finding the address**

We are given an image of the side of the building we need to locate. Using the Search by Image extension in Firefox, we crop only the building with the art on it and do a reverse search, which leads us to the webpage https://streetartnews.net/2013/08/2501-new-pieces-in-chicago-usa.html where we get an address for the building, South Shore 1706-8 E. 79th street.

## **Finding the artist**

Using Google Maps streetview, we look around the side of the building to find a mural with the words "Culture is Power." A quick Google search of "culture is power chicago mural" brings us to the webpage https://chicago.suntimes.com/murals-mosaics/2020/2/28/21144592/murals-chicago-max-sansing-avalon-park-south-side-graffiti where we find the name of the artist is Max Sansing. This gives us our flag.

osu{Max_Sansing}