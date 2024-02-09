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