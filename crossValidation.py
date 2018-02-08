from decisionTree import *
import time

def kFoldCrossValidation(data, attributes, targetAttribute, impurity, k):
    # La funzione esegue per k volte una cross validation con trainset e testset sempre diversi
    numberExamples = len(data)
    totalScoreAverage = 0.0
    scores = []

    print str(k) + "-Fold Cross Validation (with impurity type = " + str(impurity) + ") is starting ..."

    for i in range(0, k):
        sys.stdout.write("\r{0}".format("Test number " + str(i + 1) + " of " + str(k) + " ..."))
        sys.stdout.flush()
        time.sleep(0.15)

        # Si inizializzano le variabili
        tmpScore = 0.0
        trainSet = data[:]
        testSet = []
        tmp = []

        # I seguenti cicli permettono di non avere mai train e test uguali
        for j in range(0, i*numberExamples/k):
            tmp.append(trainSet.pop(0))
        trainSet.extend(tmp)

        for j in range(0, numberExamples/k if i != k-1 else (numberExamples/k)+numberExamples % k):
            testSet.append(trainSet.pop(0))

        # Si crea l'albero di decisione usando il trainset
        tree = createDecisionTree(trainSet, attributes, targetAttribute, impurity, None)

        # Si calcola lo score dell'albero in base ai dati del testset
        for j in testSet:
            if getTargetValue(tree, j) is not None:
                tmpScore = tmpScore + 1.0

        tmpScore = tmpScore / len(testSet)
        totalScoreAverage = totalScoreAverage + tmpScore
        scores.append(tmpScore)
        sys.stdout.write("\r{0}".format("Test number " + str(i + 1) + " of " + str(k) + " finished!"))
        sys.stdout.flush()

    print
    return scores, totalScoreAverage/k

def getTargetValue(tree, line):
    # La funzione controlla se il tipo dell'albero e' una stringa. Se cosi' non e' vuol dire che non siamo arrivati
    # ad una foglia e che bisogna continuare la visita dell'albero.
    if type(tree) == type("string"):
        return tree
    else:
        attribute = tree.keys()[0]
        # Se il valore di attribute non viene trovato nel sotto albero la funzione ritorna None in modo da indicare
        # al livello superiore che l'albero non riesce a trovare una soluzione per line
        if line[attribute] not in tree[attribute].keys():
            return None
        else:
            t = tree[attribute][line[attribute]]

        return getTargetValue(t, line)