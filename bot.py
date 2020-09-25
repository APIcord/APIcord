import time
import discord
from discord.ext import commands
import flask
import json
import urllib3
import keep_alive


# Token and prefix
token = ("[token]")
prefix = ("api!")
# Color chooser
color = ("red")
# Options: red, white, black, grey, blue_metalic, green, light_blue & yellow


# Start stuff
bot = commands.Bot(command_prefix=prefix, allowed_mentions=discord.AllowedMentions(roles=False, users=False, everyone=False))
embed = discord.Embed
http = urllib3.PoolManager()
print("APIcord")
print("Logs:")


# Color
if color == ("red"):
  botcolor= (0xff0000)
elif color == ("grey"):
  botcolor = (0xffffff)
elif color == ("white"):
  botcolor = (0xffffff)
elif color == ("black"):
  botcolor == (0x000000)
elif color == ("blue_metalic"):
  botcolor = (0xfff)
elif color == ("green"):
  botcolor == (0xff000)
elif color == ("light_blue"):
  botcolor = (0x00fbff)
elif color == ("yellow"):
  botcolor = (0xffee00)
elif color == ("orange"):
  botcolor = (0xff8800)
# Status
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="APIs | " + prefix + "commands"))
# Good part

@bot.command()
async def nice(ctx):
  await ctx.send("Thank you! You're nice too 👍")

