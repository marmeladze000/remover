from disnake.ext import commands


class Design(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="design", description='How to make an order?')
    async def design(self, interaction):
        await interaction.response.send_message("If you wanna make an order, create a ticket through this channel: <#1061361207400996904>!")


def setup(bot):
    bot.add_cog(Design(bot))