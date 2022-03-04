import logging
from os import getenv
from datetime import datetime, timedelta
import discord
import requests


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


def qr_code(tekst: str) -> str:
    '''return url for QR code'''
    return f"https://image-charts.com/chart?chs=150x150&cht=qr&chl={tekst}&choe=UTF-8"


def chuck() -> str:
    '''return Chuck Norris joke'''
    return requests.get('https://api.chucknorris.io/jokes/random').json()['value']


def trump() -> str:
    '''return Trump quotes'''
    return requests.get('https://tronalddump.io/random/quote').json()['value']


def get_crypto() -> str:
    '''return crypto prices '''
    cryptos = ["BTC", "LTC", "ETC", "BCH", "XLM",
               "NEO", "ETH", "XRP", "DASH", "STORJ"]
    baseurl = "https://min-api.cryptocompare.com/data/pricemulti"
    url = f"{baseurl}?fsyms={','.join(cryptos)}&tsyms=USD&api_key={CRYPTO_API}"
    response = requests.get(url).json()
    logging.debug(response)
    return ('\t').join([x+" : "+str(y['USD']) for x, y in response.items()])


class DiscordClient(discord.Client):
    '''Discord client'''
    KOMMANDOER = "!lunch , !google , !trump , !chuck , !crypto , !qr"

    async def on_ready(self) -> None:
        '''Discord client connected'''
        logging.info("Logged on as %s in %s", self.user, self.guilds[0].name)

    async def on_message(self, message) -> None:
        '''message handler '''
        logging.debug("%s : %s in %s", client.user,
                      message.content, message.channel)
        if message.author == client.user:
            pass

        match message.content.lower().split():
            case ["!help"]:
                await message.channel.send(f"Mulige kommandoer: {self.KOMMANDOER} ")
            case ["ping"]:
                await message.channel.send("pong")
            case ["!chuck"]:
                await message.channel.send(chuck())
            case ["!trump"]:
                await message.channel.send(trump())
            case ["!lunch"]:
                await message.channel.send(lunch())
            case ["!crypto"]:
                await message.channel.send(get_crypto())
            case ["!qr", *args]:
                if len(args) > 0:
                    await message.channel.send(qr_code(('+').join(args)))
                else:
                    await message.channel.send('Riktig bruk er : !QR TEKST')
            case ["!google", *args]:
                if len(args) > 0:
                    await message.channel.send(f"https://google.com/search?q={('+').join(args)}")
                else:
                    await message.channel.send('Riktig bruk er : !google SØKEORD')
            case _:
                logging.debug(message)


client = DiscordClient()
client.run(TOKEN)
