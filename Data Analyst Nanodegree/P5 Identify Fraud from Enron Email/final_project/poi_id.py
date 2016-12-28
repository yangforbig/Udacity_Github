import sys
import pickle
sys.path.append("../tools/")
import numpy as np
import pandas as pd
from feature_format import featureFormat, targetFeatureSplit
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.svm import SVC

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)


financial_features = ['salary', 'deferral_payments', 'total_payments',
                      'loan_advances', 'bonus', 'restricted_stock_deferred',
                      'deferred_income', 'total_stock_value', 'expenses',
                      'exercised_stock_options', 'other', 'long_term_incentive',
                      'restricted_stock', 'director_fees']
email_features =  ['to_messages', 'from_poi_to_this_person',
                    'from_messages', 'from_this_person_to_poi',
                    'shared_receipt_with_poi']

all_features = financial_features + email_features


### Task 2: Remove outliers
data_dict.pop('TOTAL')
data_dict.pop('BELFER ROBERT')
data_dict.pop('BANNANTINE JAMES M')

### Task 3: Create new feature(s)
### select the features are numerical and have less NA(less than 70)
my_feature = ['poi', 'total_stock_value',
              'salary', 'expenses',
              'other', 'to_messages', 'shared_receipt_with_poi', 'from_messages',
              'from_poi_to_this_person', 'from_this_person_to_poi', 'bonus']

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing

data = featureFormat(my_dataset, my_feature, sort_keys = True)
labels, features = targetFeatureSplit(data)



# feature scale first
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scale_features = scaler.fit_transform(features)


#use SelectPercentile to improve feature selection
from sklearn.feature_selection import SelectPercentile, f_classif
selector = SelectPercentile(f_classif, percentile=50)
selector.fit(scale_features, labels)
SP_features = []
for e in range(len(selector.get_support())):
    if  selector.get_support()[e] == True:
        SP_features.append(my_feature[1:][e])
print "SelectPercentile features: ", SP_features

#updated myfeature
def get_data(features_list, full_data):
    data = featureFormat(full_data, features_list, sort_keys = True)
    labels, features = targetFeatureSplit(data)
    return features, labels

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

'''
Decision Tree, Knearnest neighour and Naive Bayes will be used in this project. Becasue, from the plots before, we can see
there are lot of noise points in this skewed dataset, so SVM is not good choice for this case. PCA is good for feature reduction.
But in this case, a financial fraud detection, model explanation is more intuitive and important than the model accuracy.
PCA will transform the features and the new features are hard to interpret. Decision Tree is the first choice and
good for this uniquely small dataset, even though it would take a risk of overfitting. An overfitting model for this particular case is
quite resonable, since the fraud is second to none in American history. Knearest neighours and Naive Bayes would be served as a comparation to
Decsion Tree method.
'''
## DecisionTree

def DecisionTree_clf(train, label):
    print "Training Decsion Tree: \n........"
    tree_clf = DecisionTreeClassifier(random_state=10)
    param_grid = [{'max_features':[2,3],
                   'class_weight':['balanced', None],
                   'criterion':['gini','entropy']}]
    score = 'recall'

    print 'Tuning hyperparameters for %s' % score
    cv = StratifiedShuffleSplit(n_splits=1000, test_size=0.1, random_state=0)
    clf = GridSearchCV(tree_clf, param_grid, scoring='%s_macro' % score, cv=cv)
    clf.fit(train, label)
    print 'Best parameters set found on development set:\n '
    print clf.best_params_
    print "Detailed classification report: "
    print pd.DataFrame(clf.cv_results_)


    #fi = clf.feature_importances_
    #feature_importance = zip(features, fi)sa
    #print features_importance
    return clf.best_estimator_


features, labels = get_data(['poi']+SP_features, my_dataset)
# Decision Tree
tree_clf = DecisionTree_clf(features, labels)
print 'Best Tree: '
print tree_clf
print 'feature importances in the best tree: '
importances = tree_clf.feature_importances_
print zip(SP_features, importances)
print "The number of features when tree is performed: "
print tree_clf.n_features_




'''
the importance of feature 'from_poi_to_this_person' and 'salary' are the two most irrelevant features.
So, take them away from the feature list and train the tree again
'''
# Retrain Decison Tress
SP_features.remove('shared_receipt_with_poi')
SP_features.remove('salary')
features, labels = get_data(['poi']+SP_features, my_dataset)
tree_clf = DecisionTree_clf(features, labels)
print 'Best Tree: '
print tree_clf
print 'feature importances in the best tree: '
importances = tree_clf.feature_importances_
print zip(SP_features, importances)
print "The number of features when tree is performed: "
print tree_clf.n_features_


