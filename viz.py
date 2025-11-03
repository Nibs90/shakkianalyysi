import os
import pandas as pd
import plotly.express as px

# Luodaan kansio kuville, jos sitä ei ole vielä olemassa
IMP = "data/games.csv"
os.makedirs("pics", exist_ok=True)

# Luetaan omat pelit Lichessistä tallennettuun csv-tiedostoon
df = pd.read_csv(IMP)

# --- 1. Yleinen tulostenjakauma (voitot / häviöt / tasapelit) ---
counts = df["result"].value_counts().reset_index()
counts.columns = ["Tulos", "Pelit"]
pic1 = px.pie(counts, names="Tulos", values="Pelit", title="Tulokset ")
pic1.write_html("pics/01_tulokset.html", auto_open=True)

# --- 2. Avauksien voittoprosentit ---
# Muutetaan tulokset myös suomeksi
df["tulos"] = (
    df["result"].astype(str)
      .str.strip().str.lower()
      .replace({
          "valkoinen voittaa": "white win",
          "musta voittaa": "black win",
          "tasapeli": "draw"
      })
)

# Otetaan 10 yleisintä avausta ja katsotaan, kuinka usein valkea voitti
top = df["opening_name"].value_counts().head(10).index
tmp = df[df["opening_name"].isin(top)].copy()

tmp["white_win"] = (tmp["tulos"] == "white win").astype(int)
winrate = tmp.groupby("opening_name")["white_win"].mean().reset_index()
winrate["white_win_%"] = (winrate["white_win"] * 100).round(1)

pic3 = px.bar(
    winrate.sort_values("white_win_%", ascending=False),
    x="opening_name", y="white_win_%",
    title="Valkoisen voitto% – top 10 avaukset",
    labels={"opening_name": "Avaus", "white_win_%": "Valkoisen voitto%"}
)
pic3.update_layout(xaxis_tickangle=-30)
pic3.show()

# --- 3. Pelityylien jakauma (esim. blitz, rapid jne.) ---
sp = df["speed"].value_counts().reset_index()
sp.columns = ["Tyyli","Pelit"]
pic3 = px.bar(sp, x="Tyyli", y="Pelit", title="Pelit pelityyleittäin")
pic3.write_html("pics/03_pelityylit.html")

print(" Valmista: pics/01_*, 02_*, 03_*")
