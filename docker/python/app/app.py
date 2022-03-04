import logging
from os import getenv
import discord
from utils import utils

logging.basicConfig(level=logging.INFO)

TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')
CRYPTO_API = getenv('CRYPTO_API')

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
                await message.channel.send(utils.chuck())
            case ["!trump"]:
                await message.channel.send(utils.trump())
            case ["!lunch"]:
                await message.channel.send(utils.lunch())
            case ["!crypto"]:
                await message.channel.send(utils.get_crypto(CRYPTO_API))
            case ["!qr", *args]:
                if len(args) > 0:
                    await message.channel.send(utils.qr_code(('+').join(args)))
                else:
                    await message.channel.send('Riktig bruk er : !QR TEKST')
            case ["!google", *args]:
                if len(args) > 0:
                    await message.channel.send(f"https://google.com/search?q={('+').join(args)}")
                else:
                    await message.channel.send('Riktig bruk er : !google SØKEORD')
            case _:
                logging.debug(message)

if __name__ == '__main__':
    client = DiscordClient()
    client.run(TOKEN)
