import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix="m$")

# ban
@bot.command()
async def test(ctx, msg):
    await ctx.guild.ban(msg)

@bot.event
async def on_ready():
    print("logged in as {0.user}".format(bot))

# @bot.event
# async def on_message(message):
#     # skip self
#     if message.author == client.user: return

if __name__ == '__main__':
    bot.run(config.discord)
