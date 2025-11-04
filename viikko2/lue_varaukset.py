"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"
    tuloste = "tuloste.txt"

    # Avataan tiedosto ja luetaan sisältö, lisäksi avataan tulostiedosto kirjoitusta varten
    with open(varaukset, "r", encoding="utf-8") as f, open(tuloste, "w", encoding="utf-8") as out:
        for line in f:
            varaus = line.strip()
            osat = varaus.split('|')
            if len(osat) < 10:
                continue # Ohitetaan virheelliset rivit

            # Jäsennellään varaus osiin
            varausId = osat[0]
            varaaja = osat[1]
            paivamaara = osat[2]
            aloitusaika = osat[3]
            tuntimaara = osat[4]
            tunthinta = osat[5]
            kokonaishinta = float(tunthinta) * float(tuntimaara)
            maksu = osat[6]
            kohde = osat[7]
            puhelin = osat[8]
            sahkoposti = osat[9]

             # Muutetaan piste pilkuksi eurojen esitystä varten
            mtunthinta = tunthinta.replace(".", ",")
            mkokonaishinta = f"{kokonaishinta:.2f}".replace(".", ",")

             # Muutetaan maksettu tieto luettavampaan muotoon
            maksettu = "Kyllä" if maksu == "True" else "Ei"

             # Muutetaan päivämäärän muotoon dd.mm.yyyy
            from datetime import datetime
            dt = datetime.strptime(paivamaara, "%Y-%m-%d")
            paivamaara = dt.strftime("%d.%m.%Y")

             # Tulostetaan jäsennellyt tiedot
            print("Varausnumero:", varausId)
            print("Varaaja:", varaaja)
            print("Päivämäärä:", paivamaara)
            print("Aloitusaika:", aloitusaika)
            print("Tuntimäärä:", tuntimaara)
            print("Tuntihinta:", mtunthinta, "€")
            print("Kokonaishinta:", mkokonaishinta, "€")
            print("Maksettu:", maksettu)
            print("Kohde:", kohde)
            print("Puhelin:", puhelin)
            print("Sähköposti:", sahkoposti)
            print("-" * 50)  # Tyhjä rivi varausten väliin

            # Kirjoitetaan tiedot tulostiedostoon
            out.write(f"Varausnumero: {varausId}\n")
            out.write(f"Varaaja: {varaaja}\n")
            out.write(f"Päivämäärä: {paivamaara}\n")
            out.write(f"Aloitusaika: {aloitusaika}\n")
            out.write(f"Tuntimäärä: {tuntimaara}\n")
            out.write(f"Tuntihinta: {mtunthinta} €\n")
            out.write(f"Kokonaishinta: {mkokonaishinta} €\n")
            out.write(f"Maksettu: {maksettu}\n")
            out.write(f"Kohde: {kohde}\n")
            out.write(f"Puhelin: {puhelin}\n")
            out.write(f"Sähköposti: {sahkoposti}\n")
            out.write("-" * 50 + "\n")



if __name__ == "__main__":
    main()