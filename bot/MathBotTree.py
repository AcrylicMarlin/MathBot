from discord.app_commands import CommandTree, AppCommandError, ContextMenu
from discord.ext.commands import Command
from discord import Interaction
from typing import Optional, Any, Union
# import logging
import sys
import traceback

from utils import ErrorEmbed


class MathBotTree(CommandTree):
    def __init__(self, client):
        super().__init__(client)

    async def on_error(self, interaction: Interaction, command: Optional[Union[ContextMenu, Command[Any, ..., Any]]], error: AppCommandError) -> None:
        embed = ErrorEmbed(error)
        await interaction.channel.send(embed = embed)
        
        print('Ignoring {} in command {}:'.format(type(error), command.name), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        # logging.error(f'Ignoring {type(error)} in command {command.name}: {error}')