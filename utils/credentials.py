from enum import Enum
import os

from discord import Object
from dotenv import load_dotenv
load_dotenv()

class Credentials(Enum):
    Token = os.environ.get('TOKEN')
    Guild = Object(id = 951262048011051038)