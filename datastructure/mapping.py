# read file name from standard input
# map the data to a dictionary

import csv
import pprint as pp
from textwrap import indent
from turtle import width

filename = input("file: ")                      #input() reads user value from standard input as string

file = csv.DictReader(open(filename))           #opens file by name and csv.dictreader map it to file

myDictionary = []                               #empty list because of square brackets

for line in file:                               #reads linnes from file until the end of the file and add line to the list
    myDictionary.append(line)
    
    
print (myDictionary)
pp = pprint.PrettyPrinter(indent=2,width=40) #setup pretty print data width to 40 indentation to 2 spaces
pp.pprint(myDictionary)