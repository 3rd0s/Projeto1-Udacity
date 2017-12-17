#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

def testNaN(Numero):
    if Numero=="NaN":
        return True
    else:
        return False

def find_maximo(variavel,data):
    maximo = 0
    for key in data:
        if(testNaN(data[key][variavel])!=True):
            if(maximo < data[key][variavel]):
                maximo=data[key][variavel]
    return maximo

def calc_frac(my_dataset, Person, Divisor, Variavel):
    if(testNaN(my_dataset[Person][Variavel])):
        return "NaN"
    else:
        return my_dataset[Person][Variavel]*1.0/Divisor

def calc_mult(my_dataset,Person):
        if(testNaN(my_dataset[Person]['frac_from_this_person_to_poi']) or testNaN(my_dataset[Person]['frac_from_poi_to_this_person'])):
            return "NaN"
        else:
            return my_dataset[Person]['frac_from_this_person_to_poi']*my_dataset[Person]['frac_from_poi_to_this_person']


### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','bonus','total_payments','expenses', 'total_stock_value','from_poi_to_this_person','from_this_person_to_poi', 'shared_receipt_with_poi','from_messages','to_messages'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)



### Task 2: Remove outliers

del data_dict['TOTAL']

### Task 3: Create new feature(s)
features_list.append('frac_salary')
features_list.append('frac_bonus')
features_list.append('frac_total_payments')
features_list.append('frac_expenses')
features_list.append('frac_total_stock_value')
features_list.append('frac_from_poi_to_this_person')
features_list.append('frac_from_this_person_to_poi')
features_list.append('frac_shared_receipt_with_poi')
features_list.append('multiply_emails')

del features_list[1:11]
### Store to my_dataset for easy export below.
my_dataset = data_dict

MaxSalary=find_maximo("salary",my_dataset)
MaxBonus=find_maximo("bonus",my_dataset)
MaxPayments=find_maximo("total_payments",my_dataset)
MaxExpenses=find_maximo("expenses",my_dataset)
MaxStock=find_maximo("total_stock_value",my_dataset)



for person in my_dataset:
        my_dataset[person]['frac_salary'] = calc_frac(my_dataset,person,MaxSalary,"salary")
        my_dataset[person]['frac_bonus'] = calc_frac(my_dataset,person,MaxBonus,"bonus")
        my_dataset[person]['frac_total_payments'] = calc_frac(my_dataset,person,MaxPayments,"total_payments")
        my_dataset[person]['frac_expenses'] = calc_frac(my_dataset,person,MaxExpenses,"expenses")
        my_dataset[person]['frac_total_stock_value'] = calc_frac(my_dataset,person,MaxStock,"total_stock_value")
        my_dataset[person]['frac_from_poi_to_this_person'] = calc_frac(my_dataset,person,my_dataset[person]['to_messages'],"from_poi_to_this_person")
        my_dataset[person]['frac_from_this_person_to_poi'] = calc_frac(my_dataset,person,my_dataset[person]['from_messages'],"from_this_person_to_poi")
        my_dataset[person]['frac_shared_receipt_with_poi'] = calc_frac(my_dataset,person,my_dataset[person]['to_messages'],"shared_receipt_with_poi")
        my_dataset[person]['multiply_emails'] = calc_mult(my_dataset,person)


### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)
### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.decomposition import PCA

clf=make_pipeline(PCA(n_components=4),SVC(kernel='rbf',C=40000,gamma='auto'))
#clf2 = GridSearchCV(clf, parameters)
#clf2.fit(features,labels)
### Task 5: Tune your classifier to achieve better than .3 precision and recall
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info:
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
from sklearn.metrics import precision_score, accuracy_score, recall_score
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

clf.fit(features_train,labels_train)
print precision_score(labels_test,clf.predict(features_test)), accuracy_score(labels_test,clf.predict(features_test)), recall_score(labels_test,clf.predict(features_test)),
### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
