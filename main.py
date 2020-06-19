#Thanks to pythonforengineers for this code.

import praw
import pdb
import re
import os

#Create reddit bot instance
reddit = praw.Reddit('autoBot')

#Load in all replied to posts, not efficent my ass, make it better if you cant live with it. 
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to)) #I don't expect anyone to ask "why list()?", but to anyone that does: pyyyyyyython3!

#Point the bot at r/TOR
subreddit = reddit.subreddit('pythonforengineers')

#Read the 5 newest posts (luckily r/TOR isnt that active)
for submission in subreddit.new(limit=1):
	#Check to ensure we don't spam a post
        if submission.id not in posts_replied_to:
            if re.search("vpn", submission.selftext, re.IGNORECASE): 
                    #FUCK. I need to find a way to ensure it anwsers to only the correct posts, but this is only v0.1, and I am going to need some devs that know best pratices.
                
                #Put everything in a file to make this code just a little more readable, not efficent my ass, if you know how to do it bette, well then do it!
                with open("reply.txt", "r") as f:
                    #Now reply
                    submission.reply(f.read())
                print("Bot replying to: ", submission.title)

                #Add the post to our list
                posts_replied_to.append(submission.id)

#Overwrite the posts_replied_to.txt with current list
with open("posts_replied_to.txt", "w") as f:
    for posts_id in posts_replied_to:
        f.write(posts_id + "\n")
