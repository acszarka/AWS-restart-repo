# SETS
# St is a collection of data of any type
# set is unordered
# set is un-indexed
# set is changable
# set is unique, it cannot have/allow duplicates

mySet = {"AWS", "Restart", 2022, "week 5"}          #creating a set
print (mySet)                                       #when pprinting the order of the elements the order is randomized

mySet.add ("python")                                #adds an element to set
print (mySet)

mySet.update (["March", 22])                        #add multiple elements using update
print (mySet)

mySet.remove ("python")                             #deleting by name
print (mySet)

mySet.discard("Restart")                             #deleting by name
print (mySet)

mySet.pop ()                                         #remove last element from ranomly organised set
print (mySet)

set2 = {"cohort", 9}                                  #join 2 sets
newset = mySet.union(set2)
print (newset)

newset.add(9)                                         #wont be added because there is one already
print (newset)