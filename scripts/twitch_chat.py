import os
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()
access_token = os.getenv('TWITCH_ACCESS_TOKEN')


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=access_token, prefix='', initial_channels=['vincimus_omnes'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        print(message.content)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')


# bot = Bot()
# bot.run()