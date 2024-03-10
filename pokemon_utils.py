import requests


class PokemonConnection:
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/'

    def connect_to_api(self, path=''):
        """
        :param path: An addition to the original path. i.e.: 'https://pokeapi.co/api/v2/' + 'type'
        :return: Json response from selected path.
        """
        return requests.get(self.url + path)


class PokemonData(PokemonConnection):

    def get_poke_type_id(self, poke_type):
        """
        :param poke_type: could be : fire, water, shadow, rock, steel etc...
        :return: the type ID.
        """
        data = self.connect_to_api("type").json()['results']
        type_id = None
        for i in data:
            if i['name'] != poke_type:
                continue
            type_id = i['url'].split('/')[-2]
        return int(type_id)

    def get_pokemon_list_by_type_id(self, poke_type):
        # Get ID for API url.
        id_for_url = self.get_poke_type_id(poke_type)
        # Get pokemons list by API URL ID.
        pokemons_list_type_id = self.connect_to_api(f"type/{id_for_url}").json()['pokemon']
        # Get a list of all existing pokemons under selected type.
        existing_pokemons = [p_name['pokemon']['name'] for p_name in pokemons_list_type_id]
        return existing_pokemons

    def get_pokemons_url_by_type(self, poke_type):
        # Get ID for API url.
        id_for_url = self.get_poke_type_id(poke_type)
        # Get pokemons list by API URL ID.
        pokemons_list_type_id = self.connect_to_api(f"type/{id_for_url}").json()['pokemon']
        poke_urls = {i['pokemon']['name']: i['pokemon']['url'] for i in pokemons_list_type_id}
        return poke_urls

    def get_poke_weight_by_name(self, poke_name, poke_type):
        poke_url = None
        poke_dict = self.get_pokemons_url_by_type(poke_type)
        for poke in poke_dict:
            if poke != poke_name:
                continue
            poke_url = poke_dict[poke]
            break
        if poke_url is None:
            return False
        return requests.get(poke_url).json()['weight']

