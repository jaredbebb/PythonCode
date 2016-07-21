# Chapter 6 Strings

fruit = "banana"
letter = fruit[0]
print("letter at 0 is",letter)

index = 0
while index <len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index +1
    
for letter in fruit:
    print(letter)

s = "Monty Python"
print(s[0:4])

a = "Hello"
b = a + " There"
print(b)

print("Is there an n in fruit?", "n" in fruit)

#Chapter 7 - Files
#opens file and counts lines
mboxfile = "mbox-short.txt"
def linecount(file):
    fhand = open(file)
    count = 0
    for line in fhand:
        count = count + 1
    print("Line Count: ", count)
    
print(linecount(mboxfile))

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("that file is not in the current directory:", fname)

for line in fhand:
    line = line.rstrip()
    if line.startswith("From"):
        print(line)
        
