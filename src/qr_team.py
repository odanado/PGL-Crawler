from request_pgl import RequestPGL, Language
from utils import save


def main():
    for lang in Language:
        print(lang)
        pgl = RequestPGL(lang)
        poke = pgl.fetch_pokemon(False)
        save(poke, 'data/{}'.format(lang.name), 'pokemon.json')

        moves = pgl.fetch_moves()
        save(moves, 'data/{}'.format(lang.name), 'moves.json')

        abilities = pgl.fetch_abilities()
        save(abilities, 'data/{}'.format(lang.name), 'abilities.json')

        items = pgl.fetch_items()
        save(items, 'data/{}'.format(lang.name), 'items.json')


if __name__ == '__main__':
    main()
