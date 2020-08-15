import asyncio
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="^", help_command=None, self_bot=True)

class SelfBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def embed(self, ctx, *, message):

        embed_message = discord.Embed(
            title = "Tqkns Message",
            description = f'{message}',
            colour = discord.Colour.purple()
        )

        await message.delete()
        await ctx.send(embed=embed_message)
        


client.add_cog(SelfBot(client))
client.run("MjQ3NjIzMzAxMjc3NDE3NDcy.XwxH_w.sGY_q17m5A5HRlVSBVoS8eP5Qp8", bot=False)