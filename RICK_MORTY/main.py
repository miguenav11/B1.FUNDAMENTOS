import os, psycopg, requests
url = os.getenv("DATABASE_URL")
connection = psycopg.connect(url)
cur = connection.cursor()
print("BD conectada con éxito")

# Voy por el punto 3

# DEFINO función
def createTableCharacters():
    try:
        query = """
        CREATE TABLE IF NOT EXISTS characters(
        id              INTEGER PRIMARY KEY,
        name            VARCHAR,
        status          VARCHAR,
        species         VARCHAR,
        type            VARCHAR,
        gender          VARCHAR,
        origin_name     VARCHAR,
        location_name   VARCHAR,
        image           TEXT,
        url             TEXT,
        created         TIMESTAMPZ
        );"""
        cur.execute(query)
        connection.commit()
    except Exception as e:
        print("Error creating table Characters: ", e)
"""
def createCharacter():
    try:
        query = ""
        INSERT INTO characters(name, status, species, type, gender, origin_name, location_name, image, url, created)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""
        cur.execute(query)
    except Exception as e:
        print("Error creating character: ", e)
"""

url = "https://rickandmortyapi.com/api/character"
response = requests.get(url)
data = response.json()

# EJECUTO función
# createTableCharacters()
# print(data)
# print(len(data) == 2)                 data contiene info y results
info_characters = data["results"]     # hay 20 personajes
# print(len(data["results"][0]) == 12)# cada personaje tiene 12 apartados
print(data["results"][0]["id"])
      
# GUARDO Commit
#   connection.commit()
# CIERRO conexión al final
#   cur.close()
#   connection.close()