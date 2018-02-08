# Artificial_Intelligence_Exam_2018
A python application that permits to show differences between different impurity indexes in decision trees.

# How to use
The application runs in "main.py" and when it starts "mainFunction()" is called. "mainFunction" in turn calls "fiveFoldCrossValidationTest" on "dataSets" and "targetPositions" elements.

So, to use the app with your datasets, you must insert in "dataSets" your CSV files and in "targetPositions" the positions of your target attributes.

In particular 2 observations:
* the first row of your datasets must be the attributes list
* indexes in "targetPositions" are human-friendly (if you have n attributes, the index must be a number from 1 to n).

# References
Thanks to [Christopher Roach](http://www.oreilly.com/pub/au/1904 "Christopher Roach oreilly page") and his [article](http://archive.oreilly.com/pub/a/python/2006/02/09/ai_decision_trees.html) for helping me to understand better decision trees and data structures behind them.

Thanks also to [Stack Overflow](https://stackoverflow.com/) for having always a solution for any problem.