#Thanks to pythonforengineers for this code.

import praw
import pdb
import re
import os
import time
from datetime import datetime
import feedparser
#from imgur-downloader import ImgurDownloader

#Bot's ending
replyEnd = "\n-----\n\nI am a bot, and this comment was posted automatically.  \nThis bot is Work in progress. [Github](https://github.com/hackerncoder/AutoRepliesBot) (Come help me out).  \n[How does the bot work?](https://reddit.com/r/autorepliesbot/comments/liamo7/how_the_bot_works_and_more/)"

#Create reddit bot instance
reddit = praw.Reddit('autoBot')

#Load in all replied to posts, not efficent my ass, make it better if you cant live with it. 
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
        itemsInList = len(posts_replied_to)
        if itemsInList > 10:
            posts_replied_to = posts_replied_to[-10:]
if not os.path.isfile("mentions_replied_to.txt"):
    mentions_replied_to = []
else:
    with open("mentions_replied_to.txt", "r") as f:
        mentions_replied_to = f.read()
        mentions_replied_to = mentions_replied_to.split("\n")
        mentions_replied_to = list(filter(None, mentions_replied_to))
if not os.path.isfile("torblog.txt"):
    torblog = []
else:
    with open("torblog.txt", "r") as f:
        torblog = f.read()
        torblog = torblog.split("\n")
        torblog = list(filter(None, torblog))
if not os.path.isfile("imgur_replied_to.txt"):
    imgur_replied_to = []
else:
    with open("imgur_replied_to.txt", "r") as f:
        imgur_replied_to = f.read()
        imgur_replied_to = imgur_replied_to.split("\n")
        imgur_replied_to = list(filter(None, imgur_replied_to))

#Point the bot at r/TOR
subreddit = reddit.subreddit('tor')

#Read the 5 newest posts (luckily r/TOR isnt that active)
while True: 
    for submission in subreddit.new(limit=5):
    
        #Check to ensure we don't spam a post
        if submission.id not in posts_replied_to:
        
            #if submission.link_flair_text == "FAQ": #Remove the VPN FAQ, I don't want to deal with it.

                #if re.search("vpn", submission.selftext, re.IGNORECASE):
                        #RE is regex, anyone that knows regex please help create a string that correctly identifies posts.

                    #Check for markers for anti-vpn (don't want to add a comment saying VPN bad to someone saying they aren't using vpn).
                    #"Recommend(ed)" Is not fun to do, you could phrase it in so many ways. Check the added txt file - HkrNCdr
                    #if not re.search("don(\')*t use( a)* vpn|\
                    #    didn(\')*t use( a)* vpn|\
                    #    should(n(\')*t| not) (be )*us(e|ing) (a )*vpn|\
                    #    not using( a)* vpn|\
                    #    will not( be)* us(e|ing)( a)* vpn|\
                    #    orbot vpn", submission.selftext, re.IGNORECASE):
            
                        #Put everything in a file to make this code just a little more readable.
                    #    with open("vpnReply.txt", "r") as f:
                    
                            #Now reply
                    #        submission.reply(f.read() + replyEnd)
                            
                        #Add the post to our list
                    #    posts_replied_to.append(submission.id)
            if re.search("ios|iphone", submission.title, re.IGNORECASE):
                with open("mobileReply.txt", "r") as f:
                    replyText = "Hello! I couldn't help but notice that you put IOS or Iphone in your title. Many people ask about how to install Tor on IOS, so I would just answer that question.\n\n------\n\n"
                    for i, line in enumerate(f):
                        if i > 2 and i < 9:
                            replyText += line
                    submission.reply(replyText + replyEnd)
                posts_replied_to.append(submission.id)            

            #if submission.id not in imgur_replied_to:
            #    imgurlink = re.search("imgur\.com\/(.......)", submission.selftext, re.IGNORECASE)
            #    if imgurlink:
            #        downloader = ImgurDownloader("https://imgur.com/" + imgurlink.group(1))
            #        downloader.save_images()

            #        arbSub = reddit.subreddit('autorepliesbot')
            #        arbSubmission = arbSub.submit_image(title="imgur image for " + submission.id, image_path=fn)
                    
            #        replyText = "It seems you have linked to an imgur image, Tor Browser and imgur don't play nicely, so I've reuploaded the image here: " + arbSubmission.permalink
            #        submission.reply(replyText + replyEnd)
            #        os.remove(fn)
            #        imgur_replied_to.append(submission.id)

    for mention in reddit.inbox.mentions(limit=10):
        if not mention.id in mentions_replied_to:
            if re.search("u\/AutoRepliesBot.{0,4}(ios)", mention.body, re.IGNORECASE):
                   with open("mobileReply.txt", "r") as f:
                    replyText = ""
                    for i, line in enumerate(f):
                        if i > 2 and i < 9:
                            replyText += line
                    mention.reply(replyText + replyEnd)
            
            elif re.search("u\/AutoRepliesBot.{0,4}(android)", mention.body, re.IGNORECASE):
                with open("mobileReply.txt", "r") as f:
                    replyText = ""
                    for i, line in enumerate(f):
                        if i > 10 and i < 23:
                            replyText += line
                    mention.reply(replyText + replyEnd)
            
            elif re.search("u\/AutoRepliesBot.{0,4}(mobile)", mention.body, re.IGNORECASE):
                with open("mobileReply.txt", "r") as f:
                    mention.reply(f.read() + replyEnd)
            
            elif re.search("u\/AutoRepliesBot.{0,4}letterboxing", mention.body, re.IGNORECASE):
                with open("letterboxingReply.txt", "r") as f:
                    mention.reply(f.read() + replyEnd)
            elif re.search("u\/AutoRepliesBot.{0,4}(blocked|tor blocking website(s)*)", mention.body, re.IGNORECASE):
                with open("blockingReply.txt", "r") as f:
                    mention.reply(f.read() + replyEnd)
            #else:
            #    with open("vpnReply.txt", "r") as f:
            #        mention.reply(f.read() + replyEnd)
            mentions_replied_to.append(mention.id)

    #Overwrite the posts_replied_to.txt with current list
    with open("posts_replied_to.txt", "w") as f:
        for posts_id in posts_replied_to:
            f.write(posts_id + "\n")
    with open("mentions_replied_to.txt", "w") as f:
        for mention_id in mentions_replied_to:
            f.write(mention_id + "\n")
    with open("imgur_replied_to.txt", "w") as f:
        for imgur_id in imgur_replied_to:
            f.write(imgur_id + "\n")

    TorBlogFeed = feedparser.parse("https://blog.torproject.org/feed")
    entry = TorBlogFeed.entries[0]
    if re.search("new release: tor browser", entry.title, re.IGNORECASE):
        if entry.link not in torblog:
            releaseSubmission = subreddit.submit(entry.title, url=entry.link)
            releaseSubmission.mod.flair("Software release", "", "8eb3a66a-9766-11e9-9c49-0e5278b79bf6")
            torblog.append(entry.link)
            print("posted "+entry.link)
            with open("torblog.txt", "w") as f:
                f.write(entry.link)
    
    time.sleep(120)
