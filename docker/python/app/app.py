import logging
from os import getenv
from random import random
from urllib.request import urlopen
from datetime import datetime, timedelta
import discord
import requests
from flask import json


logging.basicConfig(level=logging.INFO)

TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')
CRYPTO_API = getenv('CRYPTO_API')


def lunch() -> str:
    '''return comic'''
    date = datetime.now()
    if date.isoweekday() > 5:
        date -= timedelta(days=7-date.isoweekday())
    dateformated = date.strftime("%Y-%m-%d")
    return 'https://api.e24.no/content/v1/comics/' + dateformated


def qrCode(tekst: str) -> str:
    '''return url for QR code'''
    return f"https://image-charts.com/chart?chs=150x150&cht=qr&chl={tekst}&choe=UTF-8"


def chuck() -> str:
    '''return Chuck Norris joke'''
    return requests.get('https://api.chucknorris.io/jokes/random').json()['value']


def trump() -> str:
    '''return Trump quotes'''
    return requests.get('https://tronalddump.io/random/quote').json()['value']


def getCrypto() -> str:
    '''return crypto prices '''
    cryptos = ["BTC", "LTC", "ETC", "BCH", "XLM",
               "NEO", "ETH", "XRP", "DASH", "STORJ"]
    url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={','.join(cryptos)}&tsyms=USD&api_key={CRYPTO_API}"
    response = requests.get(url).json()
    r = ''
    for crypto in cryptos:
        r += f"{crypto}: {response[crypto]['USD']} \t"
    return r


class discord_client(discord.Client):

    async def on_ready(self):
        logging.info(f"Logged on as {self.user} in {self.guilds[0].name}")

    async def on_message(self, message):
        logging.debug(
            f"{client.user} : {message.content} in {message.channel}")
        if message.author == client.user:
            pass

        match message.content.lower().split():
            case ["!help"]:
                await message.channel.send("Mulige kommandoer: !lunch , !google , !trump , !chuck , !crypto , !qr")
            case ["ping"]:
                await message.channel.send("pong")
            case ["!chuck"]:
                await message.channel.send(chuck())
            case ["!trump"]:
                await message.channel.send(trump())
            case ["!lunch"]:
                await message.channel.send(lunch())
            case ["!crypto"]:
                await message.channel.send(getCrypto())
            case ["!qr", *args]:
                if len(args) > 0:
                    await message.channel.send(qrCode(('+').join(args)))
                else:
                    await message.channel.send('Hva vil du lage QR code for? Riktig bruk er : !QR TEKST')
            case ["!google", *args]:
                if len(args) > 0:
                    await message.channel.send(f"https://google.com/search?q={('+').join(args)}")
                else:
                    await message.channel.send('Hva vil du søke på? Riktig bruk er : !google SØKEORD')
            case _:
                logging.debug(message)


client = discord_client()
client.run(TOKEN)
