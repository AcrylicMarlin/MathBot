import asyncio
from bot import MathBot

client = MathBot()

if __name__ == '__main__':
    asyncio.run(client.run())