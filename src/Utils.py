import csv
from fuzzywuzzy import fuzz  # Libreria per calcolare la similarità tra stringhe
from gensim.parsing.preprocessing import remove_stopwords  # Rimuove le parole comuni che non aggiungono significato
from PIL import Image  # Per lavorare con immagini

def show_planimetry():
    """
    Mostra l'immagine della planimetria.
    """
    try:
        im = Image.open("./img/planimetry.png")
        im.show()
    except Exception as e:
        print("Si è verificato un errore nell'apertura dell'immagine:", e)


def find_opera(opera):
    """
    Trova un'opera nel database di opere.
    
    Args:
        opera (str): Il nome dell'opera da cercare.
        
    Returns:
        list: Informazioni sull'opera trovato.
    """
    # Apre il file CSV contenente le opere
    csv_file = csv.reader(open('./Opere.csv', "r", encoding="utf8"), delimiter=",")
    max = 0
    ris = None
    # Itera su ogni riga del file CSV
    for row in csv_file:
        # Calcola la similarità tra il nome dell'opera cercato e il nome dell'opera nella riga attuale
        similarity = fuzz.ratio(remove_stopwords(opera.lower().replace(",", " ")),
                                remove_stopwords(row[1].lower().replace(",", " ")))
        # Se la similarità supera una soglia del 60% e è maggiore della similarità massima trovata finora
        if similarity > 60 and similarity > max:
            max = similarity  # Aggiorna la similarità massima
            ris = row  # Aggiorna le informazioni sull'opera
    return ris

def get_opera_id(opera):
    """
    Ottiene l'ID di un'opera a partire dal suo nome.
    
    Args:
        opera (str): Il nome dell'opera.
        
    Returns:
        str: L'ID dell'opera.
    """
    ris = find_opera(opera)[0]
    return ris

def get_opera_name(opera):
    """
    Ottiene il nome di un opera a partire dal suo ID.
    
    Args:
        opera (str): L'ID del opera.
        
    Returns:
        str: Il nome del opera.
    """
    ris = find_opera(opera)[1]
    return ris

def get_rack(opera_id):
    """
    Ottiene il numero della sala dell'opera a partire dal suo ID.
    
    Args:
        opera_id (str): L'ID dell'opera.
        
    Returns:
        int: Il numero della sala.
    """
    # Calcola il numero della sala utilizzando l'ID del film
    n_rack = int(float(opera_id) / 3520) + 1
    return n_rack

def get_nodes(room):
    """
    Ottiene il numero di nodi per una data sala.

    Args:
        room (int): Il numero della sala.

    Returns:
        int: Il numero di nodi.
    """
    # Assegna un numero di nodi in base al numero della sala
    if room == 1:
        return 5
    elif room == 2:
        return 6
    elif room == 3:
        return 3
    elif room == 4:
        return 9
    elif room == 5:
        return 11
    elif room == 6:
        return 13
    elif room == 7:
        return 12
    elif room == 8:
        return 14
    else:
        return None  # Restituisce None se la sala specificata non è gestita