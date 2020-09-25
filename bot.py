import time
import discord
import flask
import json
import urllib3
import keep_alive




# Token and prefix
token = ("[token]")
prefix = ("api!")
# Color chooser
color = ("red")
# Options: red, grey, blue_metalic & green




# Start stuff
bot = discord.Client()
embed = discord.Embed
http = urllib3.PoolManager()
print("Man, there isn't nothing to see here, it's a normal Discord.py bot.")


# Color
if color == ("red"):
  botcolor= (0xff0000)
elif color == ("grey"):
  botcolor = (0xffffff)
elif color == ("blue_metalic"):
  botcolor = (0xfff)
elif color == ("green"):
  botcolor == (0xff000)

# Status
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="APIs | " + prefix + "help"))
# Good part
@bot.event
async def on_message(message):
  if message.content.startswith(prefix + "nice"):
    channel = message.channel
    await channel.send("Thank you! You're nice too 👍")
  elif message.content.startswith(prefix + "help"):
    channel = message.channel

    embed=discord.Embed(title=("APIcord"), description=("Help"), color=(botcolor))
    embed.add_field(name=(prefix + "help"), value=("Help command"), inline=(True))
    embed.add_field(name=(prefix + "help"), value=("Random Chuck Norris Joke"), inline=(True))
    embed.add_field(name=(prefix + "hug"), value=("A hug, for you, my friend"), inline=(True))

    embed.add_field(name=("Meme commands"), value=(prefix + "meme"), inline=(False))
    # meme=discord.Embed(title=("Meme commands"), description=(prefix + "meme"), color=(botcolor))
    embed.add_field(name=(prefix + "meme meme"), value=("Random meme"), inline=(True))
    embed.add_field(name=(prefix + "meme reddit"), value=("Random Reddit meme"), inline=(True))

    embed.add_field(name=("Image commands"), value=(prefix + "img"), inline=(False))
    # img=discord.Embed(title=("Image commands"), description=(prefix + "img"), color=(botcolor))
    embed.add_field(name=(prefix + "img coffee"), value=("Random coffee image"), inline=(True))
    embed.add_field(name=(prefix + "img dog"), value=("Random dog image"), inline=(True))
    embed.add_field(name=(prefix + "img cat"), value=("Random cat image"), inline=(True))
    embed.add_field(name=(prefix + "img panda"), value=("Random panda image"), inline=(True))
    embed.add_field(name=(prefix + "img red panda"), value=("Random red panda image"), inline=(True))
    embed.add_field(name=(prefix + "img bird"), value=("Random bird image"), inline=(True))
    embed.add_field(name=(prefix + "img fox"), value=("Random fox image"), inline=(True))
    embed.add_field(name=(prefix + "img koala"), value=("Random koala image"), inline=(True))

    embed.add_field(name=("Facts"), value=(prefix + "fact"), inline=(False))
    # fact=discord.Embed(title=("Facts"), description=(prefix + "fact"), color=(botcolor))
    embed.add_field(name=(prefix + "fact cat"), value=("Random cat fact"), inline=True)

    embed.add_field(name=("About the bot"), value=("No prefix"), inline=(False))
    # about=discord.Embed(title=("About the bot"), description=("License, privacy, credits, etc."), color=(botcolor))
    embed.add_field(name=(prefix + "about"), value=("Credits"), inline=(True))
    embed.add_field(name=(prefix + "license"), value=("License"), inline=(True))
    embed.add_field(name=(prefix + "invite"), value=("Displays bot invite"), inline=(True))
    embed.add_field(name=(prefix + "privacy"), value=("Bot Privacy Policy"), inline=(True))
    embed.add_field(name=(prefix + "code"), value=("Source code"), inline=(True))

    await channel.send(embed=embed)
    # await channel.send(embed=meme)
    # await channel.send(embed=img)
    # await channel.send(embed=fact)
    # await channel.send(embed=about)


  elif message.content.startswith(prefix + "img coffee"):
    channel = message.channel
    jdat = (http.request('GET', 'https://coffee.alexflipnote.dev/random.json'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Here you have your coffee"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['file']))
    await channel.send(embed=embed)


  elif message.content.startswith(prefix + "img dog"):
    channel = message.channel
    jdat = (http.request('GET', 'https://dog.ceo/api/breeds/image/random'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("A doggo! :D"), description=("I wish you'll like this uwu"), color=(botcolor))
    embed.set_image(url=(jsdata['message']))
    await channel.send(embed=embed)

  elif message.content.startswith(prefix + "img cat"):
    channel = message.channel
    jdat = (http.request('GET', 'https://some-random-api.ml/img/cat'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("A cat! :D"), description=("kittens & adult kittens"), color=(botcolor))
    embed.set_image(jsdata['link'])
    await channel.send(embed=embed)
  
  elif message.content.startswith(prefix + "img panda"):
    channel = message.channel
    jdat = (http.request('GET', 'https://some-random-api.ml/img/panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("p a n d a"), description=("kittens & adult kittens"), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await channel.send(embed=embed)

  elif message.content.startswith(prefix + "img red panda"):
    channel = message.channel
    jdat = (http.request('GET', 'https://some-random-api.ml/img/red_panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("red panda :)"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await channel.send(embed=embed)

  elif message.content.startswith(prefix + "img bird"):
    channel = message.channel
    jdat = (http.request('GET', 'https://some-random-api.ml/img/birb'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("*bird sounds.mp3*"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await channel.send(embed=embed)

  elif message.content.startswith(prefix + "img fox"):
    channel = message.channel
    jdat = (http.request('GET', 'https://some-random-api.ml/img/fox'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Finnegan Fox aproves it."), description=("(I think)"), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await channel.send(embed=embed)

  elif message.content.startswith(prefix + "img koala"):
    channel = message.channel
    jdat = (http.request('GET', 'https://some-random-api.ml/img/koala'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("a"), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['link']))
    await channel.send(embed=embed)



  elif message.content.startswith(prefix + "fact cat"):
    channel = message.channel
    jdat = (http.request('GET', 'https://catfact.ninja/fact'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=("Did you know..."), description=(jsdata['fact']), color=(botcolor))
    await channel.send(embed=embed)


  elif message.content.startswith(prefix + "chucknorris.io"):
    channel = message.channel
    jdat = (http.request('GET', 'https://api.chucknorris.io/jokes/random'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=(jsdata['value']), url=(jsdata['url']), description=(""), color=(botcolor))
    embed.set_thumbnail(url=(jsdata['icon_url']))
    await channel.send(embed=embed)
  
  elif message.content.startswith(prefix + "hug"):
    channel = message.channel
    jdat = (http.request('GET', 'https://some-random-api.ml/animu/hug'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    await channel.send(jsdata['link'])


  elif message.content.startswith(prefix + "meme meme"):
    channel = message.channel
    jdat = (http.request('GET', 'https://some-random-api.ml/meme'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title=(jsdata['caption']), description=(""), color=(botcolor))
    embed.set_image(url=(jsdata['image']))
    await channel.send(embed=embed)

  elif message.content.startswith(prefix + "meme reddit"):
    channel = message.channel
    jdat = (http.request('GET', 'https://meme-api.herokuapp.com/gimme'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    if jsdata['nsfw'] == "true":
      embed=discord.Embed(title=("This meme is NSFW"), description=("We're going to reload this command, sorry for the incombinient."), color=(botcolor))
      await channel.send(embed=embed)
      await channel.send(prefix + "meme reddit")
    else:
      #Embed
      embed_two=discord.Embed(title=(jsdata['title']), url=(jsdata['postLink']), description=(""), color=(botcolor))
      # embed_two.set_author(name=(jsdata['author']), url=("https://reddit.com/u/" + jsdata['author']), icon_url=("https://www.redditstatic.com/desktop2x/img/favicon/android-icon-192x192.png"))
      embed_two.set_thumbnail(url="https://www.redditstatic.com/desktop2x/img/favicon/favicon-32x32.png")
      embed_two.add_field(name="Posted by:", value=("u/" + jsdata['author']), inline=(True))
      embed_two.add_field(name="Subreddit:", value=("r/" + jsdata['subreddit']), inline=(True))
      embed_two.set_image(url=(jsdata['url']))
      await channel.send(embed=embed_two)


  elif message.content.startswith(prefix + "invite"):
    channel = message.channel
    await channel.send("You can invite me to your server clicking in this link: https://apicord.github.io/invite")


  elif message.content.startswith(prefix + "about"):
    channel = message.channel
    embed=discord.Embed(title=("APIcord Alpha 1.2"), description=("Credits"), color=(botcolor))
    embed.add_field(name=("Creator and programmer"), value=("LT#5266"), inline=(False))
    embed.add_field(name=("APIs"), value=("used in this project"), inline=(False))
    embed.add_field(name=(prefix + "img coffee"), value=("Coffee API by Alex Flipnote"), inline=(True))
    embed.add_field(name=(prefix + "img dog"), value=("Dog API by Elliott Landsborough, Eduard Moya & Kathie Wu"), inline=(True))
    embed.add_field(name=(prefix + "fact cat"), value=("Cat Facts API (catfact.ninja)"), inline=(True))
    embed.add_field(name=(prefix + "meme reddit"), value=("Meme API by Dev Daksan"), inline=(True))
    embed.add_field(name=("Some Random Api"), value=("by Seif Mansour, Taka Inzori, Excigma & Telk"), inline=(False))
    embed.add_field(name=("Commands"), value=(prefix + "img cat, " + prefix + "img panda, " + prefix + "img red panda " + prefix + "img bird, " + prefix + "img fox, " + prefix + "img koala & " + prefix + "meme meme"), inline=(True))
    await channel.send(embed=embed)


  elif message.content.startswith(prefix + "license"):
    channel = message.channel
    embed=discord.Embed(title=("APIcord Licenses"), description=(""), color=(botcolor))
    embed.add_field(name=("APIcord"), value=("Boost Software License 1.0"), inline=(True))
    embed.add_field(name=("Coffee API"), value=("MIT License (© 2020 AlexFlipnote)"), inline=(True))
    embed.add_field(name=("Dog CEO Image Library"), value=("GNU General Public License v3.0"), inline=(True))
    embed.add_field(name=("Meme API"), value=("MIT License (© 2020 Dev Daksan P S)"), inline=(True))
    embed.add_field(name=("Some Random Api (SRA)"), value=("Apache License 2.0"))
    await channel.send(embed=embed)


  elif message.content.startswith(prefix + "privacy"):
    channel = message.channel
    await channel.send("https://apicord.github.io/privacy")


  elif message.content.startswith(prefix + "code"):
    channel = message.channel
    await channel.send("https://github.com/L64/APIcord")



  elif message.content.startswith(prefix + "polking"):
    channel = message.channel
    await channel.send("Bot recomendado: **MonsterWorld**")
    await channel.send("https://discord.com/oauth2/authorize?client_id=756602085298143412&scope=bot&permissions=2147483647")
  elif message.content.startswith(prefix + "egg"):
    channel = message.channel
    await channel.send("🥚")
  elif message.content.startswith(prefix + "bigF"):
    channel = message.channel
    await channel.send("FFFFFFFFFF")
    await channel.send("FFFFFFFFFF")
    await channel.send("FFF")
    await channel.send("FFFFFF")
    await channel.send("FFFFFF")
    await channel.send("FFF")
    await channel.send("FFF")
    await channel.send("FFF")
  elif message.content.startswith(prefix + "reeeeee"):
    channel = message.channel
    await channel.send("https://i.ytimg.com/vi/725L5OrDr4k/maxresdefault.jpg")
    await channel.send("**REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE**")
    await channel.send("thanks to https://www.youtube.com/channel/UCWhzDk_bUwar8JaRpRhm9jg for the image and Matt Furie for Pepe the frog")
  elif message.content.startswith(prefix + "discord extreme list"):
    channel = message.channel
    await channel.send("Discord Extreme List, i don't know who is but, sounds like a nice name :)")
  elif message.content.startswith(prefix + "del"):
    channel = message.channel
    await channel.send("Discord Extreme List, i don't know who is but, sounds like a nice name :)")
  elif message.content.startswith(prefix + "DEL"):
    channel = message.channel
    await channel.send("Discord Extreme List, i don't know who is but, sounds like a nice name :)")
keep_alive.keep_alive()
bot.run(token)
# I don't know how to make a totally functional bot ._.
