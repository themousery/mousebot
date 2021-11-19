import discord
from discord.ext import commands
import config
import json

bot = commands.Bot(command_prefix="m$")

# revoke watts pass
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def wattspass(ctx, user: discord.Member):
    watts_pass = discord.utils.get(ctx.guild.roles, name="watts-pass")
    await user.remove_roles(watts_pass)
    await ctx.send("revoked watts pass from {0.name}".format(user))

@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))

# example for responding to messages
@bot.event
async def on_message(message):
    # skip self
    if message.author == client.user: return
    # respond with

if __name__ == '__main__':
    bot.run(config.discord)
