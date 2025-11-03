# ♟️ Shakkidata – Oma Lichess-analyysi

Pienimuotoinen Python-projekti, jossa hain omat Lichess-shakkipelini tilastot, muokkasin datan CSV-muotoon ja visualisoin sen Plotlyllä.  
Tavoitteena oli harjoitella datan hakua API:sta, sen esikäsittelyä Pandasilla ja graafikoiden tekemistä.

---

## 🔧 Käytetyt työkalut
- **Python 3.10+**  
- **Pandas** – datan käsittelyyn  
- **Plotly Express** – visualisointeihin  
- **Requests** – pelidatan hakuun Lichess API:sta  

---

## 📂 Projektin rakenne

```
├─ data/
│  ├─ games.ndjson      # raakadata
│  └─ games.csv         # siistitty versio analyysia varten
├─ pics/                # tuloksena syntyvät kuvaajat
├─ fetch_games.py       # hakee pelitiedot Lichessistä
├─ prep.py              # muuntaa datan CSV-muotoon
└─ viz.py               # tekee 3 kuvaa Plotlyllä
```

---

## ▶️ Käyttöohje

1. Asenna tarvittavat kirjastot:
   ```bash
   pip install pandas plotly requests
   ```

2. Hae pelit omalla Lichess-käyttäjälläsi (määritellään fetch_games tiedostossa):
   ```bash
   python fetch_games.py
   ```

3. Muunna raakadata CSV-muotoon:
   ```bash
   python prep.py
   ```

4. Luo kuvaajat:
   ```bash
   python viz.py
   ```

5. Valmiit graafit löytyvät kansiosta `pics`.

---

## 📊 Tulokset
Skriptit tuottavat kolme eri kuvaa:
1. **Tulokset** – Tilastoidaan kuinka moni peli päättyi voittoon, tappioon tai tasapeliin  
2. **Avaukset** – Tilastoidaan valkean voittoprosentti kymmenessä yleisimmässä pelaajan avauksessa  
3. **Pelityylit** – pelien määrä pelityypin mukaan (blitz, rapid, jne.)

---

## 💡 Miksi tein tämän
Halusin tehdä pienen projektin, joka yhdistää ohjelmointia, data-analyysiä ja oman harrastukseni shakin.  