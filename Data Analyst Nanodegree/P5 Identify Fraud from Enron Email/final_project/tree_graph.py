'''
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

# export graph

with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

'''

import pydotplus
