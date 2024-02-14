import csv
from fuzzywuzzy import fuzz
from gensim.parsing.preprocessing import remove_stopwords
from PIL import Image
<<<<<<< HEAD

=======
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d

def show_planimetry():
    """
    Mostra l'immagine della planimetria.
    """
<<<<<<< HEAD
    im = Image.open("../img/Planimetria.png")
    im.show()


def find_opera(idopera):
=======
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
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
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

<<<<<<< HEAD

=======
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
def get_opera_id(idopera):
    """
    Ottiene l'ID di un'opera a partire dal suo nome.
    
    Args:
        idopera (str): Il nome dell'opera.
        
    Returns:
        str: L'ID dell'opera.
    """
<<<<<<< HEAD
    opera_info = find_opera(idopera)[0]
    return opera_info


def get_opera_name(idopera):
    """
    Ottiene il nome di un opera a partire dal suo ID.

=======
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
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
        
    Returns:
        str: Il nome del opera.
    """
    ris = find_opera(idopera)[1]
    return ris

<<<<<<< HEAD

def get_sala(idopera):
=======
def get_rack(idopera):
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
    """
    Ottiene il numero della sala dell'opera a partire dal suo ID.
    
    Args:
        idopera (int32): L'ID dell'opera.

    Returns:
        int: Il numero della sala.
    """
    if idopera is not None:
<<<<<<< HEAD
        idsala = int(float(idopera) / 7) + 1
        return idsala
=======
        n_room = int(float(idopera) / 50) + 1
        return n_room
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
    else:
        return None


def get_nodo(sala):
    """
    Ottiene il numero del nodo per una data sala.

    Args:
        sala (int): Il numero della sala.

    Returns:
        int: Il numero del nodo.
    """
<<<<<<< HEAD
    if sala == 1 or sala == 3:
        return 2
    elif sala == 2:
=======
    if room == 1:
        return 5
    elif room == 2:
        return 6
    elif room == 3:
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
        return 3
    elif sala == 11:
        return 11
    elif sala == 4:
        return 1
    elif sala == 8:
        return 4
    elif sala == 5 or sala == 6 or sala == 7:
        return 5
    elif sala == 9 or sala == 13:
        return 7
    elif sala == 14 or sala == 15 or sala == 16:
        return 13
    elif sala == 10 or sala == 12:
        return 10
    else:
        return None
<<<<<<< HEAD
# Restituisce None se la sala specificata non è gestita
=======
# Restituisce None se la sala specificata non è gestita
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
