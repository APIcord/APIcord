import os
os.system("cls" if os.name=="nt" else "clear")
from colorama import init, Fore, Back, Style
#import time
import random
import discord
from discord.ext import commands
from flask import Flask, render_template
from threading import Thread
import json
import os.path
import urllib3
from datetime import date
from google_trans_new import google_translator
# import cairosvg

__version__ = "Alpha 3.2"
prefix = os.getenv("PREFIX")
color = os.getenv("COLOR")

# Start stuff
init()
bot = commands.Bot(command_prefix=prefix, description="Discord bot focused on APIs", allowed_mentions=discord.AllowedMentions(roles=False, users=False, everyone=False))
embed = discord.Embed
http = urllib3.PoolManager()
tdate = date.today()
gtrans = google_translator()

# ASCII
def classic_ascii():
  print(f"""{Fore.RED}yyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyy
yyyy{Fore.WHITE}:          :{Fore.RED}yyyy
yyyy{Fore.WHITE}. /s`:o+:::.{Fore.RED}hhyy
yyyy{Fore.WHITE}. s+-:o/o//.{Fore.RED}hhhh {Fore.WHITE}APIcord {Fore.RESET}(by absucc){Fore.RED}
yyyy{Fore.WHITE}.-s++:o. //.{Fore.RED}hhhh {Fore.GREEN}ASCII art powered by{Fore.RED}
yyyy{Fore.WHITE}.-.`/-:  .-.{Fore.RED}hhhh {Fore.GREEN}TEXT-IMAGE.com & Colorama{Fore.RED}
yyyy{Fore.WHITE}.`/:.....::+{Fore.RED}hhhh
yyyy{Fore.WHITE}oy{Fore.RED}hhhhhhhyyhhhhh
yyyyyyhhhhhhhhhhhhhh {Style.RESET_ALL}v{__version__}
{Style.RESET_ALL}""")
def matrix_ascii():
  print(f"""{Fore.GREEN}yyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyy
yyyy{Fore.WHITE}:          :{Fore.GREEN}yyyy
yyyy{Fore.WHITE}. /s`:o+:::.{Fore.GREEN}hhyy
yyyy{Fore.WHITE}. s+-:o/o//.{Fore.GREEN}hhhh {Fore.WHITE}APIcord {Fore.RESET}(by absucc){Fore.GREEN}
yyyy{Fore.WHITE}.-s++:o. //.{Fore.GREEN}hhhh {Fore.GREEN}ASCII art powered by{Fore.GREEN}
yyyy{Fore.WHITE}.-.`/-:  .-.{Fore.GREEN}hhhh {Fore.GREEN}TEXT-IMAGE.com & Colorama{Fore.GREEN}
yyyy{Fore.WHITE}.`/:.....::+{Fore.GREEN}hhhh
yyyy{Fore.WHITE}oy{Fore.GREEN}hhhhhhhyyhhhhh
yyyyyyhhhhhhhhhhhhhh {Style.RESET_ALL}v{__version__}
{Style.RESET_ALL}""")
def extra_ascii():
  print(f"""{Back.RED}{Fore.RED}yyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyy
yyyy{Back.RESET}{Fore.WHITE}:          :{Back.RED}{Fore.RED}yyyy
yyyy{Back.RESET}{Fore.WHITE}. /s`:o+:::.{Back.RED}{Fore.RED}hhyy
yyyy{Back.RESET}{Fore.WHITE}. s+-:o/o//.{Back.RED}{Fore.RED}hhhh{Back.RESET} {Fore.WHITE}APIcord {Fore.RESET}(by absucc){Back.RED}{Fore.RED}
yyyy{Back.RESET}{Fore.WHITE}.-s++:o. //.{Back.RED}{Fore.RED}hhhh{Back.RESET} {Fore.GREEN}ASCII art powered by{Back.RED}{Fore.RED}
yyyy{Back.RESET}{Fore.WHITE}.-.`/-:  .-.{Back.RED}{Fore.RED}hhhh{Back.RESET} {Fore.GREEN}TEXT-IMAGE.com & Colorama{Back.RED}{Fore.RED}
yyyy{Back.RESET}{Fore.WHITE}.`/:.....::+{Back.RED}{Fore.RED}hhhh
yyyy{Back.RESET}{Fore.WHITE}oy{Back.RED}{Fore.RED}hhhhhhhyyhhhhh
yyyyyyhhhhhhhhhhhhhh{Style.RESET_ALL} v{__version__}
{Style.RESET_ALL}""")
def experimental_ascii():
  print(f"""{Fore.RED}{Back.RED}yyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyy
yyyy{Back.WHITE}{Fore.WHITE}:          :{Fore.RED}{Back.RED}yyyy
yyyy{Back.WHITE}{Fore.WHITE}.{Fore.RED} /s`:o+:::.{Fore.RED}{Back.RED}hhyy
yyyy{Back.WHITE}{Fore.WHITE}.{Fore.RED} s{Fore.WHITE}+{Fore.RED}-:o/o//.{Fore.RED}{Back.RED}hhhh{Back.RESET} {Fore.WHITE}APIcord (by absucc){Back.RESET}{Fore.RED}{Back.RED}
yyyy{Back.WHITE}{Fore.WHITE}.{Fore.RED}-s++:o. //.{Fore.RED}{Back.RED}hhhh{Back.RESET} {Fore.GREEN}ASCII art powered by{Fore.RED}{Back.RED}
{Back.RED}yyyy{Back.WHITE}.-.{Fore.WHITE}`/{Fore.RED}-:  .-.{Fore.RED}{Back.RED}hhhh{Back.RESET} {Fore.GREEN}TEXT-IMAGE.com & Colorama{Fore.RED}{Back.RED}
yyyy{Back.WHITE}{Fore.WHITE}.`{Fore.RED}/:{Fore.WHITE}.....::+{Fore.RED}{Back.RED}hhhh
yyyy{Back.WHITE}{Fore.WHITE}oy{Fore.RED}{Back.RED}hhhhhhhyyhhhhh
yyyyyyhhhhhhhhhhhhhh{Style.RESET_ALL} v{__version__}
{Style.RESET_ALL}""")
def ascii():
  if os.getenv("ASCII_ART") == "classic":
    classic_ascii()
  elif os.getenv("ASCII_ART") == "matrix":
    matrix_ascii()
  elif os.getenv("ASCII_ART") == "extra":
    extra_ascii()
  elif os.getenv("ASCII_ART") == "experimental":
    experimental_ascii()
  else:
    print("[BANNER NOT FOUND]")

