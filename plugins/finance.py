import discord
from discord.ext import commands
from discord.commands import slash_command
import sys
import os
import pandas as pd
import pandas_datareader as web
import datetime as dt
import data.config as config
import ffn
import matplotlib
import matplotlib.pyplot as plt
import ystockquote

# Filename adjustments
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# Financial Functions - set of commands pertaining to class finance
class finance(commands.Cog):
    
	# Return csv slash command - return a csv file of price data within a time period given a tickerData
	@slash_command(name='return_csv', guild_ids=[config.server], description="Returns a csv file of price data within a time period given a ticker")
	async def return_csv(self, ctx, ticker, start, end):
		# Set start and end dates as given
		start = dt.datetime.strptime(start, '%Y-%m-%d')
		end = dt.datetime.strptime(end, '%Y-%m-%d')
        
		# get historical price data from ticker and send it to a csv
		tickerData = web.DataReader(ticker, 'yahoo', start, end)
		tickerData.to_csv('./plugins/data.csv')
        
		# send csv file
		await ctx.send(file=discord.File('./plugins/data.csv', filename='data.csv'))
		await ctx.respond(f'File of {ticker} price data from {start} to {end}.')
	
	# Return a chart using matplotlib
	@slash_command(name='chart', guild_ids=[config.server], description="returns the chart of given ticker(s) within start and end dates")
	async def chart(self, ctx, ticker, start, end):
		# Set start and end variables as datetimes
		start = dt.datetime.strptime(start, '%Y-%m-%d')
		end = dt.datetime.strptime(end, '%Y-%m-%d')

		# read given ticker data through pandas_datareader
		df = web.DataReader(ticker, 'yahoo', start, end)

		# plot adjusted close and save it to temp.png
		df['Adj Close'].plot()
		plt.savefig('temp.png')

		# send out price graph of given ticker within start and end dates
		await ctx.send(file=discord.File('temp.png', filename=f'{ticker}_graph.png'))
		await ctx.respond(f'File of {ticker} price graph from {start} to {end}.')
        
	# Return relevant statistics using ffn() module
	@slash_command(name='stats', guild_ids=[config.server], description="returns elaborate statistics of the of given ticker(s) within start and end dates")
	async def stats(self, ctx, ticker, start, end):
        # get prices
		prices = ffn.get(ticker, start=start, end=end)

		# calculate and display stats
		stats = prices.calc_stats()
		
		#stats = stats.display()
		
		await ctx.respond(str((stats)))

    # Obtain the live price of a given ticker
	@slash_command(name='live', guild_ids=[config.server], description="returns the real time price of a given ticker")
	async def live(self, ctx, ticker):
		
		# respond with real time yahoo finance price using ystockquote
		await ctx.respond(str(ystockquote.get_price_book(str(ticker))))

	def __init__(self, bot):
		self.bot = bot
		plugin = str(os.path.basename(__file__)).replace('.py','')

def setup(bot):
	bot.add_cog(finance(bot))
