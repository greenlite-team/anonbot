import discord, hashlib, json
from discord.ext import commands

bot = commands.Bot(command_prefix='a#')
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
async def help(ctx):
    await ctx.reply("you can generate tripcodes with `a#trip {seed}`\n(note that these aren't 4chan-usable tripcode hashes, i just threw up this code in 2 minutes)")

# you will need to create a token.json file, and fill it with this:
# {
#     "token": "insert bot token here"
# }
TOKEN = open('token.json')
TOKEN = json.load(TOKEN)
bot.run(TOKEN["token"])