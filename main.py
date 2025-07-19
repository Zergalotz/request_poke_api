import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/")
response.raise_for_status()  # Ensure we raise an error for bad responses

pokemon_data = response.json()

for pokemon in pokemon_data['results']:
    print(pokemon['name'])