'''
For model evaluation, recall and precision methods are applied, especially the higher recall of the model, the better detection for the fraud demeanour. Becasue
we want the false negative rate as few as possible, we don't want the crimials neglected.
'''

# decision tree graph
import pydotplus
from sklearn import tree
dot_data = tree.export_graphviz(tree_clf, out_file=None,
                         feature_names=SP_features,
                         class_names=['1', '0'],
                         filled=True, rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('Enrontreegraph.pdf')

# Use Gaussian Naive Bayes
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
def GaussianNB_clf(features, labels):
    print "Training Naive Bayes \n ......."
    clf = GaussianNB()
    param_grid = [{'priors':[None]}]
    score = 'recall'
    print 'Tuning hyperparameters for %s' % score
    cv = StratifiedShuffleSplit(n_splits=1000, test_size=0.1, random_state=0)
    clf = GridSearchCV(clf, param_grid, scoring='%s_macro' % score, cv=cv)
    clf.fit(features, labels)
    print 'Best parameters set found on development set:\n '
    print clf.best_params_
    print "Detailed classification report: "
    print pd.DataFrame(clf.cv_results_)
    return clf.best_estimator_
GNB_clf = GaussianNB_clf(features, labels)

# Knearest neighbours
# logarithmic transformation
def log_data(features):
    for entry in features:
        for e in range(len(entry)):
            if entry[e] !=0:
                entry[e] = np.log(entry[e])
    return features


def KN_clf(train, label):
    print "Traning KNearest neighbours classifier: \n........"
    KN_clf = KNeighborsClassifier()
    param_grid = [{'n_neighbors':[3,4,5,6,7,8],
                   'algorithm':['auto']}]
    score = 'recall'
    print 'Tuning hyperparameters for %s' % score
    cv = StratifiedShuffleSplit(n_splits=1000, test_size=0.1, random_state=0)
    clf = GridSearchCV(KN_clf, param_grid, scoring='%s_macro' % score, cv=cv)
    clf.fit(train, label)
    print 'Best parameters set found on development set:\n '
    print clf.best_params_
    print "Detailed classification report: "
    print pd.DataFrame(clf.cv_results_)
    return clf.best_estimator_

log_features = log_data(features)
KNeighbors_clf = KN_clf(log_features, labels)
#Support Vector Machine
def SVM_clf(train, label):
    print "Training SVM classifier: \n........"
    svm_clf = SVC()
    param_grid = [{'C':[0.1,1,5,10,100,500,1000],
                   'kernel':['rbf'],
                   'gamma':[0.005, 0.01, 0.1]}]
    score = 'recall'
    print 'Tuning hyperparameters for %s' % score
    cv = StratifiedShuffleSplit(n_splits=1000, test_size=0.1, random_state=0)
    clf = GridSearchCV(svm_clf, param_grid, scoring='%s_macro' % score, cv=cv)
    clf.fit(train, label)
    print 'Best parameters set found on development set:\n '
    print clf.best_params_
    print "Detailed classification report: "
    print pd.DataFrame(clf.cv_results_)
    return clf.best_estimator_

svm_clf = SVM_clf(features, labels)
### Task 5: Tune your classifier to achieve better than .3 precision and recall
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info:
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.



def dump_classifier_and_data(clf, dataset, feature_list):
    CLF_PICKLE_FILENAME = ["tree_clf.pkl", "GNB_clf.pkl", "KNeighbors_clf.pkl", "svm_clf.pkl"]
    DATASET_PICKLE_FILENAME = "my_dataset.pkl"
    FEATURE_LIST_FILENAME = "SP_features.pkl"
    for filename in CLF_PICKLE_FILENAME:
        try:
            eval(filename[:-4])
        except:
            continue
        if eval(filename[:-4]) == clf:
            with open(filename, "w") as clf_outfile:
                pickle.dump(clf, clf_outfile)
    with open(DATASET_PICKLE_FILENAME, "w") as dataset_outfile:
        pickle.dump(dataset, dataset_outfile)
    with open(FEATURE_LIST_FILENAME, "w") as featurelist_outfile:
        pickle.dump(feature_list, featurelist_outfile)


clf_list = [tree_clf, GNB_clf, KNeighbors_clf, svm_clf]
for clf in clf_list:
    dump_classifier_and_data(clf, my_dataset, ['poi']+SP_features)
