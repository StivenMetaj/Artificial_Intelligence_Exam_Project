import math

def gain(data, attribute, targetAttribute, functionName):
    # La funzione permette il calcolo dell'information gain di un attributo
    frequencyList = getValuesFrequency(data, attribute)

    # Il seguente ciclo permette il calcolo del secondo termine della formula dell'information gain
    secondTerm = 0.0
    for value in frequencyList.keys():
        tmp = functionName([i for i in data if i[attribute] == value], targetAttribute)
        secondTerm = secondTerm + ((frequencyList[value] / sum(frequencyList.values())) * tmp)

    # Viene ritornato il costo dell'intero dataSet rispetto al target - il termine calcolato precedentemente
    return functionName(data, targetAttribute) - secondTerm

def entropy(data, targetAttribute):
    # La funzione calcola l' entropia di un attributo rispetto al dataSet

    # Essa fa uso del logaritmo ed e' la piu' pesante (delle tre) in termini di computazione anche se
    # in molti casi permette un'accuratezza piu' alta
    frequencyList = getValuesFrequency(data, targetAttribute)
    entropy = 0.0

    for i in frequencyList.values():
        entropy = entropy + (-i / len(data)) * math.log(i / len(data), 2)

    return entropy

def misclassification(data, targetAttribute):
    # La funzione calcola l'errore di classificazione di un attributo rispetto al dataSet

    # Essa e' la piu' veloce (delle tre) ma in molti casi non permette una valutazione precisa
    # quanto quella delle altre due funzioni
    frequencyList = getValuesFrequency(data, targetAttribute)
    maxValue = max(frequencyList.values())
    return 1.0 - maxValue/len(data)

def gini(data, targetAttribute):
    # La funzione calcola l'errore di gini di un attributo rispetto al dataSet

    # Essa e' quella che si preferisce usare dato che non fa uso di logaritmi e nella maggior parte dei
    # casi ha una accuratezza molto vicina a quella dell'entropia
    frequencyList = getValuesFrequency(data, targetAttribute)
    gini = 0.0

    for i in frequencyList.values():
        gini = gini + (i / len(data)) * (1 - (i / len(data)))

    return gini

def getValuesFrequency(data, attribute):
    # La funzione crea un dizionario dove ad ogni possibile valore di attribute viene associato il numero
    # di volte che esso appare
    frequencyList = {}

    for i in data:
        if (frequencyList.has_key(i[attribute])):
            frequencyList[i[attribute]] += 1.0
        else:
            frequencyList[i[attribute]] = 1.0

    return frequencyList
