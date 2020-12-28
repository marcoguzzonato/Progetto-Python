class nodo():
    def __init__(self, index, id, nome, flag, peso, prev, vicini):  # oggetto nodo
        self.index = index  # definisco gli attributi dell'oggetto nodo
        self.id = id
        self.nome = nome
        self.flag = flag
        self.peso = peso
        self.prev = prev
        self.vicini = vicini


nodi = []  # struttura dati per rappresentare il grafo (una lista che contiene tutti i nodi che compongono il grafo)

nodi.append(nodo(0, "111", "Londra", True, float('inf'), "",
                 {"222": 2, "555": 8}))  # definisco gli attributi per ogni nodo appartenente al grafo
nodi.append(nodo(1, "222", "Mosca", True, float('inf'), "", {"333": 6, "444": 2}))
nodi.append(nodo(2, "333", "Tokyo", True, float('inf'), "", {"777": 5}))
nodi.append(nodo(3, "444", "Dubay", True, float('inf'), "", {"555": 2, "666": 9}))
nodi.append(nodo(4, "555", "Sidney", True, float('inf'), "", {"666": 3}))
nodi.append(nodo(5, "666", "New York", True, float('inf'), "", {"777": 1}))
nodi.append(nodo(6, "777", "Londra fine", True, float('inf'), "", {}))

# gli unici nodi dove siamo sicuri di passare sono quello iniziale e quello finale quindi li impostiamo

inizio = "111"
fine = "777"

# ricerco il nodo di partenza e lo imposto per la partenza dell'algoritmo

for x in nodi:
    if (x.id == inizio):
        x.flag = False
        x.peso = 0
        x.prev = inizio
        i = x.index

k = 0

# ciclo dell'algortimo per il calcolo del percorso minimo del grafo

while True:
    for x in nodi[i].vicini.keys():
        for y in nodi:
            if (y.id == x and y.flag):
                somma = nodi[i].peso + nodi[i].vicini[x]
                if (y.peso > somma):
                    y.peso = somma
                    y.prev = nodi[i].id

    potenziale = float('inf')
    for z in nodi:
        if (z.flag and z.peso < potenziale):
            potenziale = z.peso
            n = z.index

    nodi[n].flag = False
    i = n
    if (k != 0 and nodi[i].id == fine):
        lunghezza = nodi[i].peso
        break
    k = k + 1

percorso_id = []  # lista dove inserire tutti i nodi visitati in ordine cronologico
percorso_nomi = []
s = fine
while True:
    percorso_id.append(s)
    for x in nodi:
        if (x.id == s):
            s = x.prev
    if (s == inizio):
        percorso_id.append(s)
        break
for x in percorso_id:
    for y in nodi:
        if (y.id == x):
            percorso_nomi.append(y.nome)

percorso_nomi.reverse()
strada = "-".join(percorso_nomi)
print("Tragitto: " + strada)
print("Il tempo minimo per completare il percorso è " + str(lunghezza) + " ore che corrispondono a " + str(float(lunghezza) / 24.) + " giorni.")
