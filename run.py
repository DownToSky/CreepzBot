import discord
import asyncio
import logging

bot = discord.Client()
bot.logger=logging.getLogger("discord")
bot.logger.setLevel(logging.DEBUG)
bot.handler=logging.FileHandler(filename="discord.log",encoding="utf-8",mode='w')
bot.handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s"))
bot.logger.addHandler(bot.handler)

async def update_config_task():
    await bot.wait_until_ready()
    
    while not bot.is_closed:
        await asyncio.sleep(60)

@bot.event
async def on_message(message):
    pass

@bot.event
async def on_ready():
    print("Connected")
    print("As {}")
    print("_________")

client.loop.creat_task(update_config_task())
client.run("email","password)"
