#creating dictionaries

dictionary1 = {'name':'mariana', 'age': 18, 'height': 1.77}

print(dictionary1)
print(dictionary1['age']) #prints dictionary's element "age"

#creating new keys and adding values

dictionary1['programmer'] = True #creating dictionary's element "programmer" and atributting value "True"

dictionary1['height'] = 2 #subscribing a value in the dictionary

#iteration in dictionary

for variable in dictionary1:
    print(variable) #output: each nametag in the dictionary.

for key in dictionary1:
    print(key, dictionary1[key])

#bool in dictionary

print('weight' in dictionary1) #prints false because there isn't that key in the dictionary.
print('height' in dictionary1) #prints true because there is that key in the dictionary.