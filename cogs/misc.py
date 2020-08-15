import discord
from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx, type = 'all'):
        if (type == 'all'):
            help_embed = discord.Embed(
                title = 'Discord Essentials Command List',
                colour = discord.Colour.purple(),
                description = "List of aviable help commands for Discord Essentials",
            )

            help_embed.add_field(name=':blue_book: Misc', value='`.help misc`')
            help_embed.add_field(name=':tools: Admin', value='`.help admin`')
            help_embed.add_field(name=':tada: Memes', value='`.help memes`')
        elif (type == 'info'):
            help_embed = discord.Embed(
                title = 'Discord Essentials Command List',
                colour = discord.Colour.purple(),
                description = "Misc Commands \n ```.help (option) \n.info ```"
            )
        elif (type == 'admin'):
            help_embed = discord.Embed(
                title = 'Discord Essentials Command List',
                colour = discord.Colour.purple(),
                description = "Admin Commands \n ```.ban (user) (reason) \n.kick (user) (reason) \n.unban (user) \n.clear (amount) \n.nick (user) (nick) ```"
            )
        elif (type == 'memes'):
            help_embed = discord.Embed(
                title = 'Discord Essentials Command List',
                colour = discord.Colour.purple(),
                description = "Meme Commands \n ```.dick \n.love (member 1) (member 2)```"
            )

        await ctx.send(embed=help_embed)

def setup(bot):
    bot.add_cog(Misc(bot))