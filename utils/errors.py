class MathBotError(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class CogLoadFailure(MathBotError):
    def __init__(self, cog:str, reason:Exception):
        super().__init__("Cog {} failed to load.\nReason: {}".format(cog, reason))