# Copyright (c) 2025 Jaakko Kivioja
# License: MIT

""" Ohjelma joka luo raportin energiankulutuksesta ja -tuotannosta"""

"""Ladataan tarvittavat kirjastot"""
from datetime import datetime, date
import locale
from tabulate import tabulate

# Asetaan paikallinen aikamuodoksi suomi
locale.setlocale(locale.LC_TIME, "fi_FI.UTF-8")


def muunna_tiedot(tieto: list) -> list:
    """Muuntaa tiedot oikeaan muotoon ja tietotyyppeihin"""
    muutettu_tieto = []
    
    paivamaara = datetime.strptime(tieto[0], "%Y-%m-%dT%H:%M:%S")
    muutettu_tieto.append(paivamaara.date())

    for i in range(1, 7):
        muutettu_tieto.append(int(tieto[i]) / 1000)
    return muutettu_tieto

def kulutus_ja_tuotto(tiedot: list, paiva: date) -> list:
    """Laskee kulutus- ja tuotantovaiheiden v1, v2 ja v3 summan per päivä ja palauttaa ne listana"""

    kulutus = [0, 0, 0]
    tuotto = [0, 0, 0]

    for lukema in tiedot:
        if lukema[0] == paiva:
            kulutus[0] += lukema[1]
            kulutus[1] += lukema[2]
            kulutus[2] += lukema[3]
            tuotto[0] += lukema[4]
            tuotto[1] += lukema[5]
            tuotto[2] += lukema[6]

    return [
        f"{kulutus[0]:.2f}".replace(".", ","),
        f"{kulutus[1]:.2f}".replace(".", ","),
        f"{kulutus[2]:.2f}".replace(".", ","),
        f"{tuotto[0]:.2f}".replace(".", ","),
        f"{tuotto[1]:.2f}".replace(".", ","),
        f"{tuotto[2]:.2f}".replace(".", ",")
    ]


def hae_tiedot(tiedostonimi: str) -> list:
    """Hakee pvm, kulutus- ja tuotantotiedot tiedostosta ja palauttaa ne listana"""

    kulutus_tuotanto_tiedot = []

    with open(tiedostonimi, "r", encoding="utf-8") as f:
        next(f)
        for rivi in f:
            rivi = rivi.strip()
            rivi = rivi.split(';')
            muutetut_tiedot = muunna_tiedot(rivi)
            kulutus_tuotanto_tiedot.append((muutetut_tiedot))
        return kulutus_tuotanto_tiedot
    

def main():
    """Pääohjelma, joka suorittaa raportin tulostuksen taulukkomuodossa"""

    tiedot = hae_tiedot("viikko42.csv")
    taulukko = []
    otsikot = ["Päivämäärä", "Kulutus V1 (kWh)", "Kulutus V2 (kWh)", "Kulutus V3 (kWh)", "Tuotto V4 (kWh)", "Tuotto V5 (kWh)", "Tuotto V6 (kWh)"]
    
    paivat = sorted(set(pvm[0] for pvm in tiedot))
    for paiva in paivat:
        yhteenveto = kulutus_ja_tuotto(tiedot, paiva)
        paiva_str = paiva.strftime("%A %d.%m.%Y")
        taulukko.append([paiva_str] + (yhteenveto))
    
    print(tabulate(taulukko, headers=otsikot, tablefmt="fancy_grid", stralign="center"))
    print("\nRaportti valmis.")
      
if __name__ == "__main__":
    main()