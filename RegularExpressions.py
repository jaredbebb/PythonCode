import re

#Regular expressions

"""you can use re.search() to see if a string matches a regular expresion
similar to find() method for strings

you can use re.findall() to extract portion of your string that match regular
expression"""

#native way of finding and return string
openedfile = open("mbox-short.txt")
for line in openedfile:  
    line = line.rstrip()
    if line.find("From:") >= 0:
        print("This is native way to find the line",line)
 
#regex way of finding and returning string, notice "import re" above
for line in openedfile:  
    line = line.rstrip()
    if re.search("From:", line):
        print("This is regex way to find the line",line)
        
# (^X.*)Matches the start of the line, with X, any character,any number of times
# (^X-\S+:) Matches the start of the line, with X-, any non-white space character, 1 or more times, followed by a colon

#findall() returns a python list
x = "My 2 favorite numbers are 19 and 42a"
y = re.findall("[0-9]+",x)
print(y)

x = "From: Using the : character"
y = re.findall("^F.+:",x)
print("Greedy",y)
#use "?" to make regex not greedy
y = re.findall("^F.+?:",x)
print("Not Greedy",y)

