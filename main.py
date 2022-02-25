import discord, config
bot = discord.Client()
@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
@bot.event
async def on_raw_reaction_add(reaction):
    if reaction.channel_id == 938541973969723463 and reaction.emoji.name == '✅' and not reaction.member.bot:
        await reaction.member.add_roles(bot.get_guild(931758960233574420).get_role(938530726092087367))

@bot.event
async def on_message(message):
    if message.content.lower().strip() == 'shark':
        await message.add_reaction('🦈')
        
if __name__ == '__main__':
    bot.run(config.discord)
