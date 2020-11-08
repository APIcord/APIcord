import time
import discord
from discord.ext import commands
import json
import urllib3
import keep_alive


# Token and prefix
token = ("[token]")
prefix = ("api!")
# Color chooser
color = ("red")
# Options: red, white, black, grey, blue_metalic, green, light_blue, yellow, orange_light


# Start stuff
bot = commands.Bot(command_prefix=prefix, description="Discord bot focused on APIs", allowed_mentions=discord.AllowedMentions(roles=False, users=False, everyone=False))
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
elif color == ("orange_light"):
  botcolor = (0xff9500)
else:
  botcolor = (color)
# Status
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="APIs | " + prefix + "help"))
# Good part

@bot.command()
async def nice(ctx):
  await ctx.send("Thank you! You're nice too 👍")

bot.remove_command("help")
@bot.command(aliases=["commands"])
async def help(ctx):
  embed=discord.Embed(title="APIcord", description="Help", color=botcolor)
  embed.add_field(name="Meme commands", value=prefix + "info meme", inline=True)
  embed.add_field(name="Image commands", value=prefix + "info img", inline=True)
  embed.add_field(name="Fact commands", value=prefix + "info fact", inline=True)
  embed.add_field(name="About commands", value=prefix + "info about", inline=True)
  embed.add_field(name="More commands", value=prefix + "info more", inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def info(ctx, category):
  if category == "meme":
    embed=discord.Embed(title="Meme commands", description=prefix + "meme", color=botcolor)
    embed.add_field(name=prefix + "reddit", value="Random Reddit meme", inline=True)
    embed.add_field(name=prefix + "meme generator", value="Meme generator help (Please read it before use it)", inline=True)
    embed.add_field(name=prefix + "gmeme <template url> <top text> <bottom text>", value="Meme generator", inline=True)
    await ctx.send(embed=embed)
  elif category == "img":
    embed=discord.Embed(title="Image commands", description=prefix + "img", color=botcolor)
    embed.add_field(name=prefix + "img coffee", value="Random coffee image", inline=True)
    embed.add_field(name=prefix + "img dog", value="Random dog image", inline=True)
    embed.add_field(name=prefix + "img cat", value="Random cat image", inline=True)
    embed.add_field(name=prefix + "img panda", value="Random panda image", inline=True)
    embed.add_field(name=prefix + "img red panda", value="Random red panda image", inline=True)
    embed.add_field(name=prefix + "img bird", value="Random bird image", inline=True)
    embed.add_field(name=prefix + "img fox", value="Random fox image", inline=True)
    embed.add_field(name=prefix + "img koala", value="Random koala image", inline=True)
    await ctx.send(embed=embed)
  elif category == "fact":
    embed=discord.Embed(title="Facts", description=prefix + "fact", color=botcolor)
    embed.add_field(name=prefix + "fact cat", value="Random cat fact", inline=True)
    embed.add_field(name=prefix + "fact dog", value="Random dog fact", inline=True)
    embed.add_field(name=prefix + "fact panda", value="Random panda fact", inline=True)
    embed.add_field(name=prefix + "fact fox", value="Random fox fact", inline=True)
    embed.add_field(name=prefix + "fact bird", value="Random bird fact", inline=True)
    embed.add_field(name=prefix + "fact koala", value="Random koala fact", inline=True)
    await ctx.send(embed=embed)
  elif category == "about":
    embed=discord.Embed(title="About the bot", description="No prefix", color=botcolor)
    embed.add_field(name=prefix + "about", value="Credits", inline=True)
    embed.add_field(name=prefix + "license", value="License", inline=True)
    embed.add_field(name=prefix + "invite", value="Displays bot invite", inline=True)
    embed.add_field(name=prefix + "privacy", value="Bot Privacy Policy", inline=True)
    embed.add_field(name=prefix + "code", value="Source code", inline=True)
    embed.add_field(name=prefix + "help", value="Displays commands", inline=True)
    embed.add_field(name=prefix + "botstats", value="Bot stats", inline=True)
    await ctx.send(embed=embed)
  elif category == "more":
    embed=discord.Embed(title="More", description="", color=botcolor)
    embed.add_field(name=prefix + "chucknorris", value="Random Chuck Norris Joke", inline=True)
    embed.add_field(name=prefix + "say <words>", value="The bot something for you", inline=True)
    embed.add_field(name=prefix + "hug", value="A hug, for you, my friend", inline=True)
    embed.add_field(name=prefix + "delete <amount>", value="Delete message", inline=True)
    embed.add_field(name=prefix + "purge <amount>", value="Delete message", inline=True)
    #embed.add_field(name=prefix + "ft <language code> <text>", value="Fun Translations (https://funtranslations.com) \n For more info of the language codes enter here: https://funtranslations.com/api", inline=True)
    await ctx.send(embed=embed)
  else:
    await ctx.send("error, please put a valid command")

@bot.command()
async def img(ctx, *, something):
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
    embed=discord.Embed(title=("p a n d a"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await ctx.send(embed=embed)
  elif something == "red panda":
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
    embed=discord.Embed(title=("a single tail fox aproves it."), description=("(I think)"), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await ctx.send(embed=embed)
  elif something == "koala":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/koala'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("a"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await ctx.send(embed=embed)
  else:
    await ctx.send("error, please put a valid command")

@bot.command(aliases=["gm"])
async def gmeme(ctx, image, top_text, bottom_text):
  if image.endswith(".jpg"):
    img_type = ".jpg"
  elif image.endswith(".jpeg"):
    img_type = ".jpeg"
  elif image.endswith(".webp"):
    img_type = ".webp"
  elif image.endswith(".png"):
    img_type = ".png"
  elif image.endswith(".gif"):
    img_type = ".gif"
  else:
    await ctx.send("error, image type not found")
  generating_meme=("https://api.memegen.link/images/custom/" + top_text + "/" + bottom_text + img_type + "?background=" + image)
  display_image=discord.Embed(title="Your meme is ready!", description="", color=botcolor)
  display_image.set_image(url=generating_meme)
  await ctx.send(embed=display_image)

@bot.command()
async def fact(ctx, factstuff):
  if factstuff == "cat":
    jdat = (http.request('GET', 'https://catfact.ninja/fact'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    await ctx.send(embed=embed)
  elif factstuff == "dog":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/dog'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    await ctx.send(embed=embed)
  elif factstuff == "panda":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
  elif factstuff == "fox":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/fox'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    await ctx.send(embed=embed)
  elif factstuff == "bird":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/bird'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    await ctx.send(embed=embed)
  elif factstuff == "koala":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/koala'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    await ctx.send(embed=embed)
  elif factstuff == "DEL":
    await ctx.send("Discord Extreme List, i don't know who is but, sounds like a nice name :)")
  elif factstuff == "bots.gg":
    await ctx.send("It's a very good Discord bot list, 70/10")
  elif factstuff == "discord.bots.gg":
    await ctx.send("It's a very good Discord bot list, 70/10")
  else:
    await ctx.send("error, please put a valid command")


#@bot.command()
#async def search(ctx, category, *, query):
  #if category == "nfact":
    #url = "http://numbersapi.com/" + query
    #data = http.request("http://numbersapi.com/" + query)
    #with open (data, 'rt') as myfile:
      #contents = myfile.read()
    #await ctx.send(contents)
  #else:
    #await ctx.send("error, please put a valid command")

#@bot.command(aliases=["fun_translations", "ft"])
#async def funtranslations(ctx, lang, *, text):
  #await ctx.send("https://api.funtranslations.com/translate/" + lang + ".json?text=" + text)
  #url = ('https://api.funtranslations.com/translate/' + lang + '.json?text=' + text)
  #jdat = (http.request('GET', url))
  #jsdata = (json.loads(jdat.data.decode('utf-8')))
  #await ctx.send(jsdata["translated"])

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
async def reddit(ctx):
  # if memetype == "meme":
  #  jdat = (http.request('GET', 'https://some-random-api.ml/meme'))
  #  jsdata = (json.loads(jdat.data.decode('utf-8')))
  #  embed=discord.Embed(title=(jsdata['caption']), description=(""), color=(botcolor))
  #  embed.set_image(url=jsdata['image'])
  #  await ctx.send(embed=embed)
  # elif memetype == "reddit":
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
async def meme(ctx, memetype):
  if memetype == "generator":
    embed=discord.Embed(title=("MeMe gEnErAtOr!!!"), description=("*(yay!)*"), color=(botcolor))
    embed.add_field(name="How to use?", value="Type " + prefix + "gmeme <template url> <top text> <bottom text>", inline=True)
    embed.add_field(name="Writing your meme", value="You can't type you meme just like that, if you like have characters like the '?' or the space ' ' you need to put special characters the guide will be here: https://git.io/JUrSj", inline=True)
    embed.add_field(name="Image types supported", value="Currently are allowed '.jpg', '.jpeg', '.webp' and '.png'")
    await ctx.send(embed=embed)
  else:
    await ctx.send("error, please put a valid command")

@bot.command()
async def invite(ctx):
  await ctx.send("You can invite me to your server clicking in this link: https://apicord.github.io/invite")

@bot.command(aliases=["apicord", "cord"])
async def about(ctx):
  embed=discord.Embed(title=("APIcord Alpha 2.4"), description=("Credits"), color=(botcolor))
  embed.add_field(name=("Creator and programmer"), value=("error#7900"), inline=(False))
  embed.add_field(name=("APIs"), value=("used in this project"), inline=(False))
  embed.add_field(name=("Coffee API"), value=("by **Alex Flipnote** \n (" + prefix + "img coffee)"), inline=(True))
  embed.add_field(name=("Dog API"), value=("by **Elliott Landsborough**, **Eduard Moya** & **Kathie Wu** \n (" + prefix + "img dog)"), inline=(True))
  embed.add_field(name=("Cat Facts API (catfact.ninja)"), value=("by **Cat Fact API creators** \n (" + prefix + "fact cat)"), inline=(True))
  embed.add_field(name=("Meme API"), value=("by **Dev Daksan** \n (" + prefix + "meme reddit)"), inline=(True))
  embed.add_field(name=("memegen.link"), value=("by **Jace Browning** \n (" + prefix + "gmeme/gm)"), inline=(True))
  #embed.add_field(name=("Fun Translations API"), value=("by **Fun Translations** \n (" + prefix + "funtranslations/fun_translations/ft)"), inline=(True))
  embed.add_field(name=("chucknorris.io"), value=("by **chucknorris.io** \n (" + prefix + "chucknorris)"), inline=(True))
  embed.add_field(name=("Some Random Api"), value=("by **Seif Mansour**, **Taka Inzori**, **Excigma** & **Telk** \n (" + prefix + "img cat, " + prefix + "img panda, " + prefix + "img red panda " + prefix + "img bird, " + prefix + "img fox, " + prefix + "img koala, " + prefix + "hug " + prefix + "fact dog, " + prefix + "fact panda, " + prefix + "fact fox, " + prefix + "fact bird & " + prefix + "fact koala)"), inline=(False))
  embed.add_field(name="Libraries", value="used", inline=False)
  embed.add_field(name="discord.py", value="by **Rapptz and the discord.py community**", inline=True)
  embed.add_field(name="python-telegram-bot", value="by **python-telegram-bot community**", inline=True)
  embed.add_field(name="pyTelegramBotAPI", value="by **Frank Wang and the pyTelegramBotAPI community**", inline=True)
  embed.add_field(name="urllib3", value="by **urllib3 community**", inline=True)
  embed.add_field(name="keep_alive.py", value="by **TheDrone7**", inline=True)
  embed.add_field(name="Thanks", value="Thanks to **Polking** to follow the development, **DEL** guys for some help and **the people** to comment and suggest", inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def license(ctx):
  embed=discord.Embed(title=("APIcord Licenses"), description=(""), color=(botcolor))
  embed.add_field(name=("APIcord"), value=("Boost Software License 1.0"), inline=(True))
  embed.add_field(name=("Coffee API"), value=("MIT License (© 2020 AlexFlipnote)"), inline=(True))
  embed.add_field(name=("Dog CEO Image Library"), value=("GNU General Public License v3.0"), inline=(True))
  embed.add_field(name=("Meme API"), value=("MIT License (© 2020 Dev Daksan P S)"), inline=(True))
  embed.add_field(name=("memegen.link"), value=("MIT License (© 2020 Jace Browning)"), inline=(True))
  embed.add_field(name=("Some Random Api (SRA)"), value=("Apache License 2.0"))
  await ctx.send(embed=embed)

@bot.command()
async def privacy(ctx):
  await ctx.send("https://apicord.github.io/privacy")

@bot.command()
async def code(ctx):
  await ctx.send("https://github.com/APIcord/discord")

@bot.command()
async def say(ctx, *, yourmessage):
  if yourmessage == "reeeeee":
    await ctx.send("**REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE**")
  elif yourmessage == "BigF":
    await ctx.send("FFFFFFFFFF\nFFFFFFFFFF\nFFF\nFFFFFF \nFFFFFF\nFFF\nFFF\nFFF")
  elif yourmessage == "polkingbot":
    embed=discord.Embed(title="**MonsterWorld**", url="https://discord.com/oauth2/authorize?client_id=756602085298143412&scope=bot&permissions=2147483647", description="Bot recomendado", color=botcolor)
    await ctx.send(embed=embed)
  else:
    await ctx.send(yourmessage)

@bot.command()
async def servercounter(ctx):
  embed=discord.Embed(title=("Bot stats"), description="", color=botcolor)
  embed.add_field(name=("Bot used in"), value=(f"{len(bot.guilds)} servers"), inline=(True))
  await ctx.send(embed=embed)

@bot.command(aliases=["delete"])
async def purge(ctx, the_limit: int):
  embed=discord.Embed(title="The messages were deleted", description="", color=botcolor)
  await ctx.channel.purge(limit=the_limit)
  await ctx.send(embed=embed)

@bot.command()
async def egg(ctx):
  await ctx.send('🥚')
@bot.command()
async def SmolF(ctx):
  await ctx.send("**f** (:-) aww, a small F, this is cute uwu)")
@bot.command()
async def thereisanimposteramongus(ctx):
  await ctx.send("**ඞ There is 1 imposter among us ඞ**")
keep_alive.keep_alive()
bot.run(token)
# I don't know how to make a totally functional bot ._.
