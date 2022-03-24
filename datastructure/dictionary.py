# dictionary is a collection of data in form of : key-Value
# dictionay is not in order
# dictionay is an index
# dictionary is changeable
# dictionary dows not allow duplicates

# import pprint

myDictionary = {
    "name":"tom",
    "age":30,
    "role":"admin",
    "ID":123456    
}
print (myDictionary)
print(myDictionary["role"])

for key in myDictionary.keys():
    print("%s - %s"%(key,myDictionary[key]))
    
del myDictionary["role"]
print (myDictionary)

del myDictionary
try:
    print(myDictionary)
except NameError:
    print ("dictionary doesn't exist anymore")

# pprint.pprint(myDictionary)