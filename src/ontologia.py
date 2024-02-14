from owlready2 import *

print("ONTOLOGIA\n")
onto = get_ontology("theatre_show.owl").load()

# Stampa il contenuto principale dell'ontologia
print("Lista delle classi nell'ontologia:\n")
print(list(onto.classes()), "\n")

# Stampa le proprietà oggetto dell'ontologia
print("Proprietà oggetto nell'ontologia:\n")
print(list(onto.object_properties()), "\n")

# Stampa le proprietà dati dell'ontologia
print("Proprietà dati nell'ontologia:\n")
print(list(onto.data_properties()), "\n")

# Stampa gli individui per classi specifiche
print("Lista degli Attori nell'ontologia:\n")
attori = onto.search(is_a=onto.Attore)
print(attori, "\n")

print("Lista dei Direttori nell'ontologia:\n")
direttori = onto.search(is_a=onto.Direttore)
print(direttori, "\n")

print("Lista dei Generi nell'ontologia:\n")
generi = onto.search(is_a=onto.Genere)
print(generi, "\n")

print("Lista degli Spettacoli nell'ontologia:\n")
spettacoli = onto.search(is_a=onto.Spettacolo)
print(spettacoli, "\n")

print("Lista degli Spettatori nell'ontologia:\n")
spettatori = onto.search(is_a=onto.Spettatore)
print(spettatori, "\n")

print("Lista dei Teatri nell'ontologia:\n")
teatri = onto.search(is_a=onto.Teatro)
print(teatri, "\n")

print("Lista dei Voti nell'ontologia:\n")
voti = onto.search(is_a=onto.Voto)
print(voti, "\n")

# esempi di query
print("Lista degli spettacoli di genere commedia:\n")
film = onto.search(is_a=onto.Spettacolo, haGenere=onto.search(is_a=onto.commedia))
print(film, "\n")
