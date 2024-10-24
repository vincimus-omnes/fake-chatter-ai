from scripts.youtube_bot import start_youtube_bot
from scripts.twitch_chat import Bot
import multiprocessing

def load_bots():
    twitch_bot = Bot()
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=twitch_bot.run(), args=(q))
    p.daemon = True
    p.start()
    # youtube_bot = start_youtube_bot() # What I really want is an instance of the bot but let's see if this works somehow
    
    return p
# It's possible the simplest way to do this is to just run 3 bots and output the chat messages to file
# It's not very cool though

# I already know if I run this it won't do what I want and I'm not sure how to track it after I run it.

# Definitely the simplest way is just reading files and running separate processes