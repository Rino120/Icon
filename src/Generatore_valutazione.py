import pandas as pd
import random

num_utenti = 10
num_opere_disponibili = 112
opere_da_votare_per_utente = 50

# Inizializzo le liste
idutente = []
idopera = []
valutazione = []

# Dizionario per tenere traccia delle opere già valutate da ciascun utente
opere_valutate = {utente: set() for utente in range(1, num_utenti + 1)}

# Genera dei dati casuali per il dataset
for utente in range(1, num_utenti + 1):
    opere_da_votare = random.sample(range(1, num_opere_disponibili + 1), opere_da_votare_per_utente)
    for opera in opere_da_votare:
        while opera in opere_valutate[utente]:  # Verifica se l'opera è già stata valutata
            opera = random.randint(1, num_opere_disponibili)  # Genera un'altra opera se già valutata
        opere_valutate[utente].add(opera)  # Aggiunge l'opera valutata al set
        idutente.append(utente)
        idopera.append(opera)
        valutazione.append(random.randint(1, 5))

# Creazione DataFrame con i dati generati
df = pd.DataFrame({'idutente': idutente, 'idopera': idopera, 'valutazione': valutazione})

# Specifica il percorso dei ratings
percorso_del_file = './Dataset/Rating.csv'

# Salva il DataFrame su disco in formato CSV
df.to_csv(percorso_del_file, index=False)
