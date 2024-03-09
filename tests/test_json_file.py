import pytest
from pokemon_utils import PokemonData, PokemonConnection

pd = PokemonData()
pc = PokemonConnection()


def test_pokemon_type_response():
    response = pc.connect_to_api(path='type')
    assert response.status_code == 200
    assert response.json()


def test_counting_pokemon_types():
    response = pc.connect_to_api(path='type')
    # This test the len of the results from response json file.
    assert len(response.json()['results']) == 20
    # Here we get the "count" value directly from the json file.
    assert response.json()['count'] == 20


def test_pokemon_existence_by_id(poke_type='fire'):
    # Get the ID of pokemon type.
    poke_type_id = pd.get_type_id(poke_type)
    pokemons_list = pd.get_pokemon_list_by_type_id(poke_type)
    assert "charmander" in pokemons_list, 'Not exits on the list'
    assert "bulbasaur" in pokemons_list, 'Not exits on the list'
    assert poke_type_id == 10


def test_heaviest_fire_type_pokemon():
    expected_weights = {
        'charizard-gmax': 10000,
        'cinderace-gmax': 10000,
        'coalossal-gmax': 10000,
        'centiskorch-gmax': 10000,
        'groudon-primal': 9997
    }


if __name__ == "__main__":
    pytest.main()
