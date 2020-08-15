import discord
import random
from discord.ext import commands

class Memes(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #memes commands
    @commands.command()
    async def dick(self, ctx):
        dick_owner = ctx.message.author

        if (str(dick_owner) == 'Tqkn#4054'):
            dick_size = 10
        elif (str(dick_owner) == 'Cub.#9136'):
            dick_size = 1
        else:
            dick_size = random.randint(1, 10)

        dick_length = '-' * dick_size
        dick_status = 'Bruh'
        dick_member = str(dick_owner)[:-5]

        if(dick_size >= 5):
            dick_status = "Thats Pog Dude"
        else:
            dick_status = "You Might want to get that checked"

        dick_embed = discord.Embed(
            title = 'Dick Size',
            description = f"**{dick_member}'s** dick is {dick_size} **inches** \n\n8{dick_length}> \n\n{dick_status}",
            colour = discord.Colour.blue()
        )

        await ctx.send(embed=dick_embed)


    @commands.command()
    async def love(self, ctx, member, member2):
        love_chance = random.randint(1, 100)
        
        if (love_chance >= 90):
            embed_colour = discord.Colour.purple()
            love_text = "**Love** at first sight, you're meant for eachother"
        elif (love_chance >= 50):
            embed_colour = discord.Colour.red()
            love_text = "Welp you could make this work if you're not retarded"
        elif (love_chance > 10):
            embed_colour = discord.Colour.blue()
            love_text = "There is a low chance of it happening lmao"
        else:
            embed_colour = discord.Colour.greyple()
            love_text = "There is no chance of this happening you would rather kill eachother than get together"


        
        love_embed = discord.Embed(
            title = 'Love Test',
            description = f'The amount of **love** between \n\n **{member}** and **{member2}** \n\n Is an incredible {love_chance}% \n\n {love_text}',
            colour = embed_colour
        )
        
        love_embed.footer
        await ctx.send(embed=love_embed)


def setup(bot):
        bot.add_cog(Memes(bot))