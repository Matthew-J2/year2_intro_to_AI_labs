from sklearn import tree
from sklearn.datasets import load_digits
import matplotlib
digits = load_digits()
samples, labels = digits.data, digits.target
decision_tree = tree.DecisionTreeClassifier()
decision_tree = decision_tree.fit(samples, labels)
tree.plot_tree(decision_tree)

"""stuff to reference
https://scikit-learn.org/stable/modules/tree.html#classification
https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.fit
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits
https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree

#import graphviz
from sklearn import tree
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
wine = load_wine()
samples, labels = wine.data, wine.target
decision_tree = tree.DecisionTreeClassifier(max_depth=4, criterion="entropy" )
decision_tree = decision_tree.fit(samples, labels)
plt.figure(figsize=(100,100))
tree.plot_tree(decision_tree, feature_names=wine.feature_names, fontsize=60)

plt.show()

""""""dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("digits") 
dot_data = tree.export_graphviz(clf, out_file=None, 
                      feature_names=digits.feature_names,  
                      class_names=digits.target_names,  
                      filled=True, rounded=True,  
                      special_characters=True)  
graph = graphviz.Source(dot_data)"""
""""""