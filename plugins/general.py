from discord.ext import commands
from discord.commands import slash_command
import data.config as config
from start import intents

# Bot command
bot = commands.Bot(command_prefix=str(config.prefix), case_insensitive=True, heartbeat_timeout=300, intents=intents)

# General test commands
class general(commands.Cog):
    # Slash command example - verifies if slash commands are working
	@slash_command(name='ping',guild_ids=[config.server], description="ping bot to measure latency")
	async def testcommand(self, ctx):
		await ctx.respond(round(bot.latency, 1))

	def __init__(self, bot):
		self.bot = bot
		plugin = str(os.path.basename(__file__)).replace('.py','')

def setup(bot):
	bot.add_cog(general(bot))
