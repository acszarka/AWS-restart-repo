#declare 3 integars 2,3,4 print them out


a=2
b=3
c=4
print (a)
print (b)
print (c)

# print a, b then 3 on the same line
print ("%d %d %d"%(a,b,c))

# another method to print on the same line
print("{} {} {}".format(a,b,c))

# declare and assign same 3 strings to "hello" print 1 of them out
x = y = z = "Hello"
print (x)

# # declare 3 integars 2,3,4
# # update first to itself + 1
# from pdb import line


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
print ("result=%f"%(result))            #%.3f= number of decimal spots can also increase number of spaces prior to "f" by puting in a whole number prior to the decimal

#########################################
# formating
name ="Tom"
Balance=150.90

# print statement Tom has $balance on the same line

# method 1
print (name+"has $"+str(Balance))

# method 2
print("%s has $%.2f"%(name, Balance))               #printed balance at 2 decimal points
print ("%-20s has $%20.2f"%(name,Balance))          #revers order with 20 spaces

# method 3
print ("{} has ${}".format(name,Balance))
print ("{} has ${:.4f}".format(name,Balance))       #we printed the balance at 4 decimal points
print ("{1} has ${0}".format(name,Balance))         #we swap the order of printing
print ("{:>10} has ${:.4f}".format(name,Balance))   #print balence from right using >
print ("{:<10} has ${:.4f}".format(name,Balance))   #print from left using <
print ("{:^10} has ${:.4f}".format(name,Balance))   #print in middle using ^
print ("{:*^10} has ${:.4f}".format(name,Balance))  #print name in middle useing ^ replacing spaces with *



###########################################
# strings
s="goanna restart 2022 - python"
l = len(s)                                          #determen lenghth of string s
print (s[0])                                        #accessing the first char in s
print (s[l-1])                                      #accessing the last char in s
print (s[7:10])                                     #access sub string on char at index 7 at index 14
print(s[7:])                                        #print from index 7 to the end of s
print (s.lower())                                   #converting  s th lower case
print (s.upper())                                   #convert s to upper care
print (s[7:15].lower())                             #specify substring that you want to convert to lowercase
print (s.count("a"))                                #will count out how many "a" are in the string
print (s.replace("a", "A"))                         #replacing "a" with "A"
print (s.replace("python","Java"))                  #replace substring with another 
print(s.find("p"))                                  #finds the insdex of p
print(s.find ("2022"))                              #finds the starting index of the substring
print(s.isalpha())                                  #check id s is made of letters only
print (s.isdigit())                                 #checks if s is made of numbers only
print (s.isalnum())                                 #checks if s is number and letters