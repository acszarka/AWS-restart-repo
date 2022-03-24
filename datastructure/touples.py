# tuple is a collection of data of any type
# tuple is ordered
# tuple is indexed
# tuple is unchangable
# tuple allows duplicates

myTuple = ("Tom", 30, 10.5)             #once the touple is created it cannot be changed(can't add or delete)
print (myTuple)
print (myTuple[0])
print (myTuple[len(myTuple)-1])

tuple2 = tuple(("dollars"))
newtuple = myTuple + tuple2             #joining 2 tuples
print (newtuple)




del myTuple

try:
    print (myTuple)
except NameError:
    print ("tuple doesn't exist")

print (myTuple)