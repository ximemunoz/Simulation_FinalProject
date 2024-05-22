import requests
import json

#--------------------------------------------#

#Credenciales de uso del API
CLIENT_ID = '' #INSERT CLIENT ID
SECRET_ID = '' #INSERT SECRET ID
TOKEN = ''     #INSERT TOKEN TO ACCESS THE API

#--------------------------------------------#

#Funcion para obtener el token de acceso al API
def getToken():
    auth_url = 'https://accounts.spotify.com/api/token'
    data = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': SECRET_ID,
    }
    auth_response = requests.post(auth_url, data=data)
    access_token = auth_response.json().get('access_token')
    print(access_token)
    
#--------------------------------------------#

#Funcion de lectura de archivos
def readFile(nombre_archivo):
    lineas = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            if(linea[0] != "#"):
                # Eliminar el salto de línea al final de cada línea y agregarla a la lista
                lineas.append(linea.strip())
    return lineas

#--------------------------------------------#

#Funcion de acceso a la información de los artistas desde el API
def getArtistInfo(artist_name):
    # Endpoint de búsqueda de artistas
    endpoint = "https://api.spotify.com/v1/search"
    
    # Parámetros de búsqueda
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }

    # Authorization token que debe haber sido creado previamente
    token = TOKEN
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # Realizar la solicitud a la API de Spotify
    response = requests.get(endpoint, params=params, headers=headers)
    data = response.json()
    
    NAME       = ''
    ID         = ''
    FOLLOWERS  = ''
    GENRES     = ''
    POPULARITY = ''
    LEVEL      =  0
    URL        = ''
    IMAGE      = ''
        
    if data.get('artists') and data['artists'].get('items'):
        
        NAME       = data['artists']['items'][0]['name']
        ID         = data['artists']['items'][0]['id']
        FOLLOWERS  = data['artists']['items'][0]['followers']['total']
        GENRES     = data['artists']['items'][0]['genres']
        POPULARITY = data['artists']['items'][0]['popularity']
        URL        = data['artists']['items'][0]['external_urls']['spotify']
        IMAGE      = data['artists']['items'][0]['images'][0]['url']
        
        if(FOLLOWERS >= 10000000): LEVEL = 1
        elif(FOLLOWERS >= 1000000): LEVEL = 2
        elif(FOLLOWERS >= 100000): LEVEL = 3
        else: LEVEL = 4
        
        info = {'Name': NAME, 'Id': ID, 'Followers': FOLLOWERS, 'Genres': GENRES, 'Popularity': POPULARITY, 'Level': LEVEL, 'Growth': 0, 'Url': URL, 'Image': IMAGE }
        
        return info
    else:
        info = {'Name': None, 'Id': None, 'Followers': None, 'Genres': None, 'Popularity': None, 'Level': LEVEL, 'Growth': None, 'Url': None, 'Image': None }
        return None


#--------------------------------------------#

#Funcion para crear un festival
def createFestival(festival, asist, ticketPrice, income):
    info = {'Festival': festival, 'Asistants': asist, 'Ticketprice': ticketPrice, 'Income': income, 'Bands': []}
    dataArtists = []
    fileName = "festivales/" + festival + ".txt"  # Reemplaza "archivo.txt" con la ruta de tu archivo
    artists = readFile(fileName)
    for artist in artists:
        dataArtists.append(getArtistInfo(artist))
    info['Bands'] = dataArtists
    return info

#--------------------------------------------#

def start():
    #Seteo de los festivales
    fests = ["CC2021", "CC2022", "CC2023", ]
    ticket = [2699, 4600, 6047, ]
    income = [328.2, 1173,1451.3]
    asist = [121600, 255000, 240000]
    
    festivalesOut = []

    for i in range(0, len(fests)):
        festivalesOut.append(createFestival(fests[i], asist[i], ticket[i], income[i]))
        
    print(festivalesOut)

    json_object = json.dumps(festivalesOut)

    # Writing to sample.json
    with open("DataApi.json", "w") as outfile:
        outfile.write(json_object)
#--------------------------------------------#

#Only use this line when the code doesnt work and change TOKEN variable
#getToken()

start()