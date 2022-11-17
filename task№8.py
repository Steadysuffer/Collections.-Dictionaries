listDict = []
str1 = input()
list1 = str1.split(sep = ", ")
set1 = set(list1)
dict1 = {i: list1.count(i) for i in list1};
sortedDict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse = True))
for items in sortedDict1.items():
    listDict.append(items)
if len(listDict) <= 3:
    for i in range(len(listDict)):
        print(listDict[i][0], listDict[i][1], sep = ": ")
else:
    for i in range(3):
        print(listDict[i][0], listDict[i][1], sep = ": ")
