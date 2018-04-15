import requests
import time
import json
from enum import Enum

_post = requests.post


class Language(Enum):
    Japanese = 1
    English = 2
    French = 3
    Spanish = 4
    German = 5
    Italian = 7
    Korean = 8
    MandarinChinese = 9
    CantoneseChinese = 10


class RequestPGL(object):

    def __init__(self, lang=Language.Japanese):
        self.lang = lang
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'

    def _default_data(self):
        return {
            'timezone': 'JST',
            'languageId': self.lang.value,
            'timeStamp': int(time.time())
        }

    def fetch_pokemon(self, order_by_name=True):
        data = self._default_data()
        data['searchFlg'] = 0 if order_by_name else 1

        url = 'https://3ds.pokemon-gl.com/frontendApi/master/getPokemon'
        referer = 'https://3ds.pokemon-gl.com/rentalteam/search'

        r = _post(url,
                  headers={'referer': referer,
                           'User-Agent': self.user_agent},
                  data=data)

        return json.loads(r.text)['pokemonInfo']

    def fetch_moves(self):
        data = self._default_data()

        url = 'https://3ds.pokemon-gl.com/frontendApi/master/getPokemonWaza'
        referer = 'https://3ds.pokemon-gl.com/rentalteam/search'

        r = _post(url,
                  headers={'referer': referer,
                           'User-Agent': self.user_agent},
                  data=data)

        return json.loads(r.text)['pokemonWazaInfo']

    def fetch_abilities(self):
        data = self._default_data()

        url = 'https://3ds.pokemon-gl.com/frontendApi/master/getPokemonTokusei'
        referer = 'https://3ds.pokemon-gl.com/rentalteam/search'

        r = _post(url,
                  headers={'referer': referer,
                           'User-Agent': self.user_agent},
                  data=data)

        return json.loads(r.text)['tokuseiInfo']

    def fetch_items(self):
        data = self._default_data()

        url = 'https://3ds.pokemon-gl.com/frontendApi/master/getItemList'
        referer = 'https://3ds.pokemon-gl.com/rentalteam/search'

        r = _post(url,
                  headers={'referer': referer,
                           'User-Agent': self.user_agent},
                  data=data)

        return json.loads(r.text)['itemInfo']

    def search_battle_team(battle_type, pokemon_id):
        pass
