import discord
from discord.ext import commands
from config import TOKEN
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def nasılsın(ctx):
    await ctx.send(f'iyiyim sen nasılsın')

@bot.command()
async def çevre_kirliliği_nedir(ctx):
    await ctx.send(f'Çevre kirliliği, insan faaliyetleri sonucunda doğaya yabancı maddelerin karışarak hava, su ve toprağın doğal yapısını, bileşimini ve ekolojik dengeyi bozmasıdır')

@bot.command()
async def çevre_kirliliğine_karşı_çıkan_kişiler(ctx):
    await ctx.send(f'Sivil Toplum Kuruluşları ayrıca bireysel ve toplumlar')



@bot.command()
async def çevre_kirliliğine_örnekler(ctx):
    await ctx.send(f'toprak kirliliği karbon salınımı elektrik ')

@bot.command()
async def botseniçokseviyorum(ctx):
    await ctx.send(f'bende seni')

@bot.command()
async def üzüldüm(ctx):
    await ctx.send(f'üzülme mutlu ol')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def cevre1(ctx):
    with open('images/cevre1.jpeg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


@bot.command()
async def çevre_kirliliği_fotoğrafı(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(TOKEN)