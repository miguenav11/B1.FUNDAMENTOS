import os, psycopg, requests
url = os.getenv("DATABASE_URL")
connection = psycopg.connect(url)
cur = connection.cursor()
print("BD conectada con éxito")


# CREO LA TABLA

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
        created         TIMESTAMPTZ
        );"""
        cur.execute(query)
        connection.commit()
        print("Create Table Characters executed")
    except Exception as e:
        print("Error creating table Characters: ", e)

createTableCharacters()


# ACCEDO A LA API

characters_list = []    # creo la lista vacía

base_url = "https://rickandmortyapi.com/api/character"
response = requests.get(base_url)
data = response.json()
try:
    num_pages = int(os.getenv("RM_PAGES", "1"))
except:
    num_pages = 1
    print("Error finding 'RM_PAGES'. So downloading only 1 page")

for page_number in range(0, num_pages):
    url_actual = f"{base_url}?page={page_number}"
    print("Obteniendo datos de:", url_actual)
    try:
        response = requests.get(url_actual)
        response.raise_for_status() # lanza error si la petición falla
        data = response.json()



print(len(data), "elementos dentro de data")    # 2: info y results
print(len(data["results"]), "personajes en total")  # 20
print(len(data["results"][0]), "apartados por personaje")   # 12
print("Nombre del primer personaje:", data["results"][0]["name"])


# INSERTO LOS PERSONAJES (filas) EN LA TABLA
def createCharacters(values):
    try:
        query = """
        INSERT INTO characters(id, name, status, species, type, gender, origin_name, location_name, image, url, created)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;"""
        cur.executemany(query, values)
    except Exception as e:
        print("Error creating character: ", e)



ch = 0
while ch < len(data["results"]):
    tuple_char = (data["results"][ch]["id"], data["results"][ch]["name"], data["results"][ch]["status"], data["results"][ch]["species"], data["results"][ch]["type"], data["results"][ch]["gender"], data["results"][ch]["origin"]["name"], data["results"][ch]["location"]["name"], data["results"][ch]["image"], data["results"][ch]["url"], data["results"][ch]["created"])
    characters_list.append(tuple_char)
    ch += 1
# print(characters_list)

try:
    createCharacters(characters_list)
    connection.commit()
    print("Characters successfully inserted.")
except Exception as e:
    print("Error creating characters:", e)
    connection.rollback()


# ACCEDO A LOS DATOS DE LA TABLA (SELECT) con fetchal()

cur.execute("SELECT id, name, species FROM characters;")
print(cur.fetchall())


# GUARDO Commit
connection.commit()
# CIERRO el cursor y la conexión
cur.close()
connection.close()