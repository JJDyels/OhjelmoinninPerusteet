# Copyright (c) 2025 Jaakko Kivioja
# License: MIT

"""Ohjelma joka kysyy käyttäjältä millaisen kulutus-/tuotantoraportin hän haluaa ja luo sen tiedostoon"""

"""Ladataan tarvittavat kirjastot"""
from datetime import datetime, date
import locale
from tabulate import tabulate

# Asetaan paikalliseksi ajaksi suomi
locale.setlocale(locale.LC_TIME, "fi_FI.UTF-8")

def muunna_tiedot(tieto: list) -> list:
    """Muuntaa tiedot oikeaan muotoon ja tietotyyppeihin"""
    muutettu_tieto = []
    
    paivamaara = datetime.fromisoformat(tieto[0])
    muutettu_tieto.append(paivamaara.date())

    for i in range(1, 4):
        muutettu_tieto.append(float(tieto[i].replace(",", ".")))
    return muutettu_tieto

def hae_tiedot(tiedostonimi: str) -> list:
    """Hakee päivämäärän sekä kulutus- ja tuotantotiedot tiedostosta ja palauttaa ne listana"""

    kulutus_tuotanto_tiedot = []

    with open(tiedostonimi, "r", encoding="utf-8") as f:
        next(f)
        for rivi in f:
            rivi = rivi.strip()
            rivi = rivi.split(';')
            kulutus_tuotanto_tiedot.append(muunna_tiedot(rivi))
        return kulutus_tuotanto_tiedot

def aikavalin_yhteenveto(tiedot: list, alku: date, loppu: date) -> list:
    """Laskee kulutuksen ja tuotannon annetulla aikavälillä ja palauttaa ne listana"""

    kulutus = []
    tuotto = []
    lampotila = []

    for lukema in tiedot:
        if alku <= lukema[0] <= loppu:
            kulutus.append(lukema[1])
            tuotto.append(lukema[2])
            lampotila.append(lukema[3])
    return [
        f"{sum(kulutus):.2f}".replace(".", ","),
        f"{sum(tuotto):.2f}".replace(".", ","),
        f"{(sum(lampotila) / len(lampotila)):.2f}".replace(".", ",")
    ]
    
def kulutus_ja_tuotto_kk(tiedot: list, paiva: date) -> list:
    """Laskee kulutuksen ja tuotannon kuukaudessa ja palauttaa ne listana"""

    kulutus = []
    tuotto = []
    lampotila = []

    for lukema in tiedot:
        if lukema[0].month == paiva.month and lukema[0].year == paiva.year:
            kulutus.append(lukema[1])
            tuotto.append(lukema[2])
            lampotila.append(lukema[3])
    return [
        f"{sum(kulutus):.2f}".replace(".", ","),
        f"{sum(tuotto):.2f}".replace(".", ","),
        f"{(sum(lampotila) / len(lampotila)):.2f}".replace(".", ",")
    ]

def vuoden_yhteenveto(tiedot: list, vuosi: int) -> list:
    """Laskee kulutuksen ja tuoton vuoden yhteenvedon ja palauttaa sen listana"""

    kulutus = []
    tuotto = []
    lampotila = []

    for lukema in tiedot:
        if lukema[0].year == vuosi:
            kulutus.append(lukema[1])
            tuotto.append(lukema[2])
            lampotila.append(lukema[3])
    return [
        f"{sum(kulutus):.2f}".replace(".", ","),
        f"{sum(tuotto):.2f}".replace(".", ","),
        f"{(sum(lampotila) / len(lampotila)):.2f}".replace(".", ",")
    ]

