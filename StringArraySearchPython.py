#linear search of string array using python

greeting = "Hi! My name is Jared. Welcome to this python test."
stringArr = greeting.split(" ")
word = "Jared"

def stringSearch(sArray, search):
    for i in sArray:
        if(sArray[i] == search):
            print("Found the string! Its at", i)
        else:
            i+1
  
numsearch(stringArr, word)