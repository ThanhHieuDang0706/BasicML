import numpy as np # Thư viện dùng để xử lý
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split  
import os
from sklearn.metrics import accuracy_score

articles_loop = 200
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
    lists = [dir + '/' + str(i) + '.txt' for i in range(0, articles_loop)]
    for l in lists:
        fileList.append(l)
    for i in range(0, articles_loop):
        Y.append(labels[temp])
    temp += 1

# print(len(fileList))
# print(len(Y))
# print(Y)
vectorizer = TfidfVectorizer(input="filename")
X = vectorizer.fit_transform(fileList).toarray()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15,random_state=10)

print("Training size: " + (str)(len(X_train)))
print("Test size : " + (str)(len(X_test)))

n = 11

neigh = KNeighborsClassifier(n_neighbors=n,p=2, weights='distance',n_jobs=4)
neigh.fit(X_train, Y_train)
Y_predict = neigh.predict(X_test)
accuracy = accuracy_score(Y_test, Y_predict)
print("Accuracy of ", n,"-NN : " ,accuracy * 100 , "%")

# print('\n')
# in ra mot vai ket qua
# print('Predicted labels: ', Y_predict[20:30])
# print('Ground truth : ', Y_test[20:30])
# Testing using GitHub
# Test again 

# Testing using GitHub 
# Test2



