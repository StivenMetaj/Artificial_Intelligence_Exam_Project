from crossValidation import kFoldCrossValidation
from dataManipulation import *

# nursery 9, letter 2, car 7, poker 11

dataSets = ["pokerHandClassifier.csv"]
targetPositions = [11]

def fiveFoldCrossValidationTest(CSVDataSet, targetPosition):
    data, attributes, targetAttribute = getInfoFromCSV(CSVDataSet, targetPosition)

    scores = []
    averageScores = []

    misclassification = kFoldCrossValidation(data, attributes, targetAttribute, 0, 5)
    gini = kFoldCrossValidation(data, attributes, targetAttribute, 1, 5)
    entropy = kFoldCrossValidation(data, attributes, targetAttribute, 2, 5)

    scores.append(misclassification[0])
    scores.append(gini[0])
    scores.append(entropy[0])

    averageScores.append(misclassification[1])
    averageScores.append(gini[1])
    averageScores.append(entropy[1])

    return scores, averageScores

def mainFunction():
    for i in range(0, len(dataSets)):
        print "DATABASE NUMBER " + str(i + 1) + " : " + dataSets[i]
        test = fiveFoldCrossValidationTest(dataSets[i], targetPositions[i])
        print
        print "Scores with MISCLASSIFICATION : " + str(test[0][0]) + "  |  Average : " + str(test[1][0])
        print "Scores with GINI : " + str(test[0][1]) + "  |  Average : " + str(test[1][1])
        print "Scores with ENTROPY : " + str(test[0][2]) + "  |  Average : " + str(test[1][2])
        print
        print

if __name__ == "__main__":
    mainFunction()