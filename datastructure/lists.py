#!/bin/python
# List in python is a collection of data of diffrent types
# list is ordered
# list is indexed
# list is changeable
# list allows duplicates


myList = ["Tom", 30, 255.80]                #creating a list
List2 = list(["bank", "account"])           #creating a list
print (myList)                              #print list
print (myList[0])                           #accessing first element
l = len(myList)                             #calculate length of list
print ("length is "+str(1))

#############################################

print (myList[l-1])                         #accessing last element of list
print(myList[1:l])                          #accessing all elements from 1 until length-1

# Modify list
myList.insert(2,"has")                      #inserting element at index 
myList.append("$")                          #adds element to the end of the list
print (myList)

myList [l-1] = "dollars"                  #changes an element at a posistion
print (myList)

myList[0] = "Lucy"
print (myList)


myList.pop(1)                               #remove element by index
print (myList)


myList.pop()                                #removes last element
print(myList)

newlist = myList + List2                    #combines lists
print (newlist)


del myList                                  #deletes list



try:                                            #reads error but will contin
    print (myList)
except NameError:
    print ("The list no longer exists.")
print ("Thank you")


mylist = list(range(1,80))                      #creates sequental list  
print (mylist)

element = int(input("find:"))

if (mylist.index(element)):                          #find the number then replace the number with word
    mylist[mylist.index(element)] = "element found"
print (mylist)
 



