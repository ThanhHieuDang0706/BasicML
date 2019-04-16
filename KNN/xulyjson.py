from __future__ import print_function
import json
import os
articles_loop = 200


with open('articles.json') as json_data:
    # Load JSON
    articles = json.load(json_data)
    print(len(articles), "Articles loaded succesfully")
    # Loop through every article in the json file
    for article in articles:
        # Your code lies here :
        # category = article["Category"]
        # if (category=="Xã hội" or category=="Pháp luật"):``
        #     category = 'thời sự'
        # if (category=="Doanh nghiệp" or category=="Kinh tế"):
        #     category = "Kinh tế"

        if not (os.path.exists(category)):
            os.mkdir(category)

        title = article["Title"]
        content = article["Content"]
        filename = (str) (len([name for name in os.listdir(category) if os.path.isfile(os.path.join(category, name))]))
        text_file = filename + '.txt'

        f = open(text_file, "w+")
        f.write(title + '\n' + content)
        f.close()
        os.system("mv " + text_file + " " + '\"' + category + '\"')


path = os.getcwd()
dirs =  os.listdir(path)
dir_list = []
for i in range(0, len(dirs)):
    temp = path + '/' + dirs[i]
    if os.path.isdir(temp):
        dir_list.append(temp)

for dir in dir_list:
    dir_len = len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))])
    if (dir_len < articles_loop):
        for file in os.listdir(dir):
            file_path = os.path.join(dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(dir)

print("Test git\n")
    #the fuck , is this


        
