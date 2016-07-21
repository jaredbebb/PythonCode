name = input("enter file:")
handle = open(name, "r")
text = handle.read()
wordslist = text.split()

#builds a dictionary with key, val pairs
#0 is default value for val, if val does not already have value
testdictionary = dict()
for word in wordslist:
    testdictionary[word] = testdictionary.get(word,0) +1
    
print("This is your dictionary() with key, val pairs:",testdictionary)
 
"""returns the key, val with the highest val 
key, val are just made up names. Not significant
algorithm only returns biggest val that occurs first"""

bigcount = None
bigword = None
for key,val in testdictionary.items():
    if bigcount is None or val > bigcount:
        bigword = key
        bigcount = val

"""TODO make alg return list of the biggest val, if there are several keys with same val
that are the biggest"""
print("This is your biggest key,val:",bigword, bigcount)