import os
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()
access_token = os.getenv('TWITCH_ACCESS_TOKEN')

twitch_log_filepath = 'twitch_chat_log.txt'

with open(twitch_log_filepath,'w') as f:
    f.write("")

class Bot(commands.Bot):

    queue = None

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=access_token, prefix='', initial_channels=['vincimus_omnes'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # self.queue.put(message.content)
        # print(message.content)
        with open(twitch_log_filepath,'a') as f:
            f.write(message.content + '\n')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()