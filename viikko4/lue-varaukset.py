"""
Ohjelma joka tulostaa tiedostosta luettujen varausten alkiot ja niiden tietotyypit

varausId | nimi | sähköposti | puhelin | varauksenPvm | varauksenKlo | varauksenKesto | hinta | varausVahvistettu | varattuTila | varausLuotu
------------------------------------------------------------------------
201 | Muumi Muumilaakso | muumi@valkoinenlaakso.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Metsätila 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
202 | Niiskuneiti Muumilaakso | niisku@muumiglam.fi | 0451122334 | 2025-12-01 | 11:30:00 | 1 | 12.00 | False | Kukkahuone | 2025-09-03 09:12:48
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
203 | Pikku Myy Myrsky | myy@pikkuraivo.net | 0415566778 | 2025-10-22 | 15:45:00 | 3 | 27.90 | True | Punainen Huone | 2025-07-29 18:05:11
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
204 | Nipsu Rahapulainen | nipsu@rahahuolet.me | 0442233445 | 2025-09-18 | 13:00:00 | 4 | 39.95 | False | Varastotila N | 2025-08-01 10:59:02
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
205 | Hemuli Kasvikerääjä | hemuli@kasvikeraily.club | 0463344556 | 2025-11-05 | 08:15:00 | 2 | 19.95 | True | Kasvitutkimuslabra | 2025-10-09 16:41:55
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
"""
from datetime import datetime

def muunna_varaustiedot(varaus: list) -> list:
    # Tähän tulee siis varaus oletustietotyypeillä (str)
    # Varauksessa on 11 saraketta -> Lista -> Alkiot 0-10
    # Muuta tietotyypit haluamallasi tavalla -> Seuraavassa esimerkki ensimmäisestä alkioista
    muutettu_varaus = []

    # Ensimmäisen alkion = varaus[0] muunnos
    muutettu_varaus.append(int(varaus[0]))
    # Ja tästä jatkuu
    muutettu_varaus.append(varaus[1])
    muutettu_varaus.append(varaus[2])
    muutettu_varaus.append(varaus[3])
    muutettu_varaus.append(datetime.strptime(varaus[4], "%Y-%m-%d").date())
    muutettu_varaus.append(datetime.strptime(varaus[5], "%H:%M").time())
    muutettu_varaus.append(int(varaus[6]))
    muutettu_varaus.append(float(varaus[7]))
    muutettu_varaus.append((varaus[8]=="True"))
    muutettu_varaus.append(varaus[9])
    muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"))

    return muutettu_varaus

def hae_varaukset(varaustiedosto: str) -> list:
    # HUOM! Tälle funktioille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut_varaukset(varaukset: list) -> list:

    vahvistetut = []
    for vahvistettu in varaukset:
        if (vahvistettu[8] is True):
            vahvistetut.append(vahvistettu)
    return vahvistetut

def pitkat_varaukset(varaukset: list) -> list:
    
    pitkät = []
    for varaus in varaukset[1:]: # ohitetaan otskikko rivin Int
        if (varaus[6] >= 3):
            pitkät.append(varaus)
    return pitkät

def vahvistus_status(varaukset: list) -> list:
    
    status_lista = []
    for varaus in varaukset[1:]:
        if varaus[8] is True:
            status = "Vahvistettu"
        else:
            status = "Ei vahvistettu"
        status_lista.append((varaus[1], status))
    return status_lista

def yhteenveto_vahvistuksista(varaukset: list) -> int:

    vahvistettu_lkm = 0
    vahvistamaton_lkm = 0
    for varaus in varaukset[1:]:
        if varaus[8] is True:
            vahvistettu_lkm += 1
        else:
            vahvistamaton_lkm += 1
    return vahvistettu_lkm, vahvistamaton_lkm

def vahvistettujen_tulo(varaukset: list) -> float:

    yhteistulo = 0.0
    for varaus in varaukset[1:]:
        if varaus[8] is True:
            yhteistulo += varaus[7] * varaus[6]
    return yhteistulo

def main():

    # Kutsutaan funkioita hae_varaukset, joka palauttaa kaikki varaukset oikeilla tietotyypeillä
    varaukset = hae_varaukset(varaustiedosto="varaukset.txt")

    print("\n1) Vahvistetut varaukset:")
    for varaus in vahvistetut_varaukset(varaukset):
       print(f"{'-'} {varaus[1]} , {varaus[9]} , {varaus[4].strftime('%d.%m.%Y')} , {"klo"} {varaus[5].strftime('%H.%M')} ")
    
    print("\n2) Pitkät varaukset (> 3 h):")
    for varaus in pitkat_varaukset(varaukset):
        print(f"{'-'} {varaus[1]} , {varaus[4].strftime('%d.%m.%Y')} , {"klo"} {varaus[5].strftime("%H.%M")} , {'kesto'} {varaus[6]} {'h'} , {varaus[9]}")
    
    print("\n3) Varausten vahvistusstatus:")
    for varaus, status in vahvistus_status(varaukset):
        print(f"{'-'} {varaus} {'->'} {status}")

    print("\n4) Yhteenveto vahvistuksista:")
    vahvistettu_lkm, vahvistamaton_lkm = yhteenveto_vahvistuksista(varaukset)
    print(f"Vahvistettuja varauksia: {vahvistettu_lkm} {'kpl'}")
    print(f"Ei-vahvistettuja varauksia: {vahvistamaton_lkm} {'kpl'}")

    print("\n5) Vahvistettujen varausten kokonaistulot:")
    yhteistulo = vahvistettujen_tulo(varaukset)
    print(f"Vahvistettujen varausten kokonaistulot: {str(f'{yhteistulo:.2f}').replace('.', ',')} €")


if __name__ == "__main__":
    main()