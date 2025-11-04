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

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Jäsennellään varaus osiin
    varausId = varaus.split('|')[0]
    varaaja = varaus.split('|')[1]
    paivamaara = varaus.split('|')[2]
    aloitusaika = varaus.split('|')[3]
    tuntimaara = varaus.split('|')[4]
    tunthinta = varaus.split('|')[5]
    kokonaishinta = float(tunthinta) * float(tuntimaara)
    maksu = varaus.split('|')[7]
    kohde = varaus.split('|')[8]
    puhelin = varaus.split('|')[9]
    sahkoposti = varaus.split('|')[10]

    # Muutetaan piste pilkuksi eurojen esitystä varten
    mtunthinta = tunthinta.replace(".", ",")
    mkokonaishinta = str(kokonaishinta).replace(".", ",")

    # Muutetaan maksettu tieto luettavampaan muotoon
    maksettu = "Kyllä" if maksu == "True" else "Ei"

    
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


if __name__ == "__main__":
    main()