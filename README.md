# Viikko-5-projekti
Tehtävänäsi on laatia Python-ohjelma, joka:

Lukee tiedot tiedostosta viikko42.csv // import on tehty

Laskee jokaiselle viikonpäivälle (ma–su): // array? pitää muuttaa suomalaisiksi

vaiheittaisen sähkönkulutuksen (vaihe 1–3) kWh-yksikössä // jaan tuhannella -> mwh
vaiheittaisen sähköntuotannon (vaihe 1–3) kWh-yksikössä
Tulostaa tulokset konsoliin selkeänä, käyttäjäystävällisenä taulukkona.

Tiedosto sisältää viikon 42 (ma–su) tuntikohtaiset mittaukset: jos olisi enemmän viikkoja ja haluaisi tietyn viikon tiedot niin voisi tehdä näin tms:

import csv
from datetime import datetime

weeks = set()

with open("viikko42.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)

    for row in reader:
        aika = datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S")
        week_number = aika.isocalendar()[1]   # ISO-viikon numero
        weeks.add(week_number)

print("Viikkojen numerot datassa:", weeks)
print("Viikkojen määrä:", len(weeks))



aika (päivämäärä ja kellonaika)
kulutus kolmeen vaiheeseen jaettuna (Wh) [0, 0, 0]
tuotanto kolmeen vaiheeseen jaettuna (Wh) [0, 0, 0]

testipätkä vaan jos myöhemmin luet tätä ja mietit että wtf 
:
        print(f"Rivi {i}: Viikonpaiva {viikonpaiva} Aika: {aika}, Kulutus: {kulutus1}, {kulutus2}, {kulutus3}, Tuotanto: {tuotanto1}, {tuotanto2}, {tuotanto3}")
        if i == 2:
            break



                viikonpaiva = fi_days[aika.weekday()]
    kulutus1 = float(row[1]) /1000
    kulutus2 = float(row[2]) /1000
    kulutus3 = float(row[3]) /1000
    tuotanto1 = float(row[4]) /1000
    tuotanto2 = float(row[5]) /1000
    tuotanto3 = float(row[6]) /1000



    data[viikonpaiva]["kulutus"][0] += kulutus1
    data[viikonpaiva]["kulutus"][1] += kulutus2
    data[viikonpaiva]["kulutus"][2] += kulutus3
    data[viikonpaiva]["tuotanto"][0] += tuotanto1
    data[viikonpaiva]["tuotanto"][1] += tuotanto2
    data[viikonpaiva]["tuotanto"][2] += tuotanto3


    import csv
from datetime import datetime

def lue_data(filename: str) -> list:
    rivit = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        header = next(reader)

        for row in reader:
            aika = datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%S')
            rivit.append([
                aika,
                float(row[1]) / 1000,
                float(row[2]) / 1000,
                float(row[3]) / 1000,
                float(row[4]) / 1000,
                float(row[5]) / 1000,
                float(row[6]) / 1000
            ])
    return rivit

def laske_viikkoyhteydet(rivit: list) -> list:
    fi_days = ['Maanantai', 'Tiistai', 'Keskiviikko', 'Torstai', 'Perjantai', 'Lauantai', 'Sunnuntai']
    data = [[day, 0, 0, 0, 0, 0, 0] for day in fi_days]

    for rivi in rivit:
        viikonpaiva = rivi[0].weekday()
        data[viikonpaiva][1] += rivi[1]
        data[viikonpaiva][2] += rivi[2]
        data[viikonpaiva][3] += rivi[3]
        data[viikonpaiva][4] += rivi[4]
        data[viikonpaiva][5] += rivi[5]
        data[viikonpaiva][6] += rivi[6]
    return data

def tulosta_tulokset(data: list):
    print("\nPäivän kulutus ja tuotanto yhteensä (MWh):")
    print(f"{'Päivä':<12} | {'K1':>10} | {'K2':>10} | {'K3':>10} | {'T1':>10} | {'T2':>10} | {'T3':>10}")

    for rivi in data:
        print(f"{rivi[0]:<12} | "
              f"{f'{rivi[1]:.2f}'.replace('.', ','):>10} | "
              f"{f'{rivi[2]:.2f}'.replace('.', ','):>10} | "
              f"{f'{rivi[3]:.2f}'.replace('.', ','):>10} | "
              f"{f'{rivi[4]:.2f}'.replace('.', ','):>10} | "
              f"{f'{rivi[5]:.2f}'.replace('.', ','):>10} | "
              f"{f'{rivi[6]:.2f}'.replace('.', ','):>10}")

def main():
    rivit = lue_data('viikko42.csv')
    data = laske_viikkoyhteydet(rivit)
    tulosta_tulokset(data)

if __name__ == "__main__":
    main()