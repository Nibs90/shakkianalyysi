import json
import os
import pandas as pd

# Määritetään tiedostopolut
IMP = "data/games.ndjson"
OUT = "data/games.csv"

rows = []

# Luetaan tiedosto rivi riviltä
with open(IMP, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        g = json.loads(line)
        opening = (g.get("opening") or {})
        players = g.get("players") or {}
        white = players.get("white") or {}
        black = players.get("black") or {}
        winner = g.get("winner")

        rows.append({
            "id": g.get("id"),
            "speed": g.get("speed"),
            "rated": g.get("rated"),
            "createdAt": g.get("createdAt"),
            "opening_name": opening.get("name"),
            "opening_eco": opening.get("eco"),
            "opening_ply": opening.get("ply"),
            "white_name": (white.get("user") or {}).get("name"),
            "black_name": (black.get("user") or {}).get("name"),
            "white_rating": white.get("rating"),
            "black_rating": black.get("rating"),
            "winner": winner,  # None = draw
        })

df = pd.DataFrame(rows)

# Luodaan suomenkielinen tulossarake
def outcome(w):
    if w == "white": return "Valkoinen voittaa"
    if w == "black": return "Musta voittaa"
    return "Tasapeli"
df["result"] = df["winner"].apply(outcome)

# Tallennetaan CSV-muodossa (ja varmistetaan, että kansio on olemassa)
os.makedirs("data", exist_ok=True)
df.to_csv(OUT, index=False)
print(f"tallennettu {OUT} rivit: {len(df)}")