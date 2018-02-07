import h5py
import os.path
import sys
from random import shuffle

def getInfoFromCSV(filename, targetPosition):
    # La funzione ritorna un dataset, una lista di attributo e l'attributo target con in input
    # un file csv (comma separeted values) e la posizione del target all'interno della lista di attributi
    file = open(filename, 'r')
    lines = [line.strip() for line in file.readlines()]

    attributes = [attribute.strip() for attribute in lines.pop(0).split(",")]
    targetAttribute = attributes[targetPosition-1]

    # Viene creata una lista di dizionario. Ogni riga sara' quindi un dizionario dove ad ogni attributo
    # sara' associato un certo valore
    data = []
    for line in lines:
        data.append(dict(zip(attributes, [element.strip() for element in line.split(",")])))

    # Lo score del k-fold cross validation dipende molto (da come e' stata scritta la funzione che se ne occupa)
    # dall'ordine delle righe nel dataSet. Grazie ad uno shuffle sui dati non si ha piu' questa forte dipendenza
    shuffle(data)

    file.close()
    return (data, attributes, targetAttribute)

def setDiscreteDataValuesForAdoptedChildren(data):
    # La funzione modifica il valori del dataSet "adoptedChildren". I valori del dataSet sono continui e quindi
    # la modifica permette di avere piu' valori comuni tra le righe
    for i in range(0, len(data)):
        data[i]["FMED"] = str(int(data[i]["FMED"]) - (int(data[i]["FMED"]) % 2))
        data[i]["Age2IQ"] = str(int(data[i]["Age2IQ"]) - (int(data[i]["Age2IQ"]) % 5))
        data[i]["Age4IQ"] = str(int(data[i]["Age4IQ"]) - (int(data[i]["Age4IQ"]) % 5))
        data[i]["Age8IQ"] = str(int(data[i]["Age8IQ"]) - (int(data[i]["Age8IQ"]) % 5))
        data[i]["TMIQ"] = str(int(data[i]["TMIQ"]) - (int(data[i]["TMIQ"]) % 5))
        data[i]["Age13IQ"] = str(int(data[i]["Age13IQ"]) - (int(data[i]["Age13IQ"]) % 5))

def getCSVFromHDF5(filenameHDF5, filenameCSV):
    # La funzione permette di estrapolare le informazioni di un file HDF5 (file molto usati nell'analisi di Big Data)
    # e di salvarle in formato csv da cui poi si potra' creare un dataSet

    # Purtroppo ogni dataSet viene salvato in modo diverso a seconda di chi e' che crea il file HDF5,
    # questa funzione pertanto funziona solo su uno specifico dataSet (carClassifier).

    # Per poter estrarre le informazioni da diversi dataSet e' necessario usare un approccio diverso a seconda
    # della struttura dei GRUPPI
    w = open(filenameCSV, "w")

    if os.path.isfile(filenameCSV):
        print "File already exist! It will be overwritten."
    print "Conversion started!"
    f = h5py.File(filenameHDF5, 'r')

    group = f.get(f.keys()[0])  # Create a group from the first keys, probably data
    data = []
    for i in range(0, len(list(group))):
        data.append(group.get(list(group)[i]))

    tmp = ""
    for i in range(0, len(data[0]) + 1):
        if i == 0:
            for j in range(0, len(group.keys())):
                tmp += group.keys()[j]
                if j != len(group.keys()) - 1:
                    tmp += ","
        else:
            for j in range(0, len(group.keys())):
                tmp += data[j][i - 1]
                if j != len(group.keys()) - 1:
                    tmp += ","
        tmp += "\n"
        sys.stdout.write("\r{0}".format("" + str(i+1) + " of " + str(len(data[0]) + 1)))
        sys.stdout.flush()
    print
    f.close()
    w.write(tmp)
    w.close()
