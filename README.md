# API Test Automation - Home Assignment
*This repository contains the solution to the API test automation home assignment, which involves interacting with the Pokémon API using Python and the pytest framework.*

Assignment Scenarios:
1. Verify Pokémon Type API Response
Use the resource https://pokeapi.co/api/v2/type.
Verify that the Pokémon type API returns a response with type JSON.
Verify that there are exactly 20 different Pokémon types.


2. Find ID of “Fire Type” Pokémon
Find the ID of the “Fire type” Pokémon.
Validate that:
Pokémon “charmander” is in the JSON of the Fire Pokémon list.
Pokémon “bulbasaur” is not in the JSON of the Fire Pokémon list.


3. Identify Five Heaviest Pokémon of the Fire Type
Identify the five heaviest Pokémon of the Fire type.
Ensure they have the expected weights:
   - ‘charizard-gmax’: ‘weight’: 10000
   - ‘cinderace-gmax’: ‘weight’: 10000
   - ‘coalossal-gmax’: ‘weight’: 10000
   - ‘centiskorch-gmax’: ‘weight’: 10000
   - ‘groudon-primal’: ‘weight’: 9997


Libraries Used:
- requests: Used to interact with the Pokémon API.
- pytest: Used for writing and executing test cases.

Test Function Details:
* test_pokemon_api.py - 
*Contains test functions for the given scenarios.*

## Installation:
Please install requirements.txt file before using this project.
`pip install -r requirements.txt`

## Run tests
1. You can run test by type in command line : `pytest -v`
2. You can use IDE to run tests.

### Questions
* If you have any questions about the project feel free to contact me via Email: **tomerkor1985@gmail.com**