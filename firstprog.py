
#variables/expressions
print ("hello world")
x = 120
print(x)
x = x + 2
print(x)
lessthan = "less than"
print (99/100)

#conditionals
if x < 100:
    print(lessthan, x)
else:
    print("x is more than 100, ", x)
    
astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = "astr is not a number"

print ("First", istr)    
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print ("Second", istr)

#functions
def hello():
    print("Hello", " Fun")
hello()

Bob = "Bobby Bouche"
def name(person):
    print("Hi, my name is ",person)
    
name(Bob)

#loops and iterations

friends = ["Joseph", "Glenn", "Sally", "ben", "Joseph", "john"]
for friend in friends:
    print("Happy new year:", friend)
print("done")


