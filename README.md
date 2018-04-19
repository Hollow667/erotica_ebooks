# erotica_ebooks

This is a twitter bot designed to tweet out titles for non-existent self-published erotica ebooks generated from word lists (the bot tweets these as images). The bot will also reply to anyone who replies to it and can change the content of its reply based on hashtags in the original reply. 

This bot was coded in python. It uses the **tweepy** library to access Twitter's API. It uses the **pillow** library to create images.

***WARNING***
*This bot generates explicit adult content! You must be 18+ to use or modify this bot!*

Flaming Lust Bot does its thing on twitter at [@bot_lust](https://twitter.com/bot_lust).

## features
* **Bot talks back:** replies to users that reply to its tweets
* **Creates and tweets images:** images are in memory only and not stored on drive
* **Formats image text:** includes code that wraps, vertically centers, and resizes text being applied to background image
* **Multi-threaded:** replies are handled separately from regular tweets

## running the bot

The bot uses the python library **tweepy** to access the twitter API. It requires a file called twitterauth.py which is **not** contained in this repo. you must create your own file and include your own twitter authentication codes, obtained from https://apps.twitter.com/.

To run this bot:
```
runbot [-tweet] [-numtweets NUMTWEETS] [-loop] [-test TEST] [-tweettimer TWEETTIMER] [-replytimer REPLYTIMER]
```
All args optional, but you must include **-tweet** if you want the bot to actually tweet what it generates.

Standard command line:
```
$ lust_bot -tweet -loop
```

## me

This bot was inspired by some of the sillier and lower-quality self-published erotica that can be found on sites like smashwords and amazon. I am a self-pubbed erotica writer myself so this is all done with love ;-P

This is my first python program. I am more experienced with strictly-typed object-oriented languages like Java and C#. Please excuse the non-pythonic quirks of my code.

## feel free to fork and steal

I spent way too much time working on this silly bot. Some of the features I've implemented were very poorly documented. I hope that this code can be useful to other python devs trying to do the same things I was. If you are forking or stealing large chunks of code wholesale, please be kind and give me credit and include a link to this repo.
