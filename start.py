import datetime
import data.config as config
from os import listdir
from os.path import isfile, join

import discord
from discord.ext import commands
from discord import slash_command

# add required intents like message_content
intents = discord.Intents.default()
intents.message_content = True

# discord bot variable
bot = commands.Bot(command_prefix=str(config.prefix), case_insensitive=True, heartbeat_timeout=300, intents=intents)

# removes default help command so you can make your own
bot.remove_command("help")

# state cogs (classes used) here
cogs = ['finance', 'general']

# Bot action on startup
@bot.event
async def on_ready():
	print(f'\n{bot.user} online @ {str(datetime.datetime.now())}')
	print(f'prefix: {str(config.prefix)}')

	#print("\ninvite link:\nhttps://discordapp.com/oauth2/authorize?&client_id=" + str(bot.user.id) + "&scope=applications.commands%20bot&permissions=8\n")

# global command error handler
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		pass
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("missing required argument")
	elif isinstance(error, commands.BadArgument):
		await ctx.send("missing required argument")
	else:
		print(error, ctx)

# Load cogs mentioned in list to add to command list
for cog in cogs:
	bot.load_extension('plugins.' + cog) # loads in each file, Cog, that is defined in the list

# if name of script equals to main, run the bot
if __name__ == "__main__":
	bot.run(config.discordtoken)
