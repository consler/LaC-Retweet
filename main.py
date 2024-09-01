import discord
import asyncio
from bot import check
import time
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    timer=0
    channel = client.get_channel(1252175281821585489)
    time.sleep(1)
    while True:
        result = await check()

        if not result is None:
            await channel.send(result)
            timer = 0
        else:
            timer = timer + 1
            if timer == 180:
                print("I am alive")
                timer = 0

        time.sleep(60)

client.run(TOKEN)
