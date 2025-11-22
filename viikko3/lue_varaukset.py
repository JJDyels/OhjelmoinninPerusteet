"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funkitoita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,90 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime

def hae_varausnumero(varaus: list[str]) -> int:
    varausnumero = int(varaus[0])
    return varausnumero

def hae_varaaja(varaus: list[str]) -> str:
    nimi = varaus[1]
    return nimi

def hae_paiva(varaus: list[str]) -> str:
    paiva = datetime.strptime(varaus[2], "%Y-%m-%d").strftime("%d.%m.%Y")
    return paiva

def hae_aloitusaika(varaus: list[str]) -> str:
    aloitusaika = datetime.strptime(varaus[3], "%H:%M").strftime("%H.%M")
    return aloitusaika

def hae_tuntimaara(varaus: list[str]) -> int:
    tuntimaara = int(varaus[4])
    return tuntimaara

def hae_tuntihinta(varaus: list[str]) -> float:
    tuntihinta = float(varaus[5])
    return tuntihinta

def laske_kokonaishinta(varaus: list[str]) -> float:
    kokonaishinta = hae_tuntimaara(varaus) * hae_tuntihinta(varaus)
    return kokonaishinta

def hae_maksettu(varaus: list[str]) -> str:
    maksettu = varaus[6]
    maksu = "Kyllä" if maksettu == "True" else "Ei"
    return maksu

def hae_kohde(varaus: list[str]) -> str:
    kohde = varaus[7]
    return kohde

def hae_puhelin(varaus: list[str]) -> str:
    puhelin = varaus [8]
    return puhelin

def hae_sahkoposti(varaus: list[str]) -> str:
    sahkoposti = varaus[9]
    return sahkoposti


def tulosta_varaus(varaus):
    print(f"Varausnumero: {hae_varausnumero(varaus)}")
    print(f"Varaaja: {hae_varaaja(varaus)}")
    print(f"Päivämäärä: {hae_paiva(varaus)}")
    print(f"Aloitusaika: {hae_aloitusaika(varaus)}")
    print(f"Tuntumäärä: {hae_tuntimaara(varaus)}")
    print("Tuntihinta:", f"{hae_tuntihinta(varaus):.2f}".replace(".", ","), "€")
    print("Kokonaishinta:", f"{laske_kokonaishinta(varaus):.2f}".replace(".",","), "€")
    print(f"Maksettu: {hae_maksettu(varaus)}")
    print(f"Kohde: {hae_kohde(varaus)}")
    print(f"Puhelin: {hae_puhelin(varaus)}")
    print(f"Sähköposti: {hae_sahkoposti(varaus)}")
    

def main():
    # Maaritellaan tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto, luetaan ja splitataan sisalto
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        varaus = varaus.split('|')

    hae_varausnumero(varaus)
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)
    tulosta_varaus(varaus)

if __name__ == "__main__":
    main()

# Tarkista datatyyppi bash terminaalissa komennolla: python -m mypy lue_varaukset.py
# Tarkista että mypy asennettuna: pip install mypy
