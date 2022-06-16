# This example requires the 'message_content' intent.
import os
import discord
from discord.ext import commands
from discord.ext.commands import bot
import markov

token = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

bot = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Gronk say hello!')
    if message.content.startswith('goodbye'):
        await message.channel.send('Gronk say byeee!')
    text = message.content
        
    res = markov.main(text)
    await message.channel.send(f"{res}")

@bot.command(pass_context=True)
async def on_message(message):
    channel = bot.get_channel("987085235369963590")
    if message.content.startswith('test'):
        await channel.send("Test worked!")


client.run(token)