# logsenv() and Flask("")
def logsenv():
  if os.getenv("LOGS") == "0":
    os.system("cls" if os.name=="nt" else "clear")
    ascii()
  print(Style.RESET_ALL)
app = Flask("")
logsenv()

ascii()
print(f"{Back.WHITE}{Fore.BLACK}---- LOGS ----")
logsenv()

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
  if os.getenv("STATUS_TYPE") == "online":
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="APIs | " + prefix + "help"))
  elif os.getenv("STATUS_TYPE") == "idle":
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="APIs | " + prefix + "help"))
  elif os.getenv("STATUS_TYPE") == "dnd":
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="APIs | " + prefix + "help"))
  elif os.getenv("STATUS_TYPE") == "do_not_disturb":
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="APIs | " + prefix + "help"))
  else:
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="APIs | " + prefix + "help"))
  
# Good part

@bot.command()
async def nice(ctx):
  await ctx.send("Thank you! You're nice too 👍")

bot.remove_command("help")
@bot.command(aliases=["commands"])
async def help(ctx):
  embed=discord.Embed(title="APIcord Help Menu", description="Featured Commands: **" + prefix + "motd**, **" + prefix + "about** & **" + prefix + "credits**", color=botcolor)
  embed.add_field(name="Meme commands", value=prefix + "info meme", inline=True)
  embed.add_field(name="Image commands", value=prefix + "info img", inline=True)
  embed.add_field(name="Fact commands", value=prefix + "info fact", inline=True)
  embed.add_field(name="Translation commands", value=prefix + "info translate", inline=True)
  embed.add_field(name="About commands", value=prefix + "info about", inline=True)
  embed.add_field(name="More commands", value=prefix + "info more", inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def info(ctx, category):
  if category == "meme":
    embed=discord.Embed(title="Meme commands", description="", color=botcolor)
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
  elif category == "translate":
    embed=discord.Embed(title="Translator", description="Translator => Traductor", color=botcolor)
    embed.add_field(name="How to use?", value="Type " + prefix + "translate/t <language code> <text>", inline=True)
    embed.add_field(name="Languages codes", value="I think the Languages section on the README.md of LittleCoder's \"translate\" python module could help you: https://github.com/littlecodersh/translation/blob/master/README_EN.md#language", inline=True)
    await ctx.send(embed=embed)
  elif category == "about":
    embed=discord.Embed(title="About the bot", description="", color=botcolor)
    embed.add_field(name=prefix + "about", value="About this instance", inline=True)
    embed.add_field(name=prefix + "credits", value="Credits", inline=True)
    embed.add_field(name=prefix + "licenses", value="Licenses", inline=True)
    embed.add_field(name=prefix + "invite", value="Displays bot invite", inline=True)
    embed.add_field(name=prefix + "issues", value="Go to the issues page of this bot", inline=True)
    embed.add_field(name=prefix + "privacy", value="Bot Privacy Policy", inline=True)
    embed.add_field(name=prefix + "code", value="Source code", inline=True)
    embed.add_field(name=prefix + "help", value="Displays commands", inline=True)
    await ctx.send(embed=embed)
  elif category == "more":
    embed=discord.Embed(title="More", description="", color=botcolor)
    embed.add_field(name=prefix + "chucknorris", value="Random Chuck Norris Joke", inline=True)
    embed.add_field(name=prefix + "delete <amount>", value="Delete message", inline=True)
    embed.add_field(name=prefix + "hug", value="A hug, for you, my friend", inline=True)
    embed.add_field(name=prefix + "motd", value="Read the message of the day!", inline=True)
    embed.add_field(name=prefix + "say <words>", value="The bot something for you", inline=True)
    embed.add_field(name=prefix + "purge <amount>", value="Delete message", inline=True)
    embed.add_field(name=prefix + "xkcd <0 (Current) /number>", value="Read a comic of xkcd! IN APICORD!!!", inline=True)
    await ctx.send(embed=embed)
  else:
    await ctx.send("Error, please put a valid command")

@bot.command()
async def motd(ctx):
  motdread = open("motd.txt","r") 
  await ctx.send("Message of the day:\n```\n" + motdread.read() + "\n```")
  motdread.close()

@bot.command()
async def img(ctx, *, something):
  if something == "coffee":
    jdat = (http.request('GET', 'https://coffee.alexflipnote.dev/random.json'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Here you have your coffee"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['file']))
    embed.set_footer(text="Powered by **Coffee API**")
    await ctx.send(embed=embed)
  elif something == "dog":
    jdat = (http.request('GET', 'https://dog.ceo/api/breeds/image/random'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("A doggo! :D"), description=("I wish you'll like this uwu"), color=(botcolor))
    embed.set_image(url=(jsdata['message']))
    embed.set_footer(text="Powered by Dog CEO")
    await ctx.send(embed=embed)
  elif something == "cat":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/cat'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("A cat! :D"), description=("kittens & adult kittens"), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif something == "panda":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("p a n d a"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif something == "red panda":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/red_panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("red panda :)"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif something == "bird":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/birb'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("*bird sounds.mp3*"), description=(""), color=(botcolor))
    embed.set_image(url=jsdata['link'])
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif something == "fox":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/fox'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title="fox mouse", description="(I think)", color=botcolor)
    embed.set_image(url=(jsdata['link']))
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif something == "koala":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/koala'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title="a", description="", color=botcolor)
    embed.set_image(url=jsdata['link'])
    embed.set_footer(text="Powered by Some Random Api")
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
#  elif image.endswith(".gif"):
#    img_type = ".gif"
  else:
    await ctx.send("error, image type not found")
  generating_meme=("https://api.memegen.link/images/custom/" + top_text + "/" + bottom_text + img_type + "?background=" + image)
  display_image=discord.Embed(title="Your meme is ready!", description="", color=botcolor)
  display_image.set_image(url=generating_meme)
  display_image.set_footer(text="Powered by memegen.link")
  await ctx.send(embed=display_image)

#@bot.command()
#async def getitoncodeberg(ctx, *, text):
#  cache_name = random.randint(1, 1000000000)
#  cache_is_ok = 0
#  def cache_search():
#    if os.path.isfile("cache/" + str(cache_name) + ".png"):
#      cache_is_ok = 0
#    else:
#      cache_is_ok = 1
#    return
#  cache_search()
#  if cache_is_ok == 0:
#    while cache_is_ok == 0:
#      cache_search()
#  cairosvg.svg2png(url="https://api.l64.repl.co/badges.php?type=codeberg&subtype=blue-on-white&background_color=000000&text=" + text, write_to="cache/"+ cache_name +".png")
#  display_image=discord.Embed(title="Your meme is ready!", description="", color=botcolor)
#  display_image.set_image(url="cache/" + cache_name + ".png")
#  await ctx.send(embed=display_image)

@bot.command()
async def fact(ctx, factstuff):
  if factstuff == "cat":
    #jdat = (http.request('GET', 'https://catfact.ninja/fact'))
    jdat = (http.request("GET", "https://some-random-api.ml/facts/cat"))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    #embed.set_footer(text="Powered by catfact.ninja")
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif factstuff == "dog":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/dog'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif factstuff == "panda":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif factstuff == "fox":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/fox'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif factstuff == "bird":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/bird'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    embed.set_footer(text="Powered by Some Random Api")
    await ctx.send(embed=embed)
  elif factstuff == "koala":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/koala'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    embed.set_footer(text="Powered by Some Random Api")
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
    embed.set_footer(text="Powered by chucknorris.io")
    await ctx.send(embed=embed)
  
@bot.command()
async def hug(ctx):
    jdat = (http.request('GET', 'https://some-random-api.ml/animu/hug'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    await ctx.send(jsdata['link'] + "\nPowered by Some Random Api")

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
    embed=discord.Embed(title=("This meme is NSFW"), description=("Please, use " + prefix + "reddit again"), color=(botcolor))
    await ctx.send(embed=embed)
  else:
    #Embed
    embed_two=discord.Embed(title=(jsdata['title']), url=(jsdata['postLink']), description=(""), color=(botcolor))
    # embed_two.set_author(name=(jsdata['author']), url=("https://reddit.com/u/" + jsdata['author']), icon_url=("https://www.redditstatic.com/desktop2x/img/favicon/android-icon-192x192.png"))
    embed_two.set_thumbnail(url="https://www.redditstatic.com/desktop2x/img/favicon/favicon-32x32.png")
    embed_two.add_field(name="Posted by:", value=("u/" + jsdata['author']), inline=(True))
    embed_two.add_field(name="Subreddit:", value=("r/" + jsdata['subreddit']), inline=(True))
    embed_two.set_image(url=jsdata['url'])
    embed_two.set_footer(text="Powered by Dev Daksan's Meme API")
    await ctx.send(embed=embed_two)

@bot.command()
async def meme(ctx, memetype):
  if memetype == "meme":
    ctx.send("Command deleted, if you want something similar, please try: " + prefix + "reddit")
  elif memetype == "reddit":
    ctx.send("Command moved to \"" + prefix + "reddit\"")
  elif memetype == "generator":
    embed=discord.Embed(title=("MeMe gEnErAtOr!!!"), description=("*(yay!)*"), color=(botcolor))
    embed.add_field(name="How to use?", value="Type " + prefix + "gmeme <template url> <top text> <bottom text>", inline=True)
    embed.add_field(name="Writing your meme", value="You can't type you meme just like that, if you like have characters like the '?' or the space ' ' you need to put special characters the guide will be here: https://git.io/JUrSj", inline=True)
    embed.add_field(name="Image types supported", value="Currently are allowed '.jpg', '.jpeg', '.webp' and '.png'")
    embed.set_footer(text="Powered by memegen.link")
    await ctx.send(embed=embed)
  else:
    await ctx.send("error, please put a valid command")

#@bot.command()
#async def w(ctx, *, query):
#    jdatq = (http.request('GET', 'https://www.metaweather.com/api/location/search/?query=' + query))
#    jsdataq = (json.loads(jdatq.data.decode('utf-8')))
#    queryp = (http.request('GET', #'https://www.metaweather.com/api/location/' + jsdataq['woeid'] + '/'))
#    qp = (json.loads(queryp.data.decode('utf-8')))
#    embed=discord.Embed(title=(qp['value']), url=(jsdata['url']), description=(""), color=(botcolor))
#    embed.set_thumbnail(url=(jsdata['icon_url']))
#    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
  await ctx.send("You can invite me to your server clicking in this link: " + os.getenv("INVITE"))

@bot.command()
async def issues(ctx):
  await ctx.send("https://github.com/APIcord/discord/issues")

@bot.command()
async def about(ctx):
  embed_two=discord.Embed(title=os.getenv("NAME"), url="", description="", color=botcolor)
  embed_two.set_thumbnail(url=os.getenv("AVATAR_URL"))
  embed_two.add_field(name="Instance Type:", value="Discord", inline=True)
  embed_two.add_field(name="Owner:", value=os.getenv("OWNER"), inline=True)
  embed_two.add_field(name="Prefix:", value=os.getenv("PREFIX"), inline=True)
  embed_two.add_field(name="Number of servers:", value=f"{len(bot.guilds)} servers", inline=True)
  embed_two.add_field(name="Version of APIcord:", value=f"{__version__} servers", inline=True)
  embed_two.set_footer(text="Bot software powered by APIcord")
  await ctx.send(embed=embed_two)

@bot.command(aliases=["apicord", "cord"])
async def credits(ctx):
  embed=discord.Embed(title=f"APIcord v{__version__}", description="Credits", color=botcolor)
  embed.add_field(name="-- CREW --", value=":)", inline=False)
  embed.add_field(name="Creator and programmer", value="error#7900 (absucc)", inline=True)
  embed.add_field(name="-- APIS --", value="used in this project", inline=False)
  embed.add_field(name="Coffee API", value="by **Alex Flipnote** \n (" + prefix + "img coffee)", inline=True)
  embed.add_field(name="Dog API", value="by **Elliott Landsborough**, **Eduard Moya** & **Kathie Wu** \n (" + prefix + "img dog)", inline=True)
  #embed.add_field(name="Cat Facts API (catfact.ninja)", value="by **Cat Fact API creators** \n (" + prefix + "fact cat)", inline=True)
  embed.add_field(name="Meme API", value="by **Dev Daksan** \n (" + prefix + "reddit)", inline=True)
  embed.add_field(name="memegen.link", value="by **Jace Browning** \n (" + prefix + "gmeme/gm)", inline=True)
  #embed.add_field(name=("Fun Translations API"), value=("by **Fun Translations** \n (" + prefix + "funtranslations/fun_translations/ft)"), inline=(True))
  embed.add_field(name="chucknorris.io", value="by **chucknorris.io** \n (" + prefix + "chucknorris)", inline=True)
  embed.add_field(name="xkcd's JSON interface", value="by **Randall Munroe** \n (" + prefix + "xkcd)", inline=True)
  embed.add_field(name="Some Random Api", value="by **Seif Mansour**, **Taka Inzori**, **Excigma** & **Telk** \n (" + prefix + "img cat, " + prefix + "img panda, " + prefix + "img red panda, " + prefix + "img bird, " + prefix + "img fox, " + prefix + "img koala, " + prefix + "hug, " + prefix + "fact cat, " + prefix + "fact dog, " + prefix + "fact panda, " + prefix + "fact fox, " + prefix + "fact bird & " + prefix + "fact koala)", inline=False)
  embed.add_field(name="-- LIBRARIES --", value="used", inline=False)
  embed.add_field(name="urllib3", value="by **urllib3 community**", inline=True)
  embed.add_field(name="Colorama", value="by **Jonathan Hartley & contributors**", inline=True)
  embed.add_field(name="google_trans_new", value="by **lushan88a**", inline=True)
  embed.add_field(name="Discord", value="yes, I made a section for 1 library", inline=False)
  embed.add_field(name="discord.py", value="by **Rapptz and the discord.py community**", inline=True)
  embed.add_field(name="Telegram", value="Coming soon", inline=False)
  embed.add_field(name="pyTelegramBotAPI", value="by **Frank Wang and the pyTelegramBotAPI community**", inline=True)
  embed.add_field(name="python-telegram-bot", value="by **python-telegram-bot community**", inline=True)
  embed.add_field(name="Web interface", value="(and the website)", inline=False)
  embed.add_field(name="Bootstrap", value="by **Twitter, Inc. & The Bootstrap Authors**", inline=True)
  embed.add_field(name="Fork Awesome", value="by **Fork Awesome**", inline=True)
  embed.add_field(name="Flask", value="by **Armin Ronacher**", inline=True)
  embed.add_field(name="keep_alive.py", value="by **TheDrone7**", inline=True)
  embed.add_field(name="-- SPECIAL THANKS --", value="used", inline=False)
  embed.add_field(name="@doodlei_ (Instagram)", value="for the logotype", inline=True)
  embed.add_field(name="Discord Extreme List guys", value="for some help", inline=True)
  embed.add_field(name="Google, LLC", value="for the translations for " + prefix + "translate/t", inline=True)
  embed.add_field(name="UptimeRobot", value="Website Monitoring for the original bot", inline=True)
  embed.add_field(name="Repl.it", value="for hosting (for the original bot and the development bot) and the IDE", inline=True)
  await ctx.send(embed=embed)

@bot.command(aliases=["licenses"])
async def license(ctx):
  embed=discord.Embed(title="Licenses", description="", color=botcolor)
  embed.add_field(name="APIcord", value="MIT License (© 2020 absucc)", inline=True)
  embed.add_field(name="Bootstrap", value="MIT License (© 2011-2020 Twitter, Inc. & The Bootstrap Authors)", inline=True)
  embed.add_field(name="Coffee API", value="MIT License (© 2020 AlexFlipnote)", inline=True)
  embed.add_field(name="Colorama", value="BSD-3-Clause License", inline=True)
  embed.add_field(name="Discord.py", value="MIT License (© 2015-2021 Rapptz)", inline=True)
  embed.add_field(name="Dog CEO Image Library", value="GNU General Public License v3.0", inline=True)
  embed.add_field(name="Flask", value="BSD-3-Clause License", inline=True)
  embed.add_field(name="Fork Awesome", value="SIL OFL 1.1 (Font) & MIT License (CSS, LESS and Sass)", inline=True)
  embed.add_field(name="google_trans_new", value="MIT License (© 2020 lushan88a)", inline=True)
  embed.add_field(name="memegen.link", value="MIT License (© 2020 Jace Browning)", inline=True)
  embed.add_field(name="Meme API", value="MIT License (© 2020 Dev Daksan P S)", inline=True)
  embed.add_field(name="Some Random Api (SRA)", value="Apache License 2.0")
  await ctx.send(embed=embed)

@bot.command()
async def privacy(ctx):
  await ctx.send("https://apicord.github.io/privacy.html")

@bot.command()
async def code(ctx):
  await ctx.send("https://github.com/APIcord/discord\nhttps://gitlab.com/APIcord/discord (Mirror)")

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

@bot.command(aliases=["delete"])
async def purge(ctx, the_limit: int):
  embed=discord.Embed(title=":wastebasket::thumbsup:", description=str(the_limit) + " messages were eliminated successfully", color=botcolor)
  await ctx.channel.purge(limit=the_limit)
  await ctx.send(embed=embed)

@bot.command()
async def xkcd(ctx, numberz: int):
  if numberz == 0:
    jdat = (http.request('GET', 'https://xkcd.com/info.0.json'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=(jsdata["title"]), description="N° " + str(jsdata["num"]) + " | " + jsdata["month"] + "/" + jsdata["day"] + "/" + jsdata["year"], color=botcolor)
    embed.set_image(url=jsdata["img"])
    embed.set_footer(text="Powered by xkcd's JSON interface")
    await ctx.send(embed=embed)
  else:
    jdat = (http.request("GET", "https://xkcd.com/" + str(numberz) + "/info.0.json"))
    jsdata = (json.loads(jdat.data.decode("utf-8")))
    embed=discord.Embed(title=jsdata["title"], description="N° " + str(jsdata["num"]) + " | " + jsdata["month"] + "/" + jsdata["day"] + "/" + jsdata["year"], color=botcolor)
    embed.set_image(url=jsdata["img"])
    embed.set_footer(text="Powered by xkcd's JSON interface")
    await ctx.send(embed=embed)

@bot.command(aliases=['t'])
async def translate(ctx, lang: str, *, query: str):
  one = gtrans.translate([query], lang_tgt=lang)
  two = one.replace("[\'", "")
  three = two.replace("\']", "")
  await ctx.send(three)

@bot.command(aliases=["hgang", "Hgang", "HGang", "H", "h", "jointhehgang"])
async def joinhgang(ctx):
  embed=discord.Embed(title="Join the H gang", description="""██╗░░██╗
  ██║░░██║
  ███████║
  ██╔══██║
  ██║░░██║
  ╚═╝░░╚═╝""", color=botcolor)
  embed.set_thumbnail(url="https://media.nertivia.net/6661602938407882752/6680595321476616192/avatar.gif")
  embed.add_field(name="Reddit", value="r/TheLetterH", inline=True)
  embed.add_field(name="Nertivia", value="https://nertivia.net/invites/H", inline=True)
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
@bot.command(aliases=["christmaseve", "christmasevening", "xmas"])
async def christmas(ctx):
  day = tdate.strftime("%d")
  month = tdate.strftime("%m")
  if month == "12":
    if day == "24":
      await ctx.send("Tommorow is christamas")
    elif day == "25":
      await ctx.send("**MERRY CHRISTMAS!!!**")
    else:
      await ctx.send("It's not christmas\nThis is easter egg is for Christmas Eve & Christmas\nWait for it")

    
# WEBSERVER
if os.getenv("REPL.IT") == "1":
  enwebserver = True
  host_flask = "0.0.0.0"
  if os.getenv("PORT") == "80":
    port_flask = "5000"
  else:
    port_flask = os.getenv("PORT")
else:
  if os.getenv("WEBSERVER") == "1":
    enwebserver = True
    host_flask = os.getenv("HOST")
    port_flask = os.getenv("PORT")

if enwebserver == True:
  @app.errorhandler(404)
  def error404(error):
    logsenv()
    return render_template("errors/404.html", **locals()),404
  @app.errorhandler(500)
  def error500(error):
    logsenv()
    return render_template("errors/500.html", **locals()),500

  @app.route("/")
  def main():
    logsenv()
    return render_template("index.html", **locals(), prefix=os.getenv("PREFIX"), avatar=os.getenv("AVATAR_URL"), instance_name=os.getenv("NAME"), instance_owner=os.getenv("OWNER"), guilds=f"{len(bot.guilds)}", version=f"{__version__}")
  @app.route("/privacy")
  def privacya():
    logsenv()
    return render_template("privacy.html", **locals())

  def run():
    app.run(host=host_flask, port=port_flask)
    logsenv()

  # Code from https://repl.it/@TheDrone7/discordpy-rewrite#keep_alive.py
  def keep_alive():
    server = Thread(target=run)
    server.start()
    logsenv()

  keep_alive()
bot.run(os.getenv("TOKEN"))
#The APIcord Team wishes you a great 2021!
