import discord
from discord.ext import commands


class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ping
    @commands.hybrid_command(name='ping')
    async def ping(self, ctx):
        f = round(self.bot.latency * 1000)
        await ctx.send('**Ping: **' + str(f) + ' ms')

    # info
    @commands.hybrid_command(name='info')
    async def info(self, ctx, member: discord.Member):

        stat = str(member.status)

        embed = discord.Embed(
            title=member.name,
            description=member.mention,
            color=discord.Color.red()
        )
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Status", value=stat.upper(), inline=False),
        embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d"), inline=False)
        embed.add_field(name="Registered", value=member.created_at.strftime("%Y-%m-%d"), inline=False)
        if len(member.roles) > 1:
            role_string = " ".join([r.mention for r in member.roles][1:])
            embed.add_field(name="Roles[{0}]".format(len(member.roles) - 1), value=role_string, inline=False)
        perm_string = ", ".join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])

        embed.add_field(name="Permissions", value=perm_string, inline=False)
        embed.set_thumbnail(url=member.avatar)
        return await ctx.send(embed=embed)

    # server
    @commands.hybrid_command(name='server')
    async def server(self, ctx):
        description = ctx.guild.description
        created = ctx.guild.created_at.strftime("%Y-%m-%d")
        owner = ctx.guild.owner.mention
        id = ctx.guild.id
        channel = len(ctx.guild.channels)
        text = len(ctx.guild.text_channels)
        voice = len(ctx.guild.voice_channels)
        membercount = ctx.guild.member_count
        level = str(ctx.guild.verification_level).upper()
        roles = str(len(ctx.guild.roles))
        premium = str(ctx.guild.premium_subscription_count)

        embed = discord.Embed(
            title="Server Information",
            description=description or "No description",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=str(ctx.guild.icon.url))
        embed.add_field(name="ID", value=id, inline=False)
        embed.add_field(name="Created At", value=created, inline=False)
        embed.add_field(name="Owner", value=owner, inline=False)
        embed.add_field(name="Verification Level", value=level, inline=False)
        embed.add_field(name="Channels", value=channel, inline=False)
        embed.add_field(name="Text Channels", value=text, inline=True)
        embed.add_field(name="Voice Channels", value=voice, inline=True)
        embed.add_field(name="Total members", value=membercount, inline=False)
        embed.add_field(name="Premium Members", value=premium, inline=False)
        embed.add_field(name="Roles", value=roles, inline=False)

        return await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(GeneralCog(bot))
