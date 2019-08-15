from collections import Counter 
f = open('path file','r')
data = f.read()
f.close
listData = data.split()
listDataCount = Counter(listData)
print(listDataCount.most_common(5))
print(len(listDataCount.keys()))
