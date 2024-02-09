import csv
from fuzzywuzzy import fuzz
from gensim.parsing.preprocessing import remove_stopwords
from PIL import Image

def show_planimetry():
    """
    Mostra l'immagine della planimetria.
    """
    im = Image.open("../img/Planimetria_Teatro.png")
    im.show()

def find_opera(idopera):
    """
    Trova un'opera nel database di opere.
    
    Args:
        opera (str): Il nome dell'opera da cercare.
        
    Returns:
        list: Informazioni sull'opera trovato.
    """
    # Apre il file CSV contenente le opere
    csv_file = csv.reader(open('./dataset/Opere.csv', "r", encoding="utf-8"), delimiter=",")
    max_similarity = 0
    ris = None
    # Itera su ogni riga del file CSV
    for row in csv_file:
        # Rimuove le stopwords solo se idopera è una stringa
        if isinstance(idopera, str):
            idopera_processed = remove_stopwords(idopera.lower().replace(",", " "))
        else:
            idopera_processed = idopera
        # Calcola la similarità tra il nome dell'opera cercato e il nome dell'opera nella riga attuale
        similarity = fuzz.ratio(idopera_processed, remove_stopwords(row[1].lower().replace(",", " ")))
        if similarity > 70 and similarity > max_similarity:
            max_similarity = similarity
            ris = row
    return ris

def get_opera_id(idopera):
    """
    Ottiene l'ID di un'opera a partire dal suo nome.
    
    Args:
        idopera (str): Il nome dell'opera.
        
    Returns:
        str: L'ID dell'opera.
    """
    opera_info = find_opera(idopera)
    if opera_info is not None:
        return opera_info[0]
    else:
        return None

def get_opera_name(idopera):
    """
    Ottiene il nome di un opera a partire dal suo ID.
    
    Args:
        idopera (int32): L'ID del opera.
        
    Returns:
        str: Il nome del opera.
    """
    ris = find_opera(idopera)[1]
    return ris

def get_rack(idopera):
    """
    Ottiene il numero della sala dell'opera a partire dal suo ID.
    
    Args:
        idopera (int32): L'ID dell'opera.

    Returns:
        int: Il numero della sala.
    """
    if idopera is not None:
        n_room = int(float(idopera) / 50) + 1
        return n_room
    else:
        return None

def get_nodes(room):
    """
    Ottiene il numero di nodi per una data sala.

    Args:
        room (int): Il numero della sala.

    Returns:
        int: Il numero di nodi.
    """
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
        return None
# Restituisce None se la sala specificata non è gestita