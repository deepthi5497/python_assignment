# fh=open("input","r")
# print fh.read(5)
# for i in fh:
#     print(i)
# print fh.readlines()
# fh=open("output","w")
# fh.write("this will add to the file")
# fh=open("input","a")
# fh.write("this will add to the file")
# fh=open("input","r")
# print fh.read()
# import csv
#
# with open('writeData.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     #way to write to csv file
#     writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
#     writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
#     writer.writerow(['Java', 'James Gosling', '1995', '.java'])
#     writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])
# import csv
# with open('players.csv', 'w') as file:
#     fieldnames = ['player_name', 'fide_rating']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
#     writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
#     writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
# import json
#
# data = {}
# data['people'] = []
# data['people'].append({
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })
#
# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)
# import json
#
# with open('data.txt') as json_file:
#     data = json.load(json_file)
#     for p in data['people']:
#         print('Name: ' + p['name'])
#         print('Website: ' + p['website'])
#         print('From: ' + p['from'])
#         print('')

# Python program showing
# use of json package

# import json
#
# # {key:value mapping}
# a = {"name": "John",
#      "age": 31,
#      "Salary": 25000}
#
# # conversion to JSON done by dumps() function
# b = json.dumps(a)
#
# # printing the output
# print(b)
# import json
# var = {
#       "Subjects": {
#                   "Maths":85,
#                   "Physics":90
#                    }
#       }
# with open("Sample.json", "w") as p:
#     print json.dumps(var, p)
with open("input","r")as f:
    words=f.read().split("\n")
    max_length=0
    longest=" "
    for word in words:
       for a in word.split(" "):
           if len(a)>max_length:
                max_length=len(a)
                longest=a
    print max_length,longest
# def longestWordLength(string):
#     length = 0
#
#     for word in string.split():
#         if (len(word) > length):
#             length = len(word)
#
#     return length,word
# string = "I am an intern at geeksforgeeks"
# print(longestWordLength(string))
