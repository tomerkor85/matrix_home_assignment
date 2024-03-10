import requests


class PokemonConnection:
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/'

    def connect_to_api(self, path=''):
        """
        :param path: An addition to the original path. i.e.: 'https://pokeapi.co/api/v2/' + 'type'
        :return: Json response from selected path.
        """
        try:
            response = requests.get(self.url + path)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to API: {e}")
            raise ConnectionError(f"API connection error: {e}")  # Raise specific exception


class PokemonData(PokemonConnection):

    def get_poke_type_id(self, poke_type):
        """
        This function is about to get the ID of Pokemons by type.
        :param poke_type: could be : fire, water, shadow, rock, steel etc...
        :return: the type ID.
        """
        try:
            data = self.connect_to_api("type").json()['results']
            for entry in data:
                if entry.get('name') == poke_type:
                    return int(entry['url'].split('/')[-2])
            raise ValueError(f"Type '{poke_type}' not found.")
        except (KeyError, ValueError) as e:
            print(f"Error getting type ID: {e}")
            raise ValueError(f"Error getting type ID: {e}")  # Raise specific exception

    def get_pokemon_list_by_type_id(self, poke_type):
        """
        This function getting the pokemon list by the type ID.
        :param poke_type: could be : fire, water, shadow, rock, steel etc...
        :return: List of pokemons under the selected type.
        """
        try:
            id_for_url = self.get_poke_type_id(poke_type)
            pokemons_list_type_id = self.connect_to_api(f"type/{id_for_url}").json()['pokemon']
            existing_pokemons = [p_name['pokemon']['name'] for p_name in pokemons_list_type_id]
            return existing_pokemons
        except Exception as e:
            print(f"Error getting Pokemon list by type ID: {e}")
            raise Exception(f"Error getting Pokemon list by type ID: {e}")  # Raise custom exception

    def get_pokemons_url_by_type(self, poke_type):
        """
        This function will get the pokemons url.
        :param poke_type: could be : fire, water, shadow, rock, steel etc...
        :return: list of Dicts with {pokemon_name: pokemon_url}
        """
        # Get ID for API url.
        id_for_url = self.get_poke_type_id(poke_type)
        # Ensure id_for_url is valid
        if id_for_url is None:
            raise ValueError(f"Invalid type '{poke_type}'")
        try:
            # Get pokemons list by API URL ID.
            pokemons_list_type_id = self.connect_to_api(f"type/{id_for_url}").json()['pokemon']
            poke_urls = {i['pokemon']['name']: i['pokemon']['url'] for i in pokemons_list_type_id}
            return poke_urls
        except (KeyError, ValueError) as e:
            print(f"Error getting Pokemon URLs by type: {e}")
            raise Exception(f"Error getting Pokemon URLs by type: {e}")  # Raise custom exception

    def get_poke_weight_by_name(self, poke_name, poke_type):
        """
        This function will get the weight of specific pokemon by given name and type.
        :param poke_name: Pokemon name i.e. : "charmander"
        :param poke_type: could be : fire, water, shadow, rock, steel etc...
        :return: Pokemon weight.
        """
        try:
            poke_urls = self.get_pokemons_url_by_type(poke_type)
            poke_url = poke_urls.get(poke_name)
            if poke_url is None:
                raise ValueError(f"Pokemon '{poke_name}' not found in type '{poke_type}'.")
            response = requests.get(poke_url)
            response.raise_for_status()  # Raise exception for non-200 status codes
            return response.json().get('weight')
        except Exception as e:
            print(f"Error getting Pokemon weight by name: {e}")
            raise Exception(f"Error getting Pokemon weight by name: {e}")
