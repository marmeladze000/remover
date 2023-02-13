import datetime

import disnake
from disnake.ext import commands


class Timeout(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command()
    async def timeout(self, interaction, member: disnake.Member, time: str, reason: str):
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        await member.timeout(reason=reason, until=time)
        await interaction.response.send_message(f"Timed out {member.mention} for {time} for {reason}", ephemeral=True)

    @commands.slash_command()
    async def untimeout(self, interaction, member: disnake.Member,):
        await member.timeout(reason=None, until=None)
        await interaction.response.send_message(f"Untimed out {member.mention}", ephemeral=True)

def setup(bot):
    bot.add_cog(Timeout(bot))