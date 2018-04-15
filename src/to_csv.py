import pandas as pd

from request_pgl import Language
from utils import load


def pokemon():
    df = pd.DataFrame(columns=['id'] + [lang.name for lang in Language])
    for lang in Language:
        path = 'data/{}'.format(lang.name)
        poke = load(path, 'pokemon.json')
        names = []
        sorted_poke = sorted(poke, key=lambda x: (x['monsno'], x['pokemonId']))
        for x in sorted_poke:
            name = x['name']
            if x['formName']:
                name += '({})'.format(x['formName'])

            names.append(name)
        df[lang.name] = names
        if lang.name == 'Japanese':
            ids = [x['monsno'] for x in sorted_poke]
            df['id'] = ids

    df.to_csv('pokemon.csv')


def process(name, output_key, sort_key):
    df = pd.DataFrame(columns=[lang.name for lang in Language])
    for lang in Language:
        path = 'data/{}'.format(lang.name)
        moves = load(path, '{}.json'.format(name))
        df[lang.name] = [x[output_key]
                         for x in sorted(moves, key=lambda x: x[sort_key])]

    # df.to_csv('{}.csv'.format(name))
    for _, x in df.iterrows():
        print('{}\t{}\t固有名詞'.format(
            x[Language.Japanese.name], x[Language.English.name]))


def main():
    pokemon()
    # ja = load('data/{}'.format(Language.Japanese.name), 'pokemon.json')
    # en = load('data/{}'.format(Language.English.name), 'pokemon.json')

    # used = set()
    # for x, y in sorted(zip(ja, en), key=lambda x: (x[0]['monsno'], x[0]['pokemonId'])):
    #     if not x['monsno'] in used:
    #         print('{}\t{}\t固有名詞'.format(x['name'], y['name']))
    #         used.add(x['monsno'])
    # process('moves', 'wazaName', 'wazaId')
    # process('abilities', 'tokuseiName', 'tokuseiId')
    # process('items', 'itemName', 'itemId')


if __name__ == '__main__':
    main()
