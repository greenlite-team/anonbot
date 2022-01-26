import discord, hashlib, json, socket
from discord.ext import commands
from mcstatus import MinecraftServer

bot = commands.Bot(command_prefix='an.')
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'{bot.user} online')
    print('----------')

@bot.command()
async def trip(ctx,*,seed):
    tripcode = hashlib.md5(seed.encode("utf")).hexdigest()
    tripcode = "".join(tripcode[:10])
    await ctx.reply(f"Your tripcode: `!{tripcode}`")
    print(f"# {ctx.author} generated the tripcode from '{seed}' to '{tripcode}'")

@bot.command()
async def mcstatus(ctx,ip):
    try:
        server = MinecraftServer(ip,25565)
        status = server.status()
        latency = server.ping()
        query = server.query()
        await ctx.reply(f"""
runs on: `{query.software.brand}`
online: `{status.players.online}/{status.players.max}`
players: `{query.players.names}`
latency: `{int(latency)} ms`
        """)
    except socket.gaierror:
        await ctx.reply("server ip isn't correct")
    except ConnectionRefusedError:
        await ctx.reply("connection refused")
    except OSError:
        await ctx.reply("server responded with no information")
    except socket.timeout:
        await ctx.reply("timed out")

@bot.command()
async def help(ctx):
    await ctx.reply("`an.mcstatus <ip>` for checking minecraft server status\n`an.trip <seed>` for doing microhashes")

# you will need to create a token.json file, and fill it with this:
# {
#     "token": "insert bot token here"
# }
TOKEN = open('token.json')
TOKEN = json.load(TOKEN)
bot.run(TOKEN["token"])