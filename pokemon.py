import requests

url = "https://pokeapi.co/api/v2/berry/"
berryin = input()

response = requests.get(url+berryin)
print(response.json())