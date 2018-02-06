from impurityIndexes import *
import sys

def createDecisionTree(data, attributes, targetAttribute, impurity, parentData):
    vals = [i[targetAttribute] for i in data]

    # Se il dataset e' vuoto o non ci sono attributi oltre a quello target si ritorna il valore di target
    # ripetuto piu' volte
    if not data:
        return pluralityValue(parentData, targetAttribute)
    elif (len(attributes) - 1) <= 0:
        return pluralityValue(data, targetAttribute)

    # Se il valore di target sono tutti uguali non c0e' bisogno di continuare la produzione di sottoalberi
    # e si ritorna il primo valore della lista vals
    elif vals.count(vals[0]) == len(vals):
        return vals[0]

    # Se non siamo nei casi precedenti si effettua la ricerca del miglior attributo con importance
    # e si crea un sotto albero per ogni valore di bestAttribute
    else:
        bestAttribute = importance(data, attributes, targetAttribute, impurity)
        tree = {bestAttribute:{}}

        tmp = []
        for i in data:
            if tmp.count(i[bestAttribute]) != 1:
                tmp.append(i[bestAttribute])

        for i in tmp:
            subAttributes = [attr for attr in attributes if attr != bestAttribute]
            exs = getSubDataset(data, bestAttribute, i)
            subtree = createDecisionTree(exs, subAttributes, targetAttribute, impurity, data)

            tree[bestAttribute][i] = subtree

    return tree

def pluralityValue(data, targetAttribute):
    # La funzione ritorna il valore ripetuto piu' volte di targetAttribute
    vals = [i[targetAttribute] for i in data]
    maxFreq = 0
    mostFrequentlyValue = None

    # Il seguente ciclo permette di avere una lista di valori non ripetuti
    tmp = []
    for i in data:
        if tmp.count(i[targetAttribute]) != 1:
            tmp.append(i[targetAttribute])

    for i in tmp:
        if vals.count(i) > maxFreq:
            maxFreq = vals.count(i)
            mostFrequentlyValue = i

    return mostFrequentlyValue

def importance(data, attributes, targetAttribute, impurity):
    # La funzione determina dato un attributo target, un insieme di attributi e un dataset
    # qual'e' l'attributo oon information gain maggiore (in base all'impurita' scelta)

    # Il gain viene inizializzato a -1 perche' in alcuni casi, con impurita' come l'errore di
    # classificazione tutti gli attributi hanno gain pari a 0
    bestGain = -1.0
    bestAttribute = None
    if impurity not in [0, 1, 2]:
        impurity = 2

    # Per ogni attributo chiamo il metodo di calcolo del gain in base all'impurita'
    for i in attributes:
        sys.stdout.write("\r{0}".format("Calculating gain of " + str(i)))
        sys.stdout.flush()
        if impurity == 0:
            tmpGain = gain(data, i, targetAttribute, misclassification)
        elif impurity == 1:
            tmpGain = gain(data, i, targetAttribute, gini)
        elif impurity == 2:
            tmpGain = gain(data, i, targetAttribute, entropy)

        # Se il gain trovato e' maggiore del massimo precedente salvo il valore e il relativo attributo
        if tmpGain >= bestGain and i != targetAttribute:
            bestGain = tmpGain
            bestAttribute = i

    return bestAttribute

def getSubDataset(data, attribute, value):
    # La funzione cerca tra i record di data quelli che hanno un certo valore per un certo attributo
    subDataset = []

    for i in data:
        if i[attribute] == value:
            subDataset.append(i)

    # Viene ritornao il subDataset usato per la creazione di un sotto albero
    return subDataset