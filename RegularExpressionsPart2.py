import re
#Regular Expressions Part II

x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("^From \S+@\S+",x)
print("Match if From is at the beginning of line, non white space, @, non white space:",y)

#Match @, match non-blank character, any number of non blank characters
#"[^ ]", ^ in this context means do no not match, not look at the beginning of the line.
y = re.findall("@([^ ]*)", x)
print("Match @, match non-blank character, any number of non blank characters:",y)