import requests
import os

#Haetaan halutun pelaajan tiedot pelitunnarilla, sekä montako peliä tarkastellaan
pelaaja = "Nibs90"
pelit = 50
out = "data/games.ndjson"

os.makedirs("data", exist_ok=True)
url = f"https://lichess.org/api/games/user/{pelaaja}"

# Rajapinnan parametrit – mitä tietoja halutaan mukaan
params = {
    "max": pelit,                 # haetaan tietty määrä pelejä
    "perfType": "blitz,rapid",    # halutut pelityypit kuten blitz ja rapid
    "opening": "true",            # avaukset
    "analysed": "false",          # analysoidut pelit
    "clocks": "false",            # pelikellon tiedot
    "moves": "false",             # siirtolistat
    "evals": "false",             # tekoälyarvioit
    "format": "ndjson",           # tallennusmuoto, kuten json
}

# Otsikkotieto (kertoo että haluamme ndjson-dataa)
headers = {"Accept": "application/x-ndjson"}
r = requests.get(url, params=params, headers=headers, timeout=60)
r.raise_for_status()
with open(out, "wb") as c:
    c.write(r.content)

print(f"tallennettu {out} ({len(r.content)//1024} KB)")