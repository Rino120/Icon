import os
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import fuzz
from gensim.parsing.preprocessing import remove_stopwords
import RicercaGrafo
import Utils


<<<<<<< HEAD
def _fuzzy_matching(hashmap, fav_opera):
    """
    restituisce la corrispondenza più vicina tramite rapporto fuzzy.
    Se non viene trovata alcuna corrispondenza, restituisce None

    parametri:

    hashmap: dict, mappa il titolo dell'opera all'indice dell'opera nei dati

    fav_opere: str, nome dell'opera inserita dall'utente

    return:

    indice della corrispondenza più vicina
    """
    match_tuple = []
    # ottieni la corrispondenza
    for titolo, idx in hashmap.items():
        ratio = fuzz.ratio(remove_stopwords(titolo.lower().replace(",", " ")),
                           remove_stopwords(fav_opera.lower().replace(",", " ")))
        if ratio >= 60:
            match_tuple.append((titolo, idx, ratio))
    # ordina
    match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
    if not match_tuple:
        print('Nessun risultato trovato')
    else:
        print('Risultati trovati: \n' + str([x[0] for x in match_tuple]))
        return match_tuple[0][1]


=======
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
class KnnRecommender:
    def __init__(self):
        self.path_opera = './dataset/Opere.csv'
        self.path_rating = './dataset/Rating.csv'
<<<<<<< HEAD
        self.opera_rating_thres = 4
=======
        self.opera_rating_thres = 10
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
        self.user_rating_thres = 10
        self.model = NearestNeighbors()
        self.model.set_params(**{
            'n_neighbors': 20,
            'algorithm': 'auto',
            'metric': 'cosine',
        })

    def _prep_data(self):
        """
        prepara i dati per il recommender
        unisce i dataframe
        """
        # leggi i dati
        df_opere = pd.read_csv(
            os.path.join(self.path_opera),
<<<<<<< HEAD
            usecols=['idopera', 'titolo', 'genere'],
            dtype={'idopera': 'int32', 'titolo': 'str', 'genere': 'str'})
=======
            usecols=['idopera', 'titolo','genere'],
            dtype={'idopera': 'int32', 'titolo': 'str', 'genere' : 'str'})

>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d

        df_rating = pd.read_csv(
            os.path.join(self.path_rating),
            usecols=['idutente', 'idopera', 'valutazione'],
            dtype={'idutente': 'int32', 'idopera': 'int32', 'valutazione': 'float32'})

<<<<<<< HEAD
        # filtra gli utenti che hanno valutato meno di 4 opere e le opere con meno di 10 valutazioni
=======
        # filtra gli utenti che hanno valutato meno di 10 opere e le opere con meno di 10 valutazioni
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
        df_opere_cnt = pd.DataFrame(df_rating.groupby('idopera').size(), columns=['count'])
        popular_opere = list(df_opere_cnt.query('count >= @self.opera_rating_thres').index)
        opere_filter = df_rating.idopera.isin(popular_opere).values

        df_users_cnt = pd.DataFrame(df_rating.groupby('idutente').size(), columns=['count'])
        active_users = list(df_users_cnt.query('count >= @self.user_rating_thres').index)
        users_filter = df_rating.idutente.isin(active_users).values

        df_rating_filtered = df_rating[opere_filter & users_filter]

        # crea la matrice opera-utente
        opera_user_mat = df_rating_filtered.pivot(index='idopera', columns='idutente', values='valutazione').fillna(0)

        # hashmap dal titolo dell'opera all'indice
        hashmap = {
            opera: i for i, opera in
            enumerate(list(df_opere.set_index('idopera').loc[opera_user_mat.index].titolo))
        }
        opera_user_mat_sparse = csr_matrix(opera_user_mat.values)
        return opera_user_mat_sparse, hashmap

<<<<<<< HEAD
    def _inference(self, model, data, hashmap,
                   fav_opera, n_recommendations):
