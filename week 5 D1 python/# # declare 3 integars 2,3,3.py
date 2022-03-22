# # declare 3 integars 2,3,4
# # update first to itself + 1
# from pdb import line_prefix


# update the second to itself  +2
# update the thirsd to itself +1
# show all integers on the same line
# compute the following opperations:
# first integer to the power of 2
# print the total of: (first+second)*(second-thrid)/(first+1)

x=2
y=3
z=4
x+=1
y+=2
z+=1
print ("x={}; y={}; z={}".format(x,y,z))
print  (x**2)
print (pow(x,2))
result= (x+y)*(x-z)/(x+1)
print ("result=%f"%(result))#%.3f= number of decimal spots can also increase number of spaces prior to "f" by puting in a whole number prior to the decimal

#########################################
# formating
name ="Tom"
Balance=150.90

# print statement Tom has $balance on the same line

# method 1
print (name+"has $"+str(Balance))

# method 2
print("%s has $%.2f"%(name, Balance))#printed balance at 2 decimal points
print ("%-20s has $%20.2f"%(name,Balance))#revers order with 20 spaces

# method 3
print ("{} has ${}".format(name,Balance))
print ("{} has ${:.4f}".format(name,Balance))#we printed the balance at 4 decimal points
print ("{1} has ${0}".format(name,Balance))#we swap the order of printing
print ("{:>10} has ${:.4f}".format(name,Balance))#print balence from right using >
print ("{:<10} has ${:.4f}".format(name,Balance))#print from left using <
print ("{:^10} has ${:.4f}".format(name,Balance))#print in middle using ^
print ("{:*^10} has ${:.4f}".format(name,Balance))#print name in middle useing ^ replacing spaces with *



###########################################
# strings
s="goanna restart 2022 - python"
l = len(s) #determen lenghth of string s
print (s[0])#accessing the first char in s
print (s[l-1])#accessing the last char in s
print (s[7:10])#access sub string on char at index 7 at index 14
print(s[7:]) #print from index 7 to the end of s
print (s.lower())#converting  s th lower case
print (s.upper())#convert s to upper care
