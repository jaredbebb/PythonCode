#File + hashmap

rawinput = input()
try:
    file = open(rawinput,"r")
except:
    print("not a file or directory")
list = file.read()
splitlist = list.split()

sentcount = dict()
for i in splitlist:
    sentcount[i] = sentcount.get(i,0) +1
  
#Print hashmap
print("this is a hash of the file, line by line", sentcount)

#print list(like the tuples) of hashmap
print("Print list of hashmap",sentcount.items())