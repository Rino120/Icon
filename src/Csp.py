<<<<<<< HEAD

from constraint import *
import RicercaGrafo
import Utils


def check_giorno(giorno):
    if 0 < int(giorno) < 8:

        return True
    else:

        return False


def check_record(list):
    print(
        "\nInserisca il giorno come intero: \n1:Lunedì\n2:Martedì"
        "\n3:Mercoledì\n4:Giovedì\n5:Venerdì\n6:Sabato\n7:Domenica\n")
    day = input("\nInserisca il giorno: ")
    if check_giorno(day) is False:
        print("Inserimento Non Valido")
        exit(0)
    print("\nSiamo aperti dalle 8.00 alle 23.59")
    print("\nRicordiamo che gli spettacoli iniziano allo scattare di ogni ora")
    print("\nInserisca l'orario in cui vorrebbe trovare l'opera in questo formato: [HH].[MM]")
    print("\n")
    time = input("Orario preferibile: \n")
    hour = format_time(time)
    name = ''
    if day == '1':
        name = input("Opere in scena il lunedì: \n \n[]\n\n")
    elif day == '2':
        name = input("Opere in scena il martedì: \n \n[]\n\n")
    elif day == '3':
        name = input("Opere in scena il mercoledì: \n \n[]\n\n")
    elif day == '4':
        name = input("Opere in scena il giovedì: \n \n[]\n\n")
    elif day == '5':
        name = input("Opere in scena il venerdì: \n \n[]\n\n")
    elif day == '6':
        name = input("Opere in scena il sabato: \n \n[]\n\n")
    elif day == '7':
        name = input("Opere in scena la domenica: \n \n[]\n\n")
    id = name_to_id(name)

    day += ','
    hour += ','
    id += '}'

    for element in list:

        strings = str(element)
        strings = strings.split(' ')

        if (day == strings[1]) and (hour == strings[3]) and (id == strings[5]):
            return True

    return False


