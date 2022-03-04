import unittest
import discord
from utils import utils
import app

class TestUtils(unittest.TestCase):
    '''Tests utils'''

    def test_utils_trump(self):
        '''test trump quote is not None'''
        self.assertIsNotNone(utils.trump())

    def test_utils_chuck(self):
        '''test chuck quote is not None'''
        self.assertIsNotNone(utils.chuck())

class TestApp(unittest.TestCase):
    '''Test app'''

    def test_app_token(self):
        '''test enviroment variabel TOKEN is set'''
        self.assertIsNotNone(app.TOKEN)

    def test_app_guild(self):
        '''test enviroment variabel GUILD is set'''
        self.assertIsNotNone(app.GUILD)

    def test_app_crypto_api(self):
        '''test enviroment variabel CRYPTO_API is set'''
        self.assertIsNotNone(app.CRYPTO_API)

    def test_discord_client(self):
        '''test DiscordClient is instance of discord.Client'''
        self.assertIsInstance(app.DiscordClient(), discord.Client)


if __name__ == '__main__':
    unittest.main()