def raportin_luonti(paavalikko: bool, alavalikko: bool) -> list:
    """ Kysyy käyttäjältä millainen raportti luodaan ja nitä tehdään raportin luonnin jälkeen"""

    while paavalikko:
        print("-"*40)
        print("Valitse raportin tyyppi:")
        print("1. Yhteenveto tietyllä aikavälillä")
        print("2. Kuukausikohtainen yhteenveto")
        print("3. Vuoden yhteenveto")
        print("4. Lopeta ohjelma")
        print("-"*40)

        valinta = input("\nValitse (1-4): ")

        try:
            valinta = int(valinta)
            if not (1 <= valinta <= 4):
                raise ValueError
            
        except ValueError: 
                print("\nVirheellinen valinta. Anna numero väliltä 1-4.\n")
                continue

        if valinta == 1:
            try:
                alku_pvm = input("\nAnna alku päivämäärä (PP.KK.YYYY): ")
                loppu_pvm = input("\nAnna loppu päivämäärä (PP.KK.YYYY): ")
                alku = datetime.strptime(alku_pvm, "%d.%m.%Y").date()
                loppu = datetime.strptime(loppu_pvm, "%d.%m.%Y").date()
                return valinta, alku, loppu
            except ValueError:
                print("\nVirheellinen päivämäärä. Käytä muotoa PP.KK.YYYY.\n")
                continue

        elif valinta == 2:
            try:
                kuukausi = int(input("\nAnna kuukausi (1-12): "))
                if not (1 <= kuukausi <= 12):
                    raise ValueError
                vuosi = datetime.now().year
                return valinta, date(vuosi, kuukausi, 1)
            except ValueError:
                print("\nVirheellinen kuukausi. Anna numero väliltä 1-12.\n")
                continue

        elif valinta == 3:
            vuosi = 2025
            return valinta, vuosi

        elif valinta == 4:
            print("\nOhjelma lopetetaan.\n")
            return 4, None
    
    while True and alavalikko:
        print("-"*40)
        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta ohjelma")
        print("-"*40)

        try:
            ala_valinta = input("\nValitse (1-3): ")
            ala_valinta = int(ala_valinta)
            if not (1 <= ala_valinta <= 3):
                raise ValueError
            
        except ValueError: 
                print("\nVirheellinen valinta. Anna numero väliltä 1-3.\n")
                continue

        if ala_valinta == 1:
            return 1, None
                
        elif ala_valinta == 2:
            return 2, None
            
        elif ala_valinta == 3:
            print("\nOhjelma lopetetaan.\n")
            return 3, None




def main():
    """Pääohjelma, joka suorittaa raportin tekemisen ja tallentaa sen tiedostoon"""

    raportintiedot = hae_tiedot("2025.csv")

    while True:
        valinta, *parametrit = raportin_luonti(True, False)

        if valinta == 1:
            alku, loppu = parametrit
            raportti = aikavalin_yhteenveto(raportintiedot, alku, loppu)
            otsikko = f"Raportti ajalta {alku.strftime('%d.%m.%Y')} - {loppu.strftime('%d.%m.%Y')}"

        elif valinta == 2:
            paiva = parametrit[0]
            raportti = kulutus_ja_tuotto_kk(raportintiedot, paiva)
            otsikko = f"Kuukausikohtainen raportti: {paiva.strftime('%B %Y')}"

        elif valinta == 3:
            vuosi = parametrit[0]
            raportti = vuoden_yhteenveto(raportintiedot, vuosi)
            otsikko = f"Vuoden {vuosi} raportti"

        elif valinta == 4:
            break

        # Tulosta raportti
        print("\n" + otsikko)
        print("=" * len(otsikko))
        taulukko = [["Kulutus (kWh)", "Tuotanto (kWh)", "Keskilämpötila (°C)"], raportti]
        print(tabulate(taulukko, headers="firstrow", tablefmt="fancy_grid"))
        print()

        # Alavalikon käsittely
        ala_valinta, _ = raportin_luonti(False, True)
        
        if ala_valinta == 1:
            with open("raportti.txt", "w", encoding="utf-8") as f:
                f.write(otsikko + "\n")
                f.write("=" * len(otsikko) + "\n")
                f.write(tabulate(taulukko, headers="firstrow", tablefmt="fancy_grid"))
            print("Raportti kirjoitettu tiedostoon raportti.txt\n")
            
        elif ala_valinta == 2:
            continue
            
        elif ala_valinta == 3:
            break


if __name__ == "__main__":
    main()