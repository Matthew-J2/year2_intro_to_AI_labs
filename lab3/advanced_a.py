"""stuff to reference
https://scikit-learn.org/stable/modules/tree.html#classification
https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.fit
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits
https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree
"""
from sklearn import tree
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
wine = load_wine()
samples, labels = wine.data, wine.target
decision_tree = tree.DecisionTreeClassifier(max_depth=4, criterion="entropy" )
decision_tree = decision_tree.fit(samples, labels)
plt.figure(figsize=(100,100))
tree.plot_tree(decision_tree, feature_names=wine.feature_names, fontsize=13)
plt.show()
