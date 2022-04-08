import os
from pathlib import Path


import discord
from discord.ext import commands


from .MathBotTree import MathBotTree
from utils import CogLoadFailure, Credentials

class MathBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True


        super().__init__(command_prefix='!', intents=intents, tree_cls=MathBotTree, application_id = 962076060567085196)

    
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


    async def setup_commands(self):
        for file in Path('cogs').glob('**/*.py'):
            *tree, _ = file.parts
            try:
                if not file.stem.startswith('_'):
                    cog = f"{'.'.join(tree)}.{file.stem}"
                    await self.load_extension(cog)
                    print(f"{cog} loaded successfully!")

            except Exception as e:
                raise CogLoadFailure(file.stem, e)
        
        await self.tree.sync(guild=Credentials.Guild.value)

    
    async def setup_hook(self) -> None:
        self.activity = discord.Activity(name = 'your math skills', type = discord.ActivityType.watching)
        self.status = discord.Status.online
        await self.setup_commands()


    async def run(self):
        try:
            async with self:
                await self.start(Credentials.Token.value)
        except KeyboardInterrupt:
            await self.close()