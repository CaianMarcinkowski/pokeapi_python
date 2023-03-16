from main import app
import requests

hostname = 'http://pokeapi.co/api/v2'
path = '/pokemon/1/'

@app.route('/allPokemon')

def allPokemon():
    request = requests.get(hostname+path)
    return request.content