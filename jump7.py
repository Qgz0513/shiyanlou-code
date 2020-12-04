import operator

x = [{'??:': '?'}, {'??': '123456'}, {'??': '1239882214@qq.com'}]
li = {}
for i in x:
    for key, values in i.items():
        li[x.index(i)] = values
print(li)
sorted_x = sorted(li.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_x)
