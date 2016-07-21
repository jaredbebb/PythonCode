import urllib.request
webpage =urllib.request.urlopen("http://www.py4inf.com/code/romeo.txt")

wordcount = dict()

for line in webpage:
    words = line.split()
    for word in words:
        wordcount[word] = wordcount.get(word,0) +1
print("This is your dictionary() with key, val pairs:",wordcount)
 
"""returns the key, val with the highest val 
key, val are just made up names. Not significant
algorithm only returns biggest val that occurs first"""

bigcount = None
bigword = None
for key,val in wordcount.items():
    if bigcount is None or val > bigcount:
        bigword = key
        bigcount = val

"""TODO make alg return list of the biggest val, if there are several keys with same val
that are the biggest"""
print("This is your biggest key,val:",bigword, bigcount)
