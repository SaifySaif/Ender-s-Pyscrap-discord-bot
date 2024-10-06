import discord
from discord.ext import commands 
import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.all() 
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('bot is online')

@bot.command()
async def repeat(ctx,arg):
    await ctx.send(arg)

@bot.command(aliases=["hi","yo","hey"])
async def hello(ctx):
    await ctx.send(f"Hello there, {ctx.author.mention}")
    embeded_msg = discord.Embed(title = "Hello there", description="description",color = discord.Color.green())
    embeded_msg.set_thumbnail(url =ctx.author.avatar)
    embeded_msg.set_image(url="https://media1.tenor.com/m/0Akz_GWDQyQAAAAC/star-wars-hello-there.gif")
    await ctx.send(embed=embeded_msg)

@bot.command()
async def ping(ctx):
    ping_embed = discord.Embed(title = "Ping",description ="Latency in ms", color = discord.Color.blue())
    ping_embed.add_field(name=f"{bot.user.name}'s latency (ms): ",value=f"{round(bot.latency*1000)} ms")
    await ctx.send(embed=ping_embed)

with open("token.txt") as f:
    token = f.read()

bot.run(token)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

client.run(token)