@bot.command()
async def commands(ctx):
  embed=discord.Embed(title="APIcord", description="Help", color=botcolor)
  embed.add_field(name=prefix + "chucknorris", value="Random Chuck Norris Joke", inline=True)
  embed.add_field(name=prefix + "say", value="The bot says 1 word for you", inline=True)
  embed.add_field(name=prefix + "hug", value="A hug, for you, my friend", inline=True)
  embed.add_field(name="Meme commands", value=prefix + "meme", inline=False)
  embed.add_field(name=prefix + "meme meme", value="Random meme", inline=True)
  embed.add_field(name=prefix + "meme reddit", value="Random Reddit meme", inline=True)
  embed.add_field(name="Image commands", value=prefix + "img", inline=False)
  embed.add_field(name=prefix + "img coffee", value="Random coffee image", inline=True)
  embed.add_field(name=prefix + "img dog", value="Random dog image", inline=True)
  embed.add_field(name=prefix + "img cat", value="Random cat image", inline=True)
  embed.add_field(name=prefix + "img panda", value="Random panda image", inline=True)
  embed.add_field(name=prefix + "img red_panda", value="Random red panda image", inline=True)
  embed.add_field(name=prefix + "img bird", value="Random bird image", inline=True)
  embed.add_field(name=prefix + "img fox", value="Random fox image", inline=True)
  embed.add_field(name=prefix + "img koala", value="Random koala image", inline=True)
  embed.add_field(name="Facts", value=prefix + "fact", inline=False)
  embed.add_field(name=prefix + "fact cat", value="Random cat fact", inline=True)
  embed.add_field(name="About the bot", value="No prefix", inline=False)
  embed.add_field(name=prefix + "about", value="Credits", inline=True)
  embed.add_field(name=prefix + "license", value="License", inline=True)
  embed.add_field(name=prefix + "invite", value="Displays bot invite", inline=True)
  embed.add_field(name=prefix + "privacy", value="Bot Privacy Policy", inline=True)
  embed.add_field(name=prefix + "code", value="Source code", inline=True)
  embed.add_field(name=prefix + "commands", value="Displays commands", inline=True)
  embed.add_field(name=prefix + "botstats", value="Bot stas", inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def img(ctx, something):
  if something == "coffee":
    jdat = (http.request('GET', 'https://coffee.alexflipnote.dev/random.json'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Here you have your coffee"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['file']))
    await ctx.send(embed=embed)
  elif something == "dog":
    jdat = (http.request('GET', 'https://dog.ceo/api/breeds/image/random'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("A doggo! :D"), description=("I wish you'll like this uwu"), color=(botcolor))
    embed.set_image(url=(jsdata['message']))
    await ctx.send(embed=embed)
  elif something == "cat":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/cat'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("A cat! :D"), description=("kittens & adult kittens"), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await ctx.send(embed=embed)
  elif something == "panda":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("p a n d a"), description=("kittens & adult kittens"), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await ctx.send(embed=embed)
  elif something == "red_panda":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/red_panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("red panda :)"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await ctx.send(embed=embed)
  elif something == "bird":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/birb'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("*bird sounds.mp3*"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await ctx.send(embed=embed)
  elif something == "fox":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/fox'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Finnegan Fox aproves it."), description=("(I think)"), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await ctx.send(embed=embed)
  elif something == "koala":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/koala'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("a"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await ctx.send(embed=embed)

@bot.command()
async def fact(ctx, factstuff):
  if factstuff == "cat":
    jdat = (http.request('GET', 'https://catfact.ninja/fact'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    await ctx.send(embed=embed)

@bot.command()
async def chucknorris(ctx):
    jdat = (http.request('GET', 'https://api.chucknorris.io/jokes/random'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=(jsdata['value']), url=(jsdata['url']), description=(""), color=(botcolor))
    embed.set_thumbnail(url=(jsdata['icon_url']))
    await ctx.send(embed=embed)
  
@bot.command()
async def hug(ctx):
    jdat = (http.request('GET', 'https://some-random-api.ml/animu/hug'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    await ctx.send(jsdata['link'])

@bot.command()
async def meme(ctx, memetype):
  if memetype == "meme":
    jdat = (http.request('GET', 'https://some-random-api.ml/meme'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=(jsdata['caption']), description=(""), color=(botcolor))
    embed.set_image(url=jsdata['image'])
    await ctx.send(embed=embed)
  elif memetype == "reddit":
    jdat = (http.request('GET', 'https://meme-api.herokuapp.com/gimme'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    if jsdata['nsfw'] == "true":
      embed=discord.Embed(title=("This meme is NSFW"), description=("We're going to reload this command, sorry for the incombinient."), color=(botcolor))
      await ctx.send(embed=embed)
      await ctx.send(prefix + "reddit")
    else:
      #Embed
      embed_two=discord.Embed(title=(jsdata['title']), url=(jsdata['postLink']), description=(""), color=(botcolor))
      # embed_two.set_author(name=(jsdata['author']), url=("https://reddit.com/u/" + jsdata['author']), icon_url=("https://www.redditstatic.com/desktop2x/img/favicon/android-icon-192x192.png"))
      embed_two.set_thumbnail(url="https://www.redditstatic.com/desktop2x/img/favicon/favicon-32x32.png")
      embed_two.add_field(name="Posted by:", value=("u/" + jsdata['author']), inline=(True))
      embed_two.add_field(name="Subreddit:", value=("r/" + jsdata['subreddit']), inline=(True))
      embed_two.set_image(url=jsdata['url'])
      await ctx.send(embed=embed_two)

@bot.command()
async def invite(ctx):
  await ctx.send("You can invite me to your server clicking in this link: https://apicord.github.io/invite")

@bot.command()
async def about(ctx):
  embed=discord.Embed(title=("APIcord Alpha 2.1"), description=("Credits"), color=(botcolor))
  embed.add_field(name=("Creator and programmer"), value=("LT#5266"), inline=(False))
  embed.add_field(name=("APIs"), value=("used in this project"), inline=(False))
  embed.add_field(name=(prefix + "img coffee"), value=("Coffee API by Alex Flipnote"), inline=(True))
  embed.add_field(name=(prefix + "img dog"), value=("Dog API by Elliott Landsborough, Eduard Moya & Kathie Wu"), inline=(True))
  embed.add_field(name=(prefix + "fact cat"), value=("Cat Facts API (catfact.ninja)"), inline=(True))
  embed.add_field(name=(prefix + "meme reddit"), value=("Meme API by Dev Daksan"), inline=(True))
  embed.add_field(name=(prefix + "Some Random Api"), value=("by Seif Mansour, Taka Inzori, Excigma & Telk"), inline=(False))
  embed.add_field(name=(prefix + "Some Random Api"), value=("by Seif Mansour, Taka Inzori, Excigma & Telk"), inline=(True))
  embed.add_field(name=("Commands"), value=("img cat, " + prefix + "img panda, " + prefix + "img red panda " + prefix + "img bird, " + prefix + "img fox, " + prefix + "img koala, " + prefix + "meme meme & " + prefix + "hug"), inline=(True))
  embed.set_footer(text="Thanks to Polking to follow the development and Discord Extreme List guys for some help")
  await ctx.send(embed=embed)

@bot.command()
async def license(ctx):
  embed=discord.Embed(title=("APIcord Licenses"), description=(""), color=(botcolor))
  embed.add_field(name=("APIcord"), value=("Boost Software License 1.0"), inline=(True))
  embed.add_field(name=("Coffee API"), value=("MIT License (© 2020 AlexFlipnote)"), inline=(True))
  embed.add_field(name=("Dog CEO Image Library"), value=("GNU General Public License v3.0"), inline=(True))
  embed.add_field(name=("Meme API"), value=("MIT License (© 2020 Dev Daksan P S)"), inline=(True))
  embed.add_field(name=("Some Random Api (SRA)"), value=("Apache License 2.0"))
  await ctx.send(embed=embed)

@bot.command()
async def privacy(ctx):
  await ctx.send("https://apicord.github.io/privacy")

@bot.command()
async def code(ctx):
  await ctx.send("https://github.com/L64/APIcord")

@bot.command()
async def say(ctx, yourmessage):
  await ctx.send(yourmessage)

@bot.command()
async def botstats(ctx):
  embed=discord.Embed(title=("Bot stats"), description="", color=botcolor)
  embed.add_field(name=("Bot used in"), value=(f"{len(bot.guilds)} servers"), inline=(True))
  await ctx.send(embed=embed)


@bot.command()
async def polking(ctx):
  embed=discord.Embed(title="**MonsterWorld**", url="https://discord.com/oauth2/authorize?client_id=756602085298143412&scope=bot&permissions=2147483647", description="Bot recomendado", color=botcolor)
  await ctx.send(embed=embed)
@bot.command()
async def egg(ctx):
  await ctx.send('🥚')
@bot.command()
async def BigF(ctx):
  await ctx.send("FFFFFFFFFF \n FFFFFFFFFF \n FFF \n FFFFFF \n FFFFFF \n FFF \n FFF \n FFF")
@bot.command()
async def SmolF(ctx):
  await ctx.send("**f** (:-) aww, a small F, this is cute uwu)")
@bot.command()
async def reeeeee(ctx):
  await ctx.send("**REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE**")
@bot.command()
async def thereisanimpostoramongus(ctx):
  await ctx.send("**ඞ There is an impostor among us ඞ**")
@bot.command()
async def DEL(ctx):
  await ctx.send("Discord Extreme List, i don't know who is but, sounds like a nice name :)")
keep_alive.keep_alive()
bot.run(token)
# I don't know how to make a totally functional bot ._.
