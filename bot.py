import discord
import json
import urllib3


# Token and prefix
token = ("[BOT TOKEN]")
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
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="APIs"))
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
    embed.add_field(name=(prefix + "about"), value=("Creditos del bot"), inline=True)
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
      embed_two=discord.Embed(title=jsdata['title'], url=jsdata['postLink'], description="Raro", color=0xff0000)
      embed_two.add_field(name="Posted by:", value="u/" + jsdata['author'], inline=True)
      embed_two.add_field(name="Subreddit:", value="r/" + jsdata['subreddit'], inline=True)
      await channel.send(jsdata['url'])
      await channel.send(embed=embed_two)
  elif message.content.startswith(prefix + "invite"):
    await channel.send("Podés invitarme a tu servidor desde acá: https://apicord.github.io/invite")
  #elif message.content.startswith(prefix + "about"):
    #channel = message.channel
    #about_embed=discord.Embed(title=("APIcord"), description=(""), color=0xff0000)
    #about_embed.add_field(name=("Creator & programmer"), value=("LT#5266"), inline=False
    #api_embed=discord.Embed(title=("API Providers"), description=(""), color=0xff0000)
    #api_embed.add_field(name=(prefix + "coffee"), value=("Coffee API (https://coffee.alexflipnote.dev)"), inline=True)
    #api_embed.add_field(name=(prefix + "dog"), value=("Dog CEO's Dog API (https://dog.ceo/dog-api)"), inline=True)
    #api_embed.add_field(name=(prefix + "cat"), value=("TheCatAPI.com"), inline=True)
    #api_embed.add_field(name=(prefix + "reddit"), value=("Meme API (https://github.com/R3l3ntl3ss/Meme_Api)"), inline=True)
    #await channel.send(embed=about_embed)
    #await channel.send(embed=api_embed)
bot.run(token)
# I don't know how to make a totally functional bot ._.