=======
    def _fuzzy_matching(self, hashmap, fav_opera):
        """
        restituisce la corrispondenza più vicina tramite rapporto fuzzy.
        Se non viene trovata alcuna corrispondenza, restituisce None

        parametri:

        hashmap: dict, mappa il titolo dell'opera all'indice dell'opera nei dati

        fav_opere: str, nome dell'opera inserita dall'utente

        return:

        indice della corrispondenza più vicina
        """
        match_tuple = []
        # ottieni la corrispondenza
        for titolo, idx in hashmap.items():
            ratio = fuzz.ratio(remove_stopwords(titolo.lower().replace(",", " ")),
                                remove_stopwords(fav_opera.lower().replace(",", " ")))
            if ratio >= 60:
                match_tuple.append((titolo, idx, ratio))
        # ordina
        match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
        if not match_tuple:
            print('Nessun risultato trovato')
        else:
            print('Risultati trovati: \n' + str([x[0] for x in match_tuple]))
            return match_tuple[0][1]

    def _inference(self, model, data, hashmap,
                fav_opera, n_recommendations):
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
        """
        restituisce le prime n raccomandazioni di opere simili in base all'opera inserita dall'utente

        parametri:

        model: modello sklearn, modello knn

        data: matrice opera-utente

        hashmap: dict, mappa il titolo dell'opera all'indice dell'opera nei dati

        fav_opera: str, nome dell'opera inserita dall'utente

        n_recommendations: int, prime n raccomandazioni

        return:

        lista delle prime n raccomandazioni di opere simili
        """
        # addestra
        model.fit(data)
        # ottieni l'indice dell'opera di input
        print('La tua opera è:', fav_opera)
        try:
<<<<<<< HEAD
            idx = _fuzzy_matching(hashmap, fav_opera)
=======
            idx = self._fuzzy_matching(hashmap, fav_opera)
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
            # inferenza
            distances, indices = model.kneighbors(
                data[idx],
                n_neighbors=n_recommendations + 1)
        except IndexError:
            exit(0)
        # ottieni la lista degli indici grezzi delle raccomandazioni
        raw_recommends = \
            sorted(
                list(
                    zip(
                        indices.squeeze().tolist(),
                        distances.squeeze().tolist()
                    )
                ),
                key=lambda x: x[1]
            )[1:6]

        # restituisci la raccomandazione (idopera, distanza)
        return raw_recommends

    def make_recommendations(self, fav_opera, n_recommendations):
        """
        crea le prime n raccomandazioni di opere

        parametri:

        fav_opera: str, nome dell'opera inserita dall'utente

        n_recommendations: int, prime n raccomandazioni
        """
        # ottieni i dati
        opera_user_mat_sparse, hashmap = self._prep_data()
        # ottieni le raccomandazioni
        raw_recommends = self._inference(
            self.model, opera_user_mat_sparse, hashmap,
            fav_opera, n_recommendations)
        # stampa i risultati
<<<<<<< HEAD
        opera_lista = []
=======
        opera_list = []
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
        reverse_hashmap = {v: k for k, v in hashmap.items()}
        print('Raccomandazioni per: ' + fav_opera)
        for i, (idx, dist) in enumerate(raw_recommends):
            print('{0}: {1}, con una distanza '
<<<<<<< HEAD
                  'di {2}'.format(i + 1, reverse_hashmap[idx], dist))
            opera_lista.append(reverse_hashmap[idx])
        return opera_lista


if __name__ == '__main__':
    print("Benvenuto al nostro programma di raccomandazione e ricerca nel grafo del teatro sociale!")
    while True:
        print("\nCosa desideri fare?")
        print("1. Mostra la planimetria del teatro sociale")
        print("2. Consiglia opere")
        print("3. Trova soluzione nel grafo")
        print("4. Esci")

        choice = input("Scegli un'opzione: ")

        if choice == '1':
            input("Premi [invio] per mostrare la planimetria del teatro sociale")
            Utils.show_planimetry()
        elif choice == '2':
            opera_pref = input('Inserisci il nome dell\'opera preferita:\n')
            top_n = 2
            recommender = KnnRecommender()
            recommendation = recommender.make_recommendations(opera_pref, top_n)
            if recommendation is not None:
                RicercaGrafo.research(recommendation)
            else:
                print("Non trovato")
        elif choice == '3':
            # Esegue la ricerca di una soluzione nel grafo
            graph, _, _ = RicercaGrafo.setup_graph()
            start_node = 0
            RicercaGrafo.find_solution(graph, start_node)
        elif choice == '4':
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")
=======
                'di {2}'.format(i + 1, reverse_hashmap[idx], dist))
            opera_list.append(reverse_hashmap[idx])
        return opera_list


if __name__ == '__main__':
    input("Premi [invio] per mostrare la planimetria del teatro sociale")
    Utils.show_planimetry()
    opera_name = input('Inserisci il nome dell\'opera preferita:\n')
    top_n = 5
    recommender = KnnRecommender()
    recommendation = recommender.make_recommendations(opera_name, top_n)
    if recommendation is not None:
        RicercaGrafo.research(recommendation)
    else:
        print("Non trovato")
>>>>>>> 57bd5057fe71bb0d0c4aa5aa5a45360c82b8306d
