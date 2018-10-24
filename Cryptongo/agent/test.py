import requests #Librería para capturar peticiones rest
import pymongo #Librería para comunicarse con la bd mongodb

API_URL = "https://api.coinmarketcap.com/v1/ticker/" #Url desde donde se obtiene los datos a guardar en mongodb

#Función para crear conexión a la bd
def get_db_connection(uri):
	client = pymongo.MongoClient(uri) #Crear una conexión a la bd
	return client.cryptongo #Devolver bd cryptongo

#Función para obtener datos del api externa
def get_cryptocurrencies_from_api():
	r = requests.get(API_URL) #Obtener datos de la url del api externa
	if r.status_code == 200: #Si devuelve 200
		result = r.json() #Formatear resultados en formato json
		return result #Devolver resultado

	raise Exception('Api Error'); #En caso de no recibir 200 del api, devolver un error forzado

def first_element(elements):
	return elements[0] #Devolver el key de elements

def get_hash(value):
	from hashlib import sha512 #Función para encriptar
	return sha512( #Encripto
		value.encode('utf-8') #El string codificado en utf-8, requisito de la librería hash
	).hexdigest() #Convertir encriptado en un string para poder ser almacenado posteriormente en bd

def get_ticker_hash(ticker_data): #Función para retornar un solo gran string con todos los datos de los items
	from collections import OrderedDict #Permite ordenar una coleción bajo un criterio
	ticker_data = OrderedDict(
		sorted( #Función para ordenar cualquier tipo de conjunto de elementos con un criterio
			ticker_data.items(), #Se le pasa la lista de items a ordenar
			key = first_element #Sorted manda a llamar a la función first_element, pasándole una tupla (key, value).
			                    #Y lo que retorne, será el valor usado para ordenar
		)
	)

	ticker_value = '' #Donde se guardará el hash final a retornar
	for _, value in ticker_data.items(): #Recorrer la lista de items
		ticker_value += str(value) #Concatenar el valor del item como string

	return get_hash(ticker_value) #Encripto string creado

def check_if_exists(db_connection, ticker_data):
	ticker_hash = get_ticker_hash(ticker_data) #Creo un hash en base a los datos de la colección del ticker

	if db_connection.tickers.find_one({"ticker_hash": ticker_hash}): #Busco en bd si encuentra el ticker a través del hash generado
		return True

	return False

def save_ticker(db_connection, ticker_data=None):
	if not ticker_data: #Verifico que los datos existan
		return False

	if check_if_exists(db_connection, ticker_data): #Verifico si existe el ticker en bd
		return False

	ticker_hash = get_ticker_hash(ticker_data) #Creo un hash en base a los datos de la colección del ticker
	ticker_data['ticker_hash'] = ticker_hash #Creo nuevo dato para ser guardado en bd
	ticker_data['rank'] = int(ticker_data['rank']) #Fuerzo conversión de dato a entero
	ticker_data['last_updated'] = int(ticker_data['last_updated']) #Fuerzo conversión de dato a entero

	db_connection.tickers.insert_one(ticker_data) #Inserto datos en bd
	return True


if __name__ == '__main__':
	connection = get_db_connection('mongodb://localhost:27017/') #Conectar a la bd de manera simple, sin usuario y contraseña
	tickers = get_cryptocurrencies_from_api() #Se solicita lista de tickers desde el api externo

	for ticker in tickers: #Recorro lista de tickers recibidos
		save_ticker(connection, ticker) #Guardo cada ticker en bd, solo si no existe actualmente

	print('Tickers almacenados')
