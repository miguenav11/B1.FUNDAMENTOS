import os, psycopg, requests
url = os.getenv("DATABASE_URL")
connection = psycopg.connect(url)
cur = connection.cursor()
print("BD conectada con éxito")

# Voy por el punto 3


# --- NO MÁS CREATE TABLES O INSERTS AQUÍ ---
# --- eso en init.sql ---

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
        created         TIMESTAMP
        );"""
        cur.execute(query)
        connection.commit()
    except Exception as e:
        print("Error creating table Characters: ", e)


url = "https://rickandmortyapi.com/api/character"
response = requests.get(url)
data = response.json()

# EJECUTO función
createTableCharacters()
print(data)

# GUARDO Commit
connection.commit()
# CIERRO conexión al final
cur.close()
connection.close()