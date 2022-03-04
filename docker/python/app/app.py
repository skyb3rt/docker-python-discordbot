from os import getenv
from random import random
from urllib.request import urlopen
from datetime import datetime, timedelta
import discord
import requests
from flask import json


TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')
CRYPTO_API = getenv('CRYPTO_API')

client = discord.Client()


def lunch()->str:
    '''return comic'''
    date = datetime.now()
    if date.isoweekday() > 5:
        date -= timedelta(days=7-date.isoweekday())
    dateformated = date.strftime("%Y-%m-%d")
    return 'https://api.e24.no/content/v1/comics/' + dateformated


def qrCode(tekst:str)->str:
    '''return url for QR code'''
    return f"https://image-charts.com/chart?chs=150x150&cht=qr&chl={tekst}&choe=UTF-8"

def chuck()->str:
    '''return Chuck Norris joke'''
    return requests.get('https://api.chucknorris.io/jokes/random').json()['value']


def trump()->str:
    '''return Trump quotes'''
    return requests.get('https://tronalddump.io/random/quote').json()['value']


def getCrypto(type:str='all')->str:
    '''return crypto prices '''
    cryptos = ["BTC", "LTC", "ETC", "BCH", "XLM",
               "NEO", "ETH", "XRP", "DASH", "STORJ"]
    url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={','.join(cryptos)}&tsyms=USD&api_key={CRYPTO_API}"
    response = requests.get(url).json()
    r = ''
    for type in cryptos:
        r += f"{type}: {response[type]['USD']} \t"
        return r


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.content).lower() == '!chuck':
        await message.channel.send(chuck())

    if str(message.content).lower().startswith('!crypto'):
        parts = str(message.content).split(' ')
        if len(parts) > 1:
            await message.channel.send(get_crypto(parts[1].upper()))
        else:
            await message.channel.send(get_crypto())

    if str(message.content).lower() == '!trump':
        await message.channel.send(trump())

    if str(message.content).lower() == '!help':
        await message.channel.send(' Mulige kommandoer: !lunch , !stackoverflow , !trump , !chuck , !crypto , !QRcode')

    if str(message.content).lower().startswith('!stackoverflow'):
        parts = str(message.content).split(' ')
        søkeord = (' ').join(parts[1:])
        if len(parts) > 1:
            await message.channel.send(stackoverflow(søkeord.upper()))
        else:
            await message.channel.send('Hva vil du søke på? Riktig bruk er : !stackoverflow SØKEORD')

    if str(message.content).lower() == '!lunch':
        await message.channel.send(lunch())

    if str(message.content).lower().startswith('!qrcode'):
        parts = str(message.content).split(' ')
        tekst = (' ').join(parts[1:])
        if len(parts) > 1:
            await message.channel.send(qr_code(tekst.upper()))
        else:
            await message.channel.send('Hva vil du lage QR code for? Riktig bruk er : !QRcode TEKST')

client.run(TOKEN)
