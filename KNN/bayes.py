from collections import Counter

from sklearn.datasets import load_files
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split  
import os
# from imblearn.under_sampling import RandomUnderSampler
# from imblearn.pipeline import make_pipeline as make_pipeline_imb
# from imblearn.metrics import classification_report_imbalanced

# Loading Data
articles_per_category = 200
path = os.getcwd()
dirs =  os.listdir(path)
dir_list = []
labels = []
for i in range(0, len(dirs)):
    temp = path + '/' + dirs[i]
    if os.path.isdir(temp):
        dir_list.append(temp)
        # print(temp)
        labels.append(dirs[i])

fileList = []
Y = []


# print(labels)
temp = 0
for dir in dir_list:
    if (dir == "/hdd1/basicMachineLearning/Baitap/.git"):
        continue
#     dir_len = len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))])
    lists = [dir + '/' + str(i) + '.txt' for i in range(0, articles_per_category)]
    for l in lists:
        fileList.append(l)
    for i in range(0, articles_per_category):
        Y.append(labels[temp])
    temp += 1

vectorizer = TfidfVectorizer(input="filename")
X = vectorizer.fit_transform(fileList).toarray()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,random_state=10)

bayes = MultinomialNB()
bayes.fit(X_train, Y_train)

Y_pred = bayes.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of Naive Bayes : " ,accuracy * 100 , "%")

# print(classification_report_imbalanced(Y_test, Y_pred))