def name_to_id(name):
    if name == 'Sogno di una notte di mezza estate':
        return '1'
    elif name == 'Il mercante di Venezia':
        return '2'
    elif name == 'Romeo e Giulietta':
        return '3'
    elif name == 'La dodicesima notte':
        return '4'
    elif name == 'Otello':
        return '5'
    elif name == 'La bisbetica domata':
        return '6'
    elif name == 'Macbeth':
        return '7'
    elif name == 'Amleto':
        return '8'
    elif name == 'Le allegre comari di Windsor':
        return '9'
    elif name == 'La tempesta':
        return '10'
    elif name == 'Il misantropo':
        return '11'
    elif name == 'Cyrano de Bergerac':
        return '12'
    elif name == 'Edipo re':
        return '13'
    elif name == 'Antigone':
        return '14'
    elif name == 'Medea':
        return '15'
    elif name == 'Le Troiane':
        return '16'
    elif name == 'Prometeo incatenato':
        return '17'
    elif name == 'Elettra':
        return '18'
    elif name == 'La notte dei re':
        return '19'
    elif name == 'Il Tartufo':
        return '20'
    elif name == 'Il malato immaginario':
        return '21'
    elif name == 'Don Giovanni':
        return '22'
    elif name == 'Le nozze di Figaro':
        return '23'
    elif name == 'Cosi fan tutte':
        return '24'
    elif name == 'Il flauto magico':
        return '25'
    elif name == 'La Traviata':
        return '26'
    elif name == 'La Bohème':
        return '27'
    elif name == 'Madama Butterfly':
        return '28'
    elif name == 'Rigoletto':
        return '29'
    elif name == 'Il barbiere di Siviglia':
        return '30'
    elif name == 'La Cenerentola':
        return '31'
    elif name == 'La gazza ladra':
        return '32'
    elif name == 'Il Corsaro Nero':
        return '33'
    elif name == 'I promessi sposi':
        return '34'
    elif name == 'Il gabbiano':
        return '35'
    elif name == 'Tre sorelle':
        return '36'
    elif name == 'Il giardino dei ciliegi':
        return '37'
    elif name == 'Platonov':
        return '38'
    elif name == 'Anna Karenina':
        return '39'
    elif name == 'Il gioco delle parti':
        return '40'
    elif name == 'Il servitore di due padroni':
        return '41'
    elif name == 'Il malpensante':
        return '42'
    elif name == 'La cena delle beffe':
        return '43'
    elif name == 'Il cavaliere della rosa':
        return '44'
    elif name == 'Il Pipistrello':
        return '45'
    elif name == 'Il lago dei cigni':
        return '46'
    elif name == 'La bella addormentata':
        return '47'
    elif name == 'Lo schiaccianoci':
        return '48'
    elif name == 'Giselle':
        return '49'
    elif name == 'La Bayadère':
        return '50'
    elif name == 'Don Chisciotte':
        return '51'
    elif name == 'Morte Da Dietro':
        return '52'
    elif name == 'Il lago dei cani':
        return '53'
    elif name == 'Il Mandorlaro':
        return '54'
    elif name == 'Teresaaaaa':
        return '55'
    elif name == 'La Brianza':
        return '56'
    elif name == 'Don Mannio':
        return '57'
    elif name == 'La Seppia Bruna':
        return '58'
    elif name == 'La cena di Natale':
        return '59'
    elif name == 'Il compleanno':
        return '60'
    elif name == 'Il segreto di Babbo Natale':
        return '61'
    elif name == 'Un Natale da ricordare':
        return '62'
    elif name == 'La festa di Capodanno':
        return '63'
    elif name == 'La notte di San Silvestro':
        return '64'
    elif name == 'La storia di un viaggio':
        return '65'
    elif name == 'Il mistero della vecchia casa':
        return '66'
    elif name == 'Il ladro di sogni':
        return '67'
    elif name == 'Il segreto del faro':
        return '68'
    elif name == 'La dama misteriosa':
        return '69'
    elif name == 'La città perduta':
        return '70'
    elif name == 'Il viaggio nel tempo':
        return '71'
    elif name == 'Il circo magico':
        return '72'
    elif name == 'Il teatro delle ombre':
        return '73'
    elif name == 'Il regno incantato':
        return '74'
    elif name == 'Il mistero dell isola deserta':
        return '75'
    elif name == 'La notte delle stelle cadenti':
        return '76'
    elif name == 'Il circo degli animali parlanti':
        return '77'
    elif name == 'La foresta magica':
        return '78'
    elif name == 'Il segreto dell orologio magico':
        return '79'
    elif name == 'Il mistero del libro antico':
        return '80'
    elif name == 'Il castello delle illusioni':
        return '81'
    elif name == 'Il tesoro nascosto':
        return '82'
    elif name == 'Il viaggio nel mondo delle fiabe':
        return '83'
    elif name == 'La leggenda del drago':
        return '84'
    elif name == 'Il regno delle meraviglie':
        return '85'
    elif name == 'La terra dei giganti':
        return '86'
    elif name == 'Il libro delle avventure':
        return '87'
    elif name == 'La storia del vecchio orologio':
        return '88'
    elif name == 'Il segreto della porta magica':
        return '89'
    elif name == 'La notte delle streghe':
        return '90'
    elif name == 'Il regno dei fantasmi':
        return '91'
    elif name == 'La leggenda della luna blu':
        return '92'
    elif name == 'Il castello incantato':
        return '93'
    elif name == 'Il giardino segreto':
        return '94'
    elif name == 'La città degli angeli':
        return '95'
    elif name == 'Il teatro delle illusioni':
        return '96'
    elif name == 'Il mistero dell antica civiltà':
        return '97'
    elif name == 'La notte dei maghi':
        return '98'
    elif name == 'Il regno dei sogni':
        return '99'
    elif name == 'La leggenda dell albero magico':
        return '100'
    elif name == 'Il libro dei segreti':
        return '101'
    elif name == 'La storia del vecchio burattinaio':
        return '102'
    elif name == 'Il segreto della lanterna magica':
        return '103'
    elif name == 'La notte delle creature fantastiche':
        return '104'
    elif name == 'Il viaggio nel mondo delle ombre':
        return '105'
    elif name == 'Il castello dei fantasmi':
        return '106'
    elif name == 'Il regno delle fate':
        return '107'
    elif name == 'La leggenda del cigno bianco':
        return '108'
    elif name == 'Il mistero della porta dimensionale':
        return '109'
    elif name == 'La notte delle storie perdute':
        return '110'
    elif name == 'Il regno dei draghi':
        return '111'
    elif name == 'La leggenda dell ultima stella':
        return '112'
    else:
        return 'id not found'


