import unittest
import discord
from utils import utils
import app


class TestUtils(unittest.TestCase):
    def test_utils_trump(self):
        self.assertIsNotNone(utils.trump())

    def test_utils_chuck(self):
        self.assertIsNotNone(utils.chuck())


class TestApp(unittest.TestCase):
    def test_app_token(self):
        self.assertIsNotNone(app.TOKEN)

    def test_app_guild(self):
        self.assertIsNotNone(app.GUILD)

    def test_app_crypto_api(self):
        self.assertIsNotNone(app.CRYPTO_API)

    def test_discord_client(self):
        self.assertIsInstance(app.DiscordClient(), discord.Client)


if __name__ == '__main__':
    unittest.main()
    print(app.CRYPTO_API)
