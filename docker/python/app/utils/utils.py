import logging
from datetime import datetime, timedelta
import requests
logging.basicConfig(level=logging.INFO)
 
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


def get_crypto(api_key) -> str:
    '''return crypto prices '''
    cryptos = ["BTC", "LTC", "ETC", "BCH", "XLM",
               "NEO", "ETH", "XRP", "DASH", "STORJ"]
    baseurl = "https://min-api.cryptocompare.com/data/pricemulti"
    url = f"{baseurl}?fsyms={','.join(cryptos)}&tsyms=USD&api_key={api_key}"
    response = requests.get(url).json()
    logging.debug(response)
    return ('\t').join([x+" : "+str(y['USD']) for x, y in response.items()])
