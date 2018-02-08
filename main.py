from crossValidation import kFoldCrossValidation
from dataManipulation import *
from decimal import *

dataSets = ["nurseryClassifier.csv", "letterClassifier.csv", "carClassifier.csv"]
targetPositions = [9, 2, 7]

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
    with localcontext() as ctx:
        ctx.rounding = ROUND_DOWN
        for i in range(0, len(dataSets)):
            print "DATABASE NUMBER " + str(i + 1) + " : " + dataSets[i]
            test = fiveFoldCrossValidationTest(dataSets[i], targetPositions[i])
            print
            print "Scores with MISCLASSIFICATION : " + Decimal(test[0][0]).quantize(Decimal('0.00001')) + \
                  "  |  Average : " + Decimal(test[1][0]).quantize(Decimal('0.00001'))

            print "Scores with GINI : " + Decimal(test[0][1]).quantize(Decimal('0.00001')) + \
                  "  |  Average : " + Decimal(test[1][1]).quantize(Decimal('0.00001'))

            print "Scores with ENTROPY : " + Decimal(test[0][2]).quantize(Decimal('0.00001')) + \
                  "  |  Average : " + Decimal(test[1][2]).quantize(Decimal('0.00001'))
            print
            print

if __name__ == "__main__":
    mainFunction()