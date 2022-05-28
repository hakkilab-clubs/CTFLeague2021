# **shallow_mind**

Category: misc

Points: 200

Downloads: http://chal.ctf-league.osusec.org/shallow_mind.zip

Access: http://shallow_mind.ctf-league.osusec.org/

Description:

We suspect that the Shallow Mind R&D Branch of Maldiant has been lying to investors. Can you check to see if their image recognition program is really all that?

## **Reverse engineering**

We start by looking at the provided`server.py` code. Here we see two endpoints for the server, authtest and classify. In order to use the classify endpoint, we need a passcode. Luckily, the authtest endpoint sends us this pass code when we run `fetch('/authtest', {method:'POST', body:JSON.stringify({"admin": "password", "devcode": null})})` in the browser console, since the devcode was never changed from `None` in `server.py`. The passcode is `"yxB5X7{G(<,:;kJR"`, and when we use this in a fetch request like `fetch('/classify', {method:'POST', body:JSON.stringify({"admin": "yxB5X7{G(<,:;kJR", "pic": URL})})` where URL is an image online, we can get a classification from the server. When the model responds with an answer of "flag", we will ge the flag.

Looking in `model.py`, we see that the answer is "flag" when the model classifies an image as green when it actually has more red in it, or if the model classifies the image as red when it actually has more green in it. So we need to find an image that will confuse the model.

## **Confusing the model**

After trying a variety of images, we find that the image at the URL https://i.etsystatic.com/15532180/r/il/322fab/1642808928/il_570xN.1642808928_shu4.jpg works to confuse the model, and we get our flag.

osu{1_d0nt_kn0w_h0w_2_tr41n_nu3r4l_n3t5}