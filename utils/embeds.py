from discord import Embed, Colour

class ErrorEmbed(Embed):
    def __init__(self, error: Exception):
        super().__init__(title = 'Error', description = f"```{str(error)}```", colour = Colour.red())
        # self.set_footer(text = 'MathBot', icon_url="")