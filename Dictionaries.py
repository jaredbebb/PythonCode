#Chapter 9 Dictionaries

#making a new dictionary/hashtable
#syntax 
#   hashtable name = dict()
#   hashtable name @[key] = value

purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75
print(purse)
print("Purse:candy = ", purse["candy"])

purse["candy"] = purse["candy"] +2

print(purse)

#another way to make a new dictionary
jjj = {"Chuck":1, "Fred":42, "Jan":100}
print(jjj)

#making a blank dictionary
ooo = {}
print(ooo)

#adding "hashes" to values

ccc = dict()
ccc["csev"] = 1
ccc["cwen"] = 1

ccc["cwen"] = ccc["cwen"] +1
print(ccc)

#adding array elements to hashtable and adding total count to hashtable
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for i in names:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] = counts[i] +1
print(counts)

#pattern of checking to see if key is already in a dictionary, method called get() that does that for us
thename = "fdsafsaf"
if thename in counts:
    print(counts[thename])
else:
    print(0)
print("The name has ' ' value:", counts.get(thename,0))

#can use get() and provide a default value of zero whwen the key is not yet in the dictionary, and then add just one
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for i in names:
    counts[i] = counts.get(i,0) +1
print("these are the counts elements",counts)

sentence = input()
sentarr = sentence.split()
sentcount = dict()
for i in sentarr:
    sentcount[i] = sentcount.get(i,0) +1
print("this is a hash of the sentences", sentcount)
