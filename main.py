import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False

TOKEN = "MTE2ODU3NzgzNDkwNjgyMDY0OA.GQlktg.MhRLG26QkaMfmveHGW8oor6L_UuMMNxesZ118A"

bot = commands.Bot(command_prefix='!', intents= intents)

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name}')


@bot.command()
async def hello(ctx):
	print("Command 'hello' invoked.")
	await ctx.send(f'Hello {ctx.author.name}!')

bot.run(TOKEN)