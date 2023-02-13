import os

import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, test_guilds=[1061295231204589640])


@bot.event
async def on_ready():
    print("Bot is ready!")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run("MTA3MTczNTI2NTAwMzA2MTM0OA.GRspfd.YMhK5YS1Qn3dWs8JkPvIdSQ0_6b82ZQx9pxgEc")