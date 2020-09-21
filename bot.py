import time
import discord
import json
import urllib3


# Token and prefix
token = ("NzU3MjU4Mjk4NzI1NjMwMDA4.X2dxvw.z5mgs-EO1_AEd5K-HA_XGp0TkRc")
prefix = ("api!")
CoffeeAPI = ("https://coffee.alexflipnote.dev/random.json")


# Start stuff
bot = discord.Client()
embed = discord.Embed
http = urllib3.PoolManager()
print("Man, there isn't nothing to see here, it's a normal Discord.py bot.")
# Status
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="APIs | " + prefix + "help"))
# Good part
@bot.event
async def on_message(message):
  if message.content.startswith(prefix + "nice"):
    channel = message.channel
    await channel.send("Thank you! You're nice too 👍")
  elif message.content.startswith(prefix + "help"):
    channel = message.channel

    embed=discord.Embed(title=("APIcord"), description=("Help"), color=(0xff0000))
    embed.add_field(name=(prefix + "help"), value=("Meme aleatorio"), inline=True)
    embed.add_field(name=(prefix + "coffee"), value=("Imagén de café aleatorio"), inline=True)
    embed.add_field(name=(prefix + "dog"), value=("Imagen de perro aleatoria"), inline=True)
    embed.add_field(name=(prefix + "cat"), value=("Imagen de gato aleatoria"), inline=True)

    embed.add_field(name=("Meme commands"), value=("lol."), inline=False)
    embed.add_field(name=(prefix + "reddit"), value=("Random Reddit meme"), inline=True)

    embed.add_field(name=("About the bot"), value=("License, privacy, credits, etc."), inline=False)
    embed.add_field(name=(prefix + "about"), value=("Credits"), inline=True)
    embed.add_field(name=(prefix + "license"), value=("License"), inline=True)
    embed.add_field(name=(prefix + "invite"), value=("Displays bot invite"), inline=True)
    embed.add_field(name=(prefix + "privacy"), value=("Bot Privacy Policy"), inline=True)

    await channel.send(embed=embed)
  elif message.content.startswith(prefix + "coffee"):
    channel = message.channel
    jdat = (http.request('GET', 'https://coffee.alexflipnote.dev/random.json'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title="Acá te traje un café", description="Espero que te guste uwu", color=0xff0000)
    embed.set_footer(text="Powered by Coffe API (https://coffee.alexflipnote.dev)")
    await channel.send(embed=embed)
    await channel.send(jsdata['file'])
  elif message.content.startswith(prefix + "dog"):
    channel = message.channel
    jdat = (http.request('GET', 'https://dog.ceo/api/breeds/image/random'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    embed=discord.Embed(title="Un perrito :D", description="Espero que te guste uwu", color=0xff0000)
    await channel.send(embed=embed)
    await channel.send(jsdata['message'])
  elif message.content.startswith(prefix + "cat"):
    embed=discord.Embed(title="Coming soon", description="", color=0xff0000)
    await channel.send(embed=embed)
  elif message.content.startswith(prefix + "reddit"):
    channel = message.channel
    jdat = (http.request('GET', 'https://meme-api.herokuapp.com/gimme'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    if jsdata['nsfw'] == "true":
      embed=discord.Embed(title="Este meme es NSFW", description="Vamos a recargar este comando, disculpe las molestias.", color=0xff0000)
      await channel.send(embed=embed)
      await channel.send(prefix + "reddit")
    else:
      #Embed
      embed_two=discord.Embed(title=jsdata['title'], url=jsdata['postLink'], description="", color=0xff0000)
      # embed_two.set_author(name=(jsdata['author']), url=("https://reddit.com/u/" + jsdata['author']), icon_url=("https://www.redditstatic.com/desktop2x/img/favicon/android-icon-192x192.png"))
      embed_two.set_thumbnail(url="https://www.redditstatic.com/desktop2x/img/favicon/favicon-32x32.png")
      embed_two.add_field(name="Posted by:", value="u/" + jsdata['author'], inline=True)
      embed_two.add_field(name="Subreddit:", value="r/" + jsdata['subreddit'], inline=True)
      await channel.send(jsdata['url'])
      await channel.send(embed=embed_two)
  elif message.content.startswith(prefix + "invite"):
    await channel.send("Podés invitarme a tu servidor desde acá: https://apicord.github.io/invite")
  elif message.content.startswith(prefix + "about"):
    channel = message.channel
    embed=discord.Embed(title=("APIcord"), description=("Credits"), color=(0xff0000))
    embed.add_field(name=("Creator and programmer"), value=("LT#5266"), inline=False)
    embed.add_field(name=("APIs"), value=("used in this project"), inline=False)
    embed.add_field(name=(prefix + "coffee"), value=("Coffee API by Alex Flipnote"), inline=True)
    embed.add_field(name=(prefix + "dog"), value=("Dog API by Elliott Landsborough"), inline=True)
    embed.add_field(name=(prefix + "cat"), value=("TheCatAPI by Aden Forshaw"), inline=True)
    embed.add_field(name=(prefix + "reddit"), value=("Meme API by Dev Daksan"), inline=True)
    embed.add_field(name=("Under Boost Software License 1.0"), value=("https://github.com/L64/APIcord/blob/master/LICENSE"), inline=False)
    await channel.send(embed=embed)
  elif message.content.startswith(prefix + "license"):
    channel = message.channel
    embed=discord.Embed(title=("APIcord is under Boost Software License 1.0"), description=(""), color=(0xff0000))
    await channel.send(embed=embed)
    await channel.send("https://github.com/L64/APIcord/blob/master/LICENSE")
  elif message.content.startswith(prefix + "privacy"):
    channel = message.channel
    await channel.send("https://apicord.github.io/privacy")
bot.run(token)
# I don't know how to make a totally functional bot ._.
