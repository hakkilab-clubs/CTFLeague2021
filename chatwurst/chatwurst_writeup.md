# **chatwurst**

Category: rev

Points: 400

Downloads: http://chal.ctf-league.osusec.org/chatwurst.apk

Access: None

Description:

We have received intel that a group of 1337 haxxors are using a little known app called 'chatwurst'. One of the hackers goes by the name 'FizzbuzzMcFlurry', and we're sure that these hackers are up to no good. Can you get into their chat and figure out what's going on?

## **Reverse engineering**

Using jadx we load in the provided apk and start looking at MainActivity. Here we see some functions for logging in and signing up that reference ChatwurstClient. Looking at ChatwurstClient we see many fuctions for making POST requests with JSON content to different endpoints to get information on users, groups, and messages.

## **Investigating user creation**

Using https://reqbin.com/ we send some POST requests to create users using the http://chatwurst.ctf-league.osusec.org/create_user endpoint and setting the content as `{"username": user, "password": pass}` with different values for user and pass. We see that the response is `{"user_id": id}` where id increments each time we make a user. This means we can just iterate through indices to find the user id for FizzbuzzMcFlurry.

## **Finding the correct user id**

We start sending some POST requests to get groups using the http://chatwurst.ctf-league.osusec.org/get_groups endpoint and setting the content as `{"credential": {"username": user, "password": pass}, "user_id": id}` where user and pass are values we previously sent to the create user endpoint and id is incremented each time. On user id 3, we see all groups contain FizzbuzzMcFlurry, so this is their user id.

## **Finding all messages for FizzbuzzMcFlurry**

Now we send POST requests to get messages using the http://chatwurst.ctf-league.osusec.org/get_messages endpoint and set the content as `{"credential": {"username": user, "password": pass}, "group_id": id}` where user and pass are again values we previously sent to the create user endpoint and id is one of the group ids for the groups FizzbuzzMcFlurry is in. As we go through messages we see that the flag is in the messages for group id 9.

osu{cH4TWUrst_m0RE_L1KE_wUrSt_ch47}