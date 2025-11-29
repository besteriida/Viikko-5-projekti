# Copyright (c) 2025 Iida Selonen
# License: Ei oo MITtään lisenssiä, tee mitä haluat 

"""tässä luetaan csv-tiedosto ja käsitellään päivämäärä"""

import csv
from datetime import datetime

def lue_data(filename: str) -> list:
    """lukee csv-tiedoston missä stringejä ja palauttaa listan"""
    rivit = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        # avaa tiedoston ja asettaa ton utf merkistön
        reader = csv.reader(csvfile, delimiter=';')
        # määrittää että erotinmerkki eli tietojen välissä on puolipiste
        header = next(reader)
        # ohitetaan otsikkorivi jossa kerrotaan mitä noi tiedot on

        for row in reader:
            # lukee jokaisen rivin paitsi ton ohitetun otsikkorivin
            aika = datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%S')
            # muuttaa ajan datetime muodoksi niinkuin ohjeessa
            rivit.append({
                # luodaan sanakirja jossa on avaimet ja float desimaaliarvot
                # jaettuna tuhannella koska kilowatti -> megawatti
                "aika": aika,
                "kulutus1": float(row[1]) / 1000,
                "kulutus2": float(row[2]) / 1000,
                "kulutus3": float(row[3]) / 1000,
                "tuotanto1": float(row[4]) / 1000,
                "tuotanto2": float(row[5]) / 1000,
                "tuotanto3": float(row[6]) / 1000
            })
    return rivit
    # palauttaa rivit

def laske_viikkoyhteydet(rivit: list) -> dict:
    """laittaa sanakirjaan viikonpäivät. Dict on sanakirja"""
    fi_days = ['Maanantai', 'Tiistai', 'Keskiviikko',
               'Torstai', 'Perjantai', 'Lauantai', 'Sunnuntai']
    # suomenkieliset viikonpäivät koska python puhuu englantia
    data = {day: {"kulutus": [0, 0, 0],
                  "tuotanto": [0, 0, 0],
                  "paivamaara": None} for day in fi_days}
    # kulutus ja tuotanto molemmilla on kolme arvoa listassa jotka asetetaan nolliksi

    for rivi in rivit:
        # käydään rivit läpi
        viikonpaiva = fi_days[rivi["aika"].weekday()]
        # määritetään viikonpäivä suomeksi

        if data[viikonpaiva]["paivamaara"] is None:
            # jos päivämäärä on tyhjä niin asetetaan se
            data[viikonpaiva]["paivamaara"] = rivi["aika"].date()
            # asetetaan päivämäärä ja viikonpäivä

        for i in range(3):
            # käydään kolme arvoa läpi muuttujan nimeltä i avulla ja lisätään ne kulutus ja tuotanto alle
            data[viikonpaiva]["kulutus"][i] += rivi[f"kulutus{i+1}"]
            data[viikonpaiva]["tuotanto"][i] += rivi[f"tuotanto{i+1}"]
    return data
    # palauttaa datan

def tulosta_tulokset(data: dict):
    """tulostaa tulokset data: sanakirjasta dict"""
    print("\nPäivän kulutus ja tuotanto yhteensä (MWh):")
    # otsikko

    print(f"📅 {'Päivä':<12} | {'Pvm':<10} | "
          f" {'K1':>6} |  {'K2':>6} |  {'K3':>6} | "
          f" {'T1':>6} |  {'T2':>6} |  {'T3':>6}")
    # Tulostetaan otsikot joille määritelty leveyksiä koska laitettu hymiöitä muuten menee sekaisin rivit
    print("-" * 96)

    for day, arvot in data.items():
        # käydään data läpi että saadaan arvot printattaviksi
        k = arvot["kulutus"]
        t = arvot["tuotanto"]
        p = arvot["paivamaara"]

        print(f"|💡🪫 {day:<12} | {p.strftime('%d.%m.%Y'):<10} | "
              f"{f'{k[0]:.2f}'.replace('.', ','):>8} | "
              f"{f'{k[1]:.2f}'.replace('.', ','):>8} | "
              f"{f'{k[2]:.2f}'.replace('.', ','):>8} | "
              f"{f'{t[0]:.2f}'.replace('.', ','):>8} | "
              f"{f'{t[1]:.2f}'.replace('.', ','):>8} | "
              f"{f'{t[2]:.2f}'.replace('.', ','):>8}")
        # Tulostetaan päivämäärätiedot ja rivit joissa on kulutus ja tuotanto ja taas hymiöitä ja piti vaihtaa se piste desimaaliluvuista pilkuksi

def main():
    """pääohjelma"""
    rivit = lue_data('viikko42.csv')
    # luetaan tiedosto
    data = laske_viikkoyhteydet(rivit)
    # lasketaan viikkoyhteydet
    tulosta_tulokset(data)
    # tulostetaan tulokset

if __name__ == "__main__":
    main()