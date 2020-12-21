import requests
import json
from config import currency


class ConvertionException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quote= str,base= str,amount= str):


        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = currency[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        total_base = round(float(amount)*float(json.loads(r.content)['rates'][currency[base]]),2)



        return total_base
