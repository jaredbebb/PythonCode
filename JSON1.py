import json

#data is formatted as JSON
data = '''{
"name": "Chuck",
"phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
    },
    "email" : {
    "hide" : "yes"
    }
}'''
#makes a list called "info"
info = json.loads(data)
print ('Name:', info["name"])
print('Hide:', info["email"]["hide"])