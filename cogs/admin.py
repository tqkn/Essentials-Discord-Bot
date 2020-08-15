import discord
import random
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #admins commands
    
    @commands.command()
    @commands.has_permissions(ban_members = False)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.member, *, reason = None):
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name and user.discriminator) == (member_name and member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.metion}")
                return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = '5'):

        if (amount == 'all'):
            await ctx.channel.purge(limit = 300)
        else:
            await ctx.channel.purge(limit = int(amount) + 1)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member : discord.member, nick):
        try:
            await member.edit(nick=nick)
            await ctx.send(f'Nickname was changed for {member.mention} ')
        except PermissionError:
            await ctx.send(f"Can't Nick {member.mention} Insufficient Permissions")

def setup(bot):
    bot.add_cog(Admin(bot))
