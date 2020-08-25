import discord
from discord.ext import commands
import time

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
                description = """Admin Commands \n ```.ban (user) (reason) \n.kick (user) (reason) \n.unban (user) \n.clear (amount) 
                                \n.nick (user) (nick) \n.role (add/remove) (member) (role) \n.roleall (add/remove) (role)```"""
            )
        elif (type == 'memes'):
            help_embed = discord.Embed(
                title = 'Discord Essentials Command List',
                colour = discord.Colour.purple(),
                description = "Meme Commands \n ```.dick \n.love (member 1) (member 2)```"
            )

        await ctx.send(embed=help_embed)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def giveaway(self, ctx, gtime, winners, *, content):

        member = ctx.message.author
        gtime_int = int(gtime[:-1])
        time_decrease = 1

        if 's' in gtime:
            time_change = 5
            time_decrease = 5
            message = 'seconds'
        elif 'm' in gtime:
            time_change = 60
            message = 'minutes'
        elif 'h' in gtime:
            time_change = 3600
            message = 'hours'
        elif 'd' in gtime:
            time_change = 3600 * 248
            message = 'days'
        
        giveaway_embed = discord.Embed(
                title = content,
                colour = discord.Colour.purple(),
                description = f"React with :tada: to enter! \nTime remaining: **{gtime_int}** {message} \nHosted by {member.mention}"
            )
        
        giveaway_embed.set_footer(text=f"{winners} winners")
        msg = await ctx.send(f":tada:  GIVEAWAY  :tada:", embed=giveaway_embed)
        await msg.add_reaction("🎉")

        while (gtime_int > 0):
            time.sleep(time_change)
            gtime_int -= time_decrease
            changed_embed = discord.Embed(
                title = content,
                colour = discord.Colour.purple(),
                description = f"React with :tada: to enter! \nTime remaining: **{gtime_int}** {message} \nHosted by {member.mention}"
            )
            changed_embed.set_footer(text=f"{winners} winners")
            await msg.edit(embed=changed_embed)
         
        



def setup(bot):
    bot.add_cog(Misc(bot))