def format_time(time):
    hour = time.split('.')
    mins = int(hour[1])
    hour = int(hour[0])

    if hour > 23 or hour < 0:
        print('Orario non valido')
        exit(0)
    elif (hour > 20 or hour < 8) or (hour == 20 and mins > 0):
        print('Teatro Chiuso')
        exit(0)
    else:
        return str(hour)


if __name__ == "__main__":

    problem = Problem()
    problem.addVariable("Day", [1, 2, 3, 4, 5, 6, 7])
    problem.addVariable("Time", [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    problem.addVariable("Idopera",
                        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                         27, 28,
                         29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                         43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                         53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
                         68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
                         84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
                         100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112])
    # vincoli orari settimana
    problem.addConstraint(lambda Day, Time, Idopera:
                          (Day == 1 and 8 <= Time <= 9 and Idopera == 1)
                          or (Day == 1 and 9 <= Time <= 10 and Idopera == 8)
                          or (Day == 1 and 10 <= Time <= 11 and Idopera == 15)
                          or (Day == 1 and 11 <= Time <= 12 and Idopera == 22)
                          or (Day == 1 and 12 <= Time <= 13 and Idopera == 29)
                          or (Day == 1 and 13 <= Time <= 14 and Idopera == 36)
                          or (Day == 1 and 14 <= Time <= 15 and Idopera == 43)
                          or (Day == 1 and 15 <= Time <= 16 and Idopera == 50)
                          or (Day == 1 and 16 <= Time <= 17 and Idopera == 57)
                          or (Day == 1 and 17 <= Time <= 18 and Idopera == 64)
                          or (Day == 1 and 18 <= Time <= 19 and Idopera == 71)
                          or (Day == 1 and 19 <= Time <= 20 and Idopera == 78)
                          or (Day == 1 and 20 <= Time <= 21 and Idopera == 85)
                          or (Day == 1 and 21 <= Time <= 22 and Idopera == 92)
                          or (Day == 1 and 22 <= Time <= 23 and Idopera == 99)
                          or (Day == 1 and 23 <= Time <= 24 and Idopera == 106)
                          or (Day == 2 and 8 <= Time <= 9 and Idopera == 2)
                          or (Day == 2 and 9 <= Time <= 10 and Idopera == 9)
                          or (Day == 2 and 10 <= Time <= 11 and Idopera == 16)
                          or (Day == 2 and 11 <= Time <= 12 and Idopera == 23)
                          or (Day == 2 and 12 <= Time <= 13 and Idopera == 30)
                          or (Day == 2 and 13 <= Time <= 14 and Idopera == 37)
                          or (Day == 2 and 14 <= Time <= 15 and Idopera == 44)
                          or (Day == 2 and 15 <= Time <= 16 and Idopera == 51)
                          or (Day == 2 and 16 <= Time <= 17 and Idopera == 58)
                          or (Day == 2 and 17 <= Time <= 18 and Idopera == 65)
                          or (Day == 2 and 18 <= Time <= 19 and Idopera == 72)
                          or (Day == 2 and 19 <= Time <= 20 and Idopera == 79)
                          or (Day == 2 and 20 <= Time <= 21 and Idopera == 86)
                          or (Day == 2 and 21 <= Time <= 22 and Idopera == 93)
                          or (Day == 2 and 22 <= Time <= 23 and Idopera == 100)
                          or (Day == 2 and 23 <= Time <= 24 and Idopera == 107)
                          or (Day == 3 and 8 <= Time <= 9 and Idopera == 3)
                          or (Day == 3 and 9 <= Time <= 10 and Idopera == 10)
                          or (Day == 3 and 10 <= Time <= 11 and Idopera == 17)
                          or (Day == 3 and 11 <= Time <= 12 and Idopera == 24)
                          or (Day == 3 and 12 <= Time <= 13 and Idopera == 31)
                          or (Day == 3 and 13 <= Time <= 14 and Idopera == 38)
                          or (Day == 3 and 14 <= Time <= 15 and Idopera == 45)
                          or (Day == 3 and 15 <= Time <= 16 and Idopera == 52)
                          or (Day == 3 and 16 <= Time <= 17 and Idopera == 59)
                          or (Day == 3 and 17 <= Time <= 18 and Idopera == 66)
                          or (Day == 3 and 18 <= Time <= 19 and Idopera == 73)
                          or (Day == 3 and 19 <= Time <= 20 and Idopera == 80)
                          or (Day == 3 and 20 <= Time <= 21 and Idopera == 87)
                          or (Day == 3 and 21 <= Time <= 22 and Idopera == 94)
                          or (Day == 3 and 22 <= Time <= 23 and Idopera == 101)
                          or (Day == 3 and 23 <= Time <= 24 and Idopera == 108)
                          or (Day == 4 and 8 <= Time <= 9 and Idopera == 4)
                          or (Day == 4 and 9 <= Time <= 10 and Idopera == 11)
                          or (Day == 4 and 10 <= Time <= 11 and Idopera == 18)
                          or (Day == 4 and 11 <= Time <= 12 and Idopera == 25)
                          or (Day == 4 and 12 <= Time <= 13 and Idopera == 32)
                          or (Day == 4 and 13 <= Time <= 14 and Idopera == 39)
                          or (Day == 4 and 14 <= Time <= 15 and Idopera == 46)
                          or (Day == 4 and 15 <= Time <= 16 and Idopera == 53)
                          or (Day == 4 and 16 <= Time <= 17 and Idopera == 60)
                          or (Day == 4 and 17 <= Time <= 18 and Idopera == 67)
                          or (Day == 4 and 18 <= Time <= 19 and Idopera == 74)
                          or (Day == 4 and 19 <= Time <= 20 and Idopera == 81)
                          or (Day == 4 and 20 <= Time <= 21 and Idopera == 88)
                          or (Day == 4 and 21 <= Time <= 22 and Idopera == 95)
                          or (Day == 4 and 22 <= Time <= 23 and Idopera == 102)
                          or (Day == 4 and 23 <= Time <= 24 and Idopera == 109)
                          or (Day == 5 and 8 <= Time <= 9 and Idopera == 5)
                          or (Day == 5 and 9 <= Time <= 10 and Idopera == 12)
                          or (Day == 5 and 10 <= Time <= 11 and Idopera == 19)
                          or (Day == 5 and 11 <= Time <= 12 and Idopera == 26)
                          or (Day == 5 and 12 <= Time <= 13 and Idopera == 33)
                          or (Day == 5 and 13 <= Time <= 14 and Idopera == 40)
                          or (Day == 5 and 14 <= Time <= 15 and Idopera == 47)
                          or (Day == 5 and 15 <= Time <= 16 and Idopera == 54)
                          or (Day == 5 and 16 <= Time <= 17 and Idopera == 61)
                          or (Day == 5 and 17 <= Time <= 18 and Idopera == 68)
                          or (Day == 5 and 18 <= Time <= 19 and Idopera == 75)
                          or (Day == 5 and 19 <= Time <= 20 and Idopera == 82)
                          or (Day == 5 and 20 <= Time <= 21 and Idopera == 89)
                          or (Day == 5 and 21 <= Time <= 22 and Idopera == 96)
                          or (Day == 5 and 22 <= Time <= 23 and Idopera == 103)
                          or (Day == 5 and 23 <= Time <= 24 and Idopera == 110)
                          or (Day == 6 and 8 <= Time <= 9 and Idopera == 6)
                          or (Day == 6 and 9 <= Time <= 10 and Idopera == 13)
                          or (Day == 6 and 10 <= Time <= 11 and Idopera == 20)
                          or (Day == 6 and 11 <= Time <= 12 and Idopera == 27)
                          or (Day == 6 and 12 <= Time <= 13 and Idopera == 34)
                          or (Day == 6 and 13 <= Time <= 14 and Idopera == 41)
                          or (Day == 6 and 14 <= Time <= 15 and Idopera == 48)
                          or (Day == 6 and 15 <= Time <= 16 and Idopera == 55)
                          or (Day == 6 and 16 <= Time <= 17 and Idopera == 62)
                          or (Day == 6 and 17 <= Time <= 18 and Idopera == 69)
                          or (Day == 6 and 18 <= Time <= 19 and Idopera == 76)
                          or (Day == 6 and 19 <= Time <= 20 and Idopera == 83)
                          or (Day == 6 and 20 <= Time <= 21 and Idopera == 90)
                          or (Day == 6 and 21 <= Time <= 22 and Idopera == 97)
                          or (Day == 6 and 22 <= Time <= 23 and Idopera == 104)
                          or (Day == 6 and 23 <= Time <= 24 and Idopera == 111)
                          or (Day == 7 and 8 <= Time <= 9 and Idopera == 7)
                          or (Day == 7 and 9 <= Time <= 10 and Idopera == 14)
                          or (Day == 7 and 10 <= Time <= 11 and Idopera == 21)
                          or (Day == 7 and 11 <= Time <= 12 and Idopera == 28)
                          or (Day == 7 and 12 <= Time <= 13 and Idopera == 35)
                          or (Day == 7 and 13 <= Time <= 14 and Idopera == 42)
                          or (Day == 7 and 14 <= Time <= 15 and Idopera == 49)
                          or (Day == 7 and 15 <= Time <= 16 and Idopera == 56)
                          or (Day == 7 and 16 <= Time <= 17 and Idopera == 63)
                          or (Day == 7 and 17 <= Time <= 18 and Idopera == 70)
                          or (Day == 7 and 18 <= Time <= 19 and Idopera == 77)
                          or (Day == 7 and 19 <= Time <= 20 and Idopera == 84)
                          or (Day == 7 and 20 <= Time <= 21 and Idopera == 91)
                          or (Day == 7 and 21 <= Time <= 22 and Idopera == 98)
                          or (Day == 7 and 22 <= Time <= 23 and Idopera == 105)
                          or (Day == 7 and 23 <= Time <= 24 and Idopera == 112)
                          )

    if check_record((problem.getSolutions())):
        print("L'opera e' in scena durante l'orario selezionato\n")
        print("Ecco come arrivarci")
        RicercaGrafo.research(Utils.get_opera_name(id))
    else: print("Spettacolo non in scena durante l'orario selezionato")
=======
import csv
import pulp

def load_records_from_csv(file_path):
    records = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            records.append(row)
    return records


def create_schedule(records):
    # Creazione del problema di ottimizzazione
    prob = pulp.LpProblem("Schedule_Operas", pulp.LpMaximize)

    # Definizione delle variabili
    operas = set(record['idopera'] for record in records)
    opera_vars = pulp.LpVariable.dicts("Opera", operas, 0, 1, pulp.LpInteger)

    # Definizione della funzione obiettivo
    prob += pulp.lpSum([opera_vars[opera] for opera in operas])

    # Vincoli
    for record in records:
        giorno = record['giorno']
        ora = record['ora']
        opera = record['idopera']
        prob += pulp.lpSum([opera_vars[opera]]) <= 1, f"Constraint_{opera}_{giorno}_{ora}"

    return prob

if __name__ == "__main__":
    records = load_records_from_csv("./dataset/programmazione.csv")

    prob = create_schedule(records)
    prob.solve()

    nome_opera = input("Inserisci il nome dell'opera teatrale: ")
    giorno = input("Inserisci il giorno come numero (1:Lunedì, 2:Martedì, ...): ")
    ora = input("Inserisci l'orario in formato HH:MM: ")

    opera_selezionata = [opera_var for opera_var in prob.variables() if opera_var.name.split('_')[1] == nome_opera][0]
    if opera_selezionata.varValue == 1:
        print("L'opera teatrale è disponibile.")
    else:
        print("L'opera teatrale non è disponibile.")
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
