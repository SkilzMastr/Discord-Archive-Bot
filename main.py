import discord,os,dotenv
from discord.ext import commands
dotenv.load_dotenv()

prefix = '.'
TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix=prefix)

channels = []
linkparts = ["http://", "https://"]


@client.event
async def on_ready():
    print("Bot Ready")


@client.event
async def on_message(message):
    
    if message.content[0] == prefix:
        await client.process_commands(message)
    elif message.channel in channels:
        for part in linkparts:
            if part in message.content:
                print("Found Link Part")
                break

@client.command(name="archive", aliases=["arch", "a"])
async def archive(ctx):
    print("Adding....")
    channels.append(ctx.channel)



client.run(TOKEN)