from crossValidation import kFoldCrossValidation
from dataManipulation import *

# print createDecisionTree(data, attributes, targetAttribute, 0)
# print createDecisionTree(data, attributes, targetAttribute, 1)
# print createDecisionTree(data, attributes, targetAttribute, 2)

dataSets = ["carClassifier.csv"]
targetPositions = [2]

def fiveFoldCrossValidationTest(CSVDataSet, targetPosition):
    data, attributes, targetAttribute = getInfoFromCSV(CSVDataSet, targetPosition)

    tmp = []
    tmp.append(kFoldCrossValidation(data, attributes, targetAttribute, 0, 5))
    tmp.append(kFoldCrossValidation(data, attributes, targetAttribute, 1, 5))
    tmp.append(kFoldCrossValidation(data, attributes, targetAttribute, 2, 5))

    return tmp

def mainFunction():
    for i in range(0, len(dataSets)):
        print "DATABASE NUMBER " + str(i + 1) + " : " + dataSets[i]
        scores = fiveFoldCrossValidationTest(dataSets[i], targetPositions[i])
        print
        print "Score with MISCLASSIFICATION : " + str(scores[0])
        print "Score with GINI : " + str(scores[1])
        print "Score with ENTROPY : " + str(scores[2])
        print
        print

if __name__ == "__main__":
    mainFunction()