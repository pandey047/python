# 1.Find number is prime or not.
'''
num=6
for i in range(2,num):
	if num%i==0:
		print(num,"is prime not prime")
		break
else:
    print(num,"is prime")

'''

# 2.Given n lenght of character ,print only last 4 character only and remaining character shuold be *
'''
num=123456789
def card(num):
    num=str(num)
    lstart=num[4:len(num)]
    lstart=len(lstart)
    lend=num[:-(len(num)-4)]
    # print(lstart)
    # print(lend)
    lstart="*"*lstart
    print(lstart+lend)
card(9876543210987)
'''

# 3.Print how many character in a string 
# ex---> "umesh"==u-1,m-1,e-1,s-1,h-1
# With help of for loop
'''
def characterCount(var):
    d1={}
    for i in var:
        d1[i]=var.count(i)
    print(d1)
    
characterCount("umesh pandey")
'''
# with help of while loop:
'''
var="umesh pandeyy"
i=0
d1={}
while(i!=len(var)):
    d1[var[i]]=var.count(var[i])
    i=i+1
print(d1)
'''

# 3. User input number , print the add from 1 to input number
#input=5 output=5+4+3+2+1=15
#For loop
'''
num=int(input("Enter the number :"))
s=0
for i in range(1,num+1):
    s=s+i
print(s)
'''
#While loop
'''
num=int(input("Enter the number"))
i=1
s=0
while(i<=num):
    s=s+i
    i=i+1
print(s)
'''
#4. Print number b/w 100 to 200 which sum of digits should be even
'''
for i in range(100,200):
    i=str(i)
    s=0
    for j in i:
        s=s+int(j)
        # print(s)
    if s%2==0:
        print(i)
'''     
#5. Credit card last four digit shold be display , rest character show ***
#Ex. num=123456789 output=*****6789
'''
def CardNumber(num):
    num=str(num)
    Snum=num[0:(len(num)-4)]
    Enum=num[-4:]
    c=len(Snum)
    print('*'*c+Enum)
CardNumber(9315018680)
'''    
#6. Print largest number in list
'''
def max_num(list):
    for i in list:
        for j in list:
            if i<j:
                break
        else:
            print(i)
        
max_num([10,1,6,3,4,5])
'''
#7. Sort a list without using any inbuilt function like sort()
'''
list=[8,5,9,3,7,4,2,17,1]
l=len(list)
my_list=[]
while True:
    if len(my_list)==l:
        break

    for i in list:  #i=1
        for j in list: #j=3
            if i>j:# False
                break
        else:
            my_list.append(i)
            list.remove(i)

print(my_list[-2])
'''
# 8. Remove all duplicate element in a list and print list without duplictae elements
'''
list=[7,8,6,5,4,3,4,5,6,7,55,45,55]    
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)
'''
# 9. Print number from 1 to 10 with while loop
'''
i=1
while(i<=10):
    print(i)
    i=i+1
'''
# 10. Print hellow world in such a way like input="hello" output=['Hello',hEllo,heLlo,helLo,hellO]
'''
var="umesh"
l=[]
for i in var:
    c=var
    l.append(c.replace(i,i.capitalize()))
    
print(l)
'''   
# 11. Create a mixed String using the following rules
#s1 = "Abc",s2 = "Xyz" output="AzbycX"
''' 
s1 = "Abc"
s2 = "Xyz"
c1=0
c2=-1
s=''
for c in s1:
    s=s+s1[c1]+s2[c2]
    c1=c1+1
    c2=c2-1
print(s)
''' 

# 12. Print a word like  input ="umesh" output="uummeesshh"
'''
str1="umesh"
str2=''
for i in str1:
    i=i+i
    str2=str2+i
print(str2)
'''

# 13. convert two list in dictionary without using zip()
'''
keys=['one','two','three']
values=[1,2]
c=0
l=[]
d={}
for j in values:
    l.append(values.index(j))
for i in keys:
    if keys.index(i) in l:
        d[i]=values[c]
        c=c+1
    elif keys.index(i) not in l:
        continue
print(d)
'''
# 14. Print table when a user input a integer number and store it in a list 
'''
list=[]
def table(num):
    for i in range(1,11):
        table1=i*num
        list.append(table1)
    print(list)
    
table(2)
'''
# 15. Skip index value from a string
'''
str1="gaurav"
for i in str1:
    if str1.index(i)==5:
        continue
    else:
        print(i)
'''
'''
str1="gaurav"
for i in range(len(str1)):
    if i ==5:
        continue
    else:
        print(str1[i])
'''
# 16 Combine two dictionaries
''' 
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

for i,j in dict1.items():
    dict2[i]=j
print(dict2)
'''
# 17. Print the 2nd largest elementin a list
'''
l1=[5,2,3,1,4,8,6,9]
l2=[]
i=0

while True:
    if len(l2)==len(l1):
        break
    for i in l1:
        for j in l1:
            if i>j:
                break
        else:
            l2.append(i)
            l1.remove(i)
print(l2[-2])

'''
# 18.Function for odd and even number in a list of integers within two different list
'''
evenList=[]
oddList=[]
def myfunc(list):
    for i in list:
        if i%2==0:
            evenList.append(i)
        else:
            oddList.append(i)
    l=[evenList,oddList]
    print(l)
myfunc([1,2,3,4,5,6,7,8,9])
'''
#.19 print a dictionary in python such a way the user input a number output should be in dict of range from 1 to number
# and values cube of number
'''
def myFun(num):
    d1={}
    for i in range(1,num+1):
        d1[i]=i**3
    print(d1)
myFun(5)
'''
# .20 Key=name,age,favourite movie & Favorite song--should be comma seperated
'''
dict={}
dict['name']=input("Enter your name :")
dict['age']=input("Enter your age :")
dict['your favourite movie']=input("Enter your favourite movie with comm seperated :").split(',')
dict['your favourite song']=input("Enter your favourite song with comm seperated :").split(',')
print(dict)
'''
#21. Take a list and print squire with lambda and map
# It works like generator
'''
list1=[1,2,3,4]

a = lambda i:i%2==0
p=filter(a,list1)
print(list(p))
for i in list(p):
    print(i,"before")
print(list(p))

for j in list(p):
    print(j,"after")
'''
# 22. Print the number from input till that number
'''
def func(num):
    if num>0:
        func(num-1)
        print(num)
    
func(5)
'''
#23. Find factorial of a number with function
'''
def um(num):
    if num==0:
        return 1
    elif num==1:
        return 0
    else:
        f=1
        for i in range(1,num+1):
            f=f*i
        return f
print(um(5))
'''
#24. Find factorial of a number with help of recursive
'''
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

print(fact(3))
'''

# 25.Find odd or even with the help of recursive
'''
def gb(l,c=0):
    if l.index(l[c])==len(l)-1:
        if l[c]%2==0:
            print(l[c])
    else:
        if l[c]%2==0:
            print(l[c])
            gb(l,c=c+1)
        else:
            gb(l,c=c+1)
gb([1,2,3,4,5,6,7,8])
''' 
# 26. Write a programm to check a number armstrong number with for loop
'''
def gb(n):
    l=[]
    
    for i in range(1,n+1):
        i=str(i)
        add=0
        for j  in i:  
            add=add+int(j)**3
        if add==int(i):
            l.append(int(i))
        # else:
        #     print(n,'is not an Armstrong number!')
    print(l)
    
gb(1000)        
'''
# 27. Write a program to check a number armstrong number with while loop.
'''
def gb2(n):
    i=1
    l=[]
    while i!=n:
        add=0
    for j in str(i):
        add=add+int(j)**3
    if add==i:
        l.append(i)
    i+=1
    print(l)
    
gb2(1000) 
'''       
# 28.Armstrong numbers in a range of 1 to 200 print.
'''
num=200
# num=str(num)
for i in range(1,num+1):
    s=0
    for j in str(i):    
        s=s+int(j)**3 
    if s==int(i):
        print(i)
        
    # else:
    #     print(num,"is not a armstrong")

'''
# 29. Make a decorator which print Firstname and Lastname
'''
def myDec(func):
    def inner(*args,**kwargs):
        print("umesh") 
        func("pandey")
    return inner

@myDec
def firstName(str1):
    print(str1)

# var=myDec(firstName)
# var()
firstName()
'''
#.30.Print even number from a list and print time taken in execution of program with help of decorator
'''
import time
def decor(func):
    def inner(*args,**kwargs):
        t1=time.time()
        func()
        t2=time.time()
        print("Time taken in execution of program is :",t2-t1)
    return inner

@decor
def even():
    l=[]
    for i in range(1,20000):
        if i%2==0:
            l.append(i)
    # print(l)

even()
'''
#31.Remove all list from below list of list
'''
l1=[8,[7,5,1],2,[1,[2,[4,2,9]]],3]
from collections.abc import Iterable
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:
             yield item

                
                
print(list(flatten(l1)))
'''
'''
#32.Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
'''
d=0
a=0
char="hello world! 123"
di={}
for i in char:
    if i.isdigit():
        d=d+1
        
    elif i.isalpha():
        a=a+1

di["Letters"]=a    
di["Digits"]=d   
print(di)
''' 
'''      
#33. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}      
        
'''  
'''      
def mufunc(num):
    d={}
    for i in range(1,num+1):
        d[i]=i*i
    print(d)   
        
mufunc(5)        
'''  

#.34 Convert jason in to python object
'''
import json
jason_obj='{"name":"umesh","age":31}'
print(json.loads(jason_obj)['age'])

python_obj=json.loads(jason_obj)

print(python_obj)
'''
#.35 Convert python objects in jason
'''
import json
from operator import index
from re import A

# python_ob={'firstName':"umesh",'lastName':'pandey'}
# print(json.dumps(python_ob))       

python_str =  "Python Json"
print(python_str[0]
json_str=json.dumps(python_str)
print(json_str)
print(json_str[0])
'''
#.36 Write a Python program to find the strings in a given list, starting with a given prefix. 
'''
Input:
[( ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']

'''
'''
Input=[( 'ca',('cat', 'car', 'fcar', 'carpenter'))]
l=[]
for i in Input[0][1]:
    if Input[0][0] in i[0:2]:
        l.append(i)

print(l) 
# print(Input[0][1][1])
'''
#37.Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers. 
# l4=[1, 2, 3, 4, 5, 6]
#Output=Increasing.
# l4=[6, 5, 4, 3, 2, 1]
# Output =Decreasing.
# l4=[19, 19, 5, 5, 5, 5, 5]
# Output=‘Not a monotonic sequence!’
'''
a=l4[0]-1
for i in l4:
    if i!=a+1:
        print('List is not in increasing oreder with one increment!')
        break
    elif i==a+1:
        a=i
else:
    print('List is in increasing order with one increment!')
'''



#38.  Write a Python program to replace last value of tuples in a list. 
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
'''
l1=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
l2=[]
for i in l1:
    i=list(i)
    i.pop()
    i.append(100)
    i=tuple(i)
    l2.append(i)
    
print(l2)
'''
#39 . 6.Write a Python program to guess a number between 1 to 9. 
'''
Note : User is prompted to enter a guess(Enter a number as User input).
If the user guesses wrong then the prompt appears again until the guess is correct,
on successful guess, user will get a "Well guessed!" message, and the program will exit.

Note: Also print, in How many attempts user guessed the right number and
print the message like “You have guessed the right number in {} attempts!”
'''  
'''
n=8
total_attempt=5
print("Welcome to our 'Guess Number' game !!")
for i in range(5):
    num=int(input("Enter a number b/w 1 to 9 :"))
    
    if num==n:
        print("Well guess in attempt",i+1)
        print("WELDONE !!! You won!!")
        break
    else:
        print("Wrong guess ,Please guess again ,you have attemp left :",total_attempt-(i+1))
        continue
else:
    print("Bye,Thank you...Try next time")
        
'''
# 40. Write a program to input user number by comma sepperated value and put these value in list and tuple
'''
num=input("Enter a number by comma seperated").split(',')
print(num)

print((list(num)))
print(tuple(num))
'''
#41. Question:
'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
'''
str=input("Enter words by comma seperated").split(',')
# str.sort()
str.sort()
        
print(str)
'''
#42. Question:
'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
'''
l=[]
l2=[0,2,4,6,8]
for i in range(1000,3001):
    i=str(i)
    # if int(i[0])%2==0 and int(i[1])%2==0 and int(i[2])%2==0 and int(i[3])%2==0:
    #     l.append(i)

    for j in i:
        if int(j) not in l2:
            break
    else:
        l.append(int(i))
print(l)
'''

# 43. Question
'''
Define a generator function which takes a number as argument and generate a squence of even numbers
from 1 to that passed number(passed as argument).
Like,if you pass 5 as an argument then you have to generate a sequence of even numbers 
from 1 to 5.So the output will be 2,4.
'''
#44. Write a program to shutdown the computer
''' 
import os
shutdown = input("Do you want to shutdown your computer (yes / no): ")
if shutdown == 'yes':
    os.system("shutdown /s /t 1")
else:
    print('Shutdown is not requested')                                               
'''
#45. Write a program to find length of string without using len() function:
'''
str1="umesh pandey"
# y=str1.index(str1[-1])
k=0
for i in str1:
    print(i,end='')
    k=k+1

print("\nlength :",k)
'''
#46. A program to know the number of  words enter by user:
'''
def gb(s):
    a=s.split(' ')
    # print(a)
    if a[-1]=="":
        print('Total words:',len(a)-1)
    elif a[-1]!="":
        print('Total words:',len(a))

gb('umesh pandey kumar ')
'''
#47. Write a program to find largest number in two numbers
'''
a=4
b=6
p=lambda a,b:max(a,b)
print(p(a,b))
'''
#48. Lambda function to find even number in list
'''

f=filter(lambda i:i%2==0,[2,3,4,5,6,7,8])
print(f)
for j in f:
    print(j)
'''
#49. Lambda function to add all value in a list
'''
import functools as f

r=f.reduce(lambda i,j:i+j,[1,2,3,4,5,6,7])
print(r)
'''
#50. Lambda function to squire of all element in a list
'''
v=map(lambda i:i*i,[1,2,3,4,5,6])

for j in v:
    print(j,end=',')
'''
#51. In a list print the value and the index parallelly
'''
l=[2,3,4,5,6,7]

for i in l:
    print(f'The value is : {i} and index is {l.index(i)}')
'''
'''
 for i ,j in enumerate(l):
       print(f'Value is: {j} and index is : {i}')
'''
#52. eval functionality in python
'''
v=eval(input("Enter a number :"))

print(v,type(v))

'''
### FUNCTION ###
#53 .Odd and even number
'''
def evenOdd(n):
    if n%2==0:
        print(n,"is even number")
    else:
        print(n, "Number is odd")
        
evenOdd(10)
'''
#54.Even and odd with lambda function
'''
l=lambda i:i%2==0
print(l(5))
'''
#Python function to calculate factorial of a number
'''
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    
    print(f) 
fact(9)
'''
#55. write a program to take input numbers by comma seperated and give the average of all
'''
num=input("Enter numbers with comma seperated : ").split(',')

c=0
for i in num:
    c=c+int(i)
    av=c/len(num)
print(av)
'''
'''
lst=[1,2,3,4]
# lst=iter(lst)
for i in iter(lst):
    print(i)
for i in iter(lst):
    print(i)
# print(next(lst2))
# print(next(lst2))
# print(next(lst2))
# print(next(lst2))
# print(next(lst2))
    
'''
# 56 .Define a class Person and its two child classes: Male and Female. 
#All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class
'''
class Person:
    def getGender(self):
        print("Person Male")

class Male(Person):
    def getGender(self):
        print('Male')
        
class Female(Person):
    def getGender(self):
        print('Female')
        
p=Person()
m=Male()
f=Female()
f.getGender()
'''
#57. Print squire of integer from 1 to 10 with list comprehension
'''
x=[i*i for i in range(1,11)]    
print(x)
'''
#58. Print how many number of objects are created of a class
'''
class A:
    c=0
    def __init__(self): 
        A.c+=1    
a1=A()
a2=A()
a3=A()
print(A.c)
'''
#59. Print the duplicate value in another list
'''
l1=[1,2,3,2,3,4,5,6,5,6]
l2=[]
for i in l1:
    if l1.count(i)>1:
        if i not in l2:
            l2.append(i)
print(l2)

'''
# 60. Print the common element in two lists
'''
a=[1,2,3,4,5,6]
b=[3,4,5,6,7,8,1]
c=[]
for i in a:
    if i in b:
        c.append(i)
        
print(c)
'''
#61. Add two dictionary:
'''
d1={'name':'mahesh','age':21}
d2={'class':10,'salary':'50k'}    

for keys,values in d1.items():
    d2[keys]=values

print(d2)
'''
#62. Arrange list  in last item in tuple 
'''
l=[(8,9),(3,4),(5,6),(1,2),(2,3)]
l3=[]
length=len(l)
while len(l3)!=length:
    for i in l:
        for j in l:
            if i[-1]>j[-1]:
                break
        else:
            l3.append(i)
            l.remove(i)
print(l3)
'''
# 63. Question
'''
lst=['p','q','r']
# output=['p1','q1','p2','q2','p3','q3']
l=[]

number = eval(input("Enter a number: "))
for i in range(1,number+1):
    for j in lst:
        l.append(j+str(i))
print(l)

'''
# 64 .Question
'''
l=[2,3,4,5,6,7,9]
s=''
for i in l:
    s=s+str(i)
print(s)
'''
# print(' '.join('umesh').split(' '))

# print(("u mesh").split(' '))
    
# Vlues inside a list indexed by plus one
l=[1,2,3,4]
# l1=[]
# j=2
# for i in l:
#     l=str(l)
    
#     l.replace(str(i),str(j))
#     j=j+1
#     # l=int(l)
# print(l,end='')
# # output=[3,2,1]

#
'''
def gb(l):
   l2=[]
   l2.append(l[-1])
   l.remove(l[-1])
   for i in l:
       l2.append(i)
   print(l2)
gb([1,2,3,4])  
'''
# Program to generate a password so that their length should be 6 to 12 digits
#@$ should be, one lower case and one upper case, one digit should be in password
# print("Password should be 6 t0 12 digits with combinations of \n one special character(#@$), one lower,one upper case and one digits")
''''
def gb():
    print('Password must contain one character from (@ # $),one upper case character,one lower case,one digit,length must be min. 6 char and max is 12 characters!!')
    l=input('Enter password as per above given suggestion:')
    sp_char=['@','#','$']
    sp=""
    lower=""
    upper=""
    digit=""
    if len(l) in range(6,13):
        for i in l:
            if i in sp_char:
                sp=sp+'y'
            elif i.islower() and 'y' not in lower:
                lower=lower+'y'
            elif i.isupper() and 'y' not in upper:
                upper=upper+'y'
            elif i.isdigit() and 'y' not in digit:
                digit=digit+'y'
        total=sp+lower+upper+digit

        if len(total)==4:
            print('You have successfully set your password!!')
        elif len(total)!=4:
            print('Your password is not set with required criteria,please try again!','Thanks..')
    else:
        print('Password must contain atleast 6 characters or max. 12 characters,please try again','Thanks..')
        
gb()
'''
# Remove the number input by user from list 
'''
list=[1,2,3,1,2,4,5,6,2,1]
num=int(input("Enter a number we rmove its all occurence in list"))

for i in list:
    if i==num:
        list.remove(num)
        
print(list)
'''
# program to swap first and last element of the list.

'''
lst=[12, 35, 9, 56, 24]
for i in lst:
    lst[-1],lst[0]=lst[0],lst[-1]
    
print(lst)
'''
#length of list without using len()
'''
lst=['mango','apple',2,3,4,5]
i=0
for i in lst:
    i=i+1
    pass
print(i)
'''
# Q. Input a number and check palindrome or not if palindrome then find next palindrome,
# and if not palindrome then also find next palindrome
'''
num=int(input("Enter the number : "))

if str(num)==str(num)[::-1]:
    print(num ,"Number is palindrome")
    while True:
        num=num+1
        if str(num)==str(num)[::-1]:
            print("Next palindrome number is ",num)
            break
    
    
elif str(num)!=str(num)[::-1]:
    print(num ,"is not a palindrome")
    while True:
        num=num+1
        if str(num)==str(num)[::-1]:
            print("Next palindrome number is ",num)
            break
''' 
'''
import time
def ab():
    n=input('Enter space seperated values to perform a pelindrome check:').split(' ')
    for i in range(len(n)):
        if n[i]==n[i][::-1]:
            print(f'{n[i]} is a palindrome number!')
            time.sleep(4)
            a=int(n[i])
            a=a+1
            while True:
                if str(a)==str(a)[::-1]:
                    print(f'Next Palindrome for this above number is {a}!')
                    break
                else:
                    a=a+1
        elif n[i]!=n[i][::-1]:
            print(f'{n[i]} is not a palindrome number!')
            time.sleep(4)
            a=int(n[i])
            a=a+1
            while True:
                if str(a)==str(a)[::-1]:
                    print(f'Next Palindrome for this above number is {a}!')
                    break
                else:
                    a=a+1
ab()                    
'''
#Q
'''
lis=[1, 2, 3, 2, 3, 1, 3]

l=filter(lambda i: lis.count(i)%2!=0,lis)
for j in l:
    print(j)
'''
#Q
# L = [1, 2, 3, 4, 5]
# n=4
'''
l=lambda n : n in [1,2,3,4,5]
a=int(input("Enter any number: "))

print(l(a),a)
'''

# Program to odd index value from l1 and even index value in to another list
'''
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3=[]
j=0
for i in range(len(l1)):
    if i%2!=0:
        l3.append(l1[i])
        
    elif i%2==0:
        l3.append(l2[i])    
        
print(l3)
'''

#Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

#Write a Python program to check if a given positive integer is a power of two
'''
def gb(n):
    a=n
    while True:
        if n%2!=0:
            print(f'{a} is not a power of 2')
            break
        elif n%2==0:
            n=n//2
            if n==1:
                break      
    if n==1.0:
        print(f'{a} is a power of 2')
gb(60)
'''
# Write a Python program to check if a number is a perfect square.
# Input : 9
# Output : True 
'''
n=int(input("Enter number : "))

for i in range(1,n):
    if i**2==n:
        print(f"Number {n} is a perfect squire of {i}")
        break
else:
    print(f"Number {n} is not perfect squire")
'''    
#Write a Python program to find missing numbers from a list.
#Input : [1,2,3,4,6,7,10]
#Output : [5, 8, 9]

'''
l= [2,4,6,8,12,14,18]
l1=[]
j=0
for i in l:
    j=j+1
    if j<=len(l)-1:
        if l[j]!=i+2:
            l1.append(i+2)
            l.insert(j,i+2)

if len(l1)!=0:
    print(l1)
else:
    print("Nothing is missing")
'''

#Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit. Go to the editor
# Input : 48
# Output : 3
'''
num=int(input("Enter an integer :"))
num=str(num)
# print(len(num))
s=0
for i in num:
    s=s+int(i)
    
k=0
if len(str(s))>1:
    for i in str(s):
        k=k+int(i)
    print(k)


else:
    print(s)
        
'''
# num=input("Enter an integer :")
# print(type(num))
'''
def myFun(num):
    while len(str(num))!=1:
        s=0
        for i in str(num):
            s=s+int(i)          
        k=0
        if len(str(s))>1:
            for i in str(s):
                k=k+int(i)
               
            print(k)
            break

        else:
            print(s)
            break
                
myFun(2178999999999999)
'''
'''
def gb(n):
    if len(str(n))==1:
        print(n)
    else:
        a=0
        for i in str(n):
                a=a+int(i)
        gb(n=a) #function calling itself 
        
gb(6767)
'''
# Write a Python program to push all zeros to the end of a list.
'''
l= [0,2,3,0,0,4,6,0,7,0,10]

for i in l:
    if i==0:
        l.remove(i)
        l.append(i)
print(l)

#Write a Python program to find majority element in a list.
# Input : [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
# Output : 5
l=[1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
'''
#Write a Python program to find majority element in a list.
# Input : [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]
# Output : 5      
'''
l=[1,2,5,5,5,6,5,3,5,1,2,8,9,1,9,9,3,9,9,9]
# l=[1,2,3,5,6,8,9]
for i in set(l):
    for j in set(l):
        if l.count(i)<l.count(j):
            break
    else:
        print(f'Digit {i} comes'+' '+str(l.count(i))+' '+'times')     
''' 
# Find the perfect Number  i.e sum of divisor of num should be equal to num
'''
def up(num):
    s=0
    for i in range(1,num):
        if num%i==0:
            s=s+i
    if s==num:
        print(f'{num} is a perfect number')
      
    else:
        print(f'{num} is not a perfect number')
        
up(12)
'''
#Write a Python program to calculate the value of 'a' to the power 'b'.
# (power(3,4) -> 81
'''
def gb(a,b):
    if b==1: #base Case
        return a
    else:
        return a*gb(a,b-1) # recursive case
print(gb(3,3))
'''
#Python program to count Even and Odd numbers in a List
'''
list1 = [2, 7, 5, 64, 14]

eve_num=len(list(filter(lambda a: a%2==0,list1)))
odd_num=len(list(filter(lambda b: b%2!=0,list1)))

print("Count of even number :",eve_num)
print("Count of odd number :",odd_num)

'''

#Write a Python program to create a list whose ith element is the maximum of the first i elements from a input list

#Input:[6, 5, 4, 3, 2, 1]
#Output:[6, 6, 6, 6, 6, 6]

# input=[6,5,4,3,2,1]
# l=[]
# for i in range(len(input)):
#     if max(i)>
'''
l1 = [(),(),('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
l2=[]
for i in l1:
    if i!=1:
        l2.append(i)
print(l2)  
'''
# Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers. Go to the editor
# input:
# [1, -4, 6, 7, 4]
# output:
# [4, 1]
'''

l=[1,0,-4,6,0,7,4]
for i,j in enumerate(l):
    for x,y in enumerate(l):
        if j+y==0 and i!=x:
            print(f'sum of {j} and {y} is 0 and indices are', i,x)
           
'''    
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d={}

for i in range(len(keys)) : d[keys[i]]=values[i]
    
    
    
print(d)
'''
'''
sample_dict = {'a': 100, 'b': 200, 'c': 300}
           #
#ternary operator i.e sort form of if else#
           #
print(True if 200 in sample_dict.values() else False)        
'''
# Cahnge the key of a dictionary
'''
d = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

# d['NAME']=d.pop('name')
d['NAME']=d['name']
del d['name']

print(d)
'''
# Minimum values of key
d= {
  'Physics': 45,
  'Math': 65,
  'history': 75
}
'''
for i,j in d.items():
    for k in d.values():
        if j>k:
            break
    else:
        print(f'minimun value is {j} and corresponding key is "{i}".')
'''
'''
l=[]
for i,j in d.items():
         l.append(j)
for i in d.keys():
         if d[i]==min(l):
            print(f'Minimum value is {min(l)} and key is {i}')        
'''
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
'''
d = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

d['emp3']['salary']=8500
print(d)
'''

# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
'''
def up(a,b):
    def sp():
        add=a+b
        return add
    return 5+sp() 
print(up(2,3))   
'''
#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
'''
var=10
var1=var
def up(num):
    if num==0:
        return num
    else:
        return num + up(num-1)
gb=up
print(gb(10))
'''
#Unpacking of a tuple or a list
'''
tuple1 = (10, 20, 30, 40)
a,b,c,d=tuple1
print(a,b,c,d)
'''
#Swap to tuple
'''
tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1,tuple2=tuple2,tuple1
print(tuple1,tuple2)
'''
'''
tuple1 = (11, [22, 33], 44, 55)   
# tuple1[1][0]=2200
# print(tuple1)
tuple1[1].remove(22)
tuple1[1].insert(0,222)
print(tuple1)
'''
#################Exercise 8: Sort a tuple of tuples by 2nd item##################
'''
t = (('a', 23),('b', 37),('c', 11), ('d',29),('e',12))
a=len(t)
t=list(t)
l=[]
while len(l)!=a:
    for i in t:
        for j in t:
            if i[1]>j[1]:
                break
        else:
            l.append(i)
            t.remove(i)  
print(tuple(l))
''' 
'''    
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29),('e',12))
tuple1=list(tuple1)
def fun(e):
    return e[1]

tuple1.sort(key=fun)
print(tuple1)
'''
'''
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

def up(i):
    return len(i)

cars.sort(key=up)
print(cars)
'''
'''
class Vehicle:
    def __init__(self):
        self.speed=90
        self.mileage=50
        
v1=Vehicle()

print(v1.speed)
print(v1.mileage)
'''
'''
class Vehicle:
    def __init__(self,company,price):
        self.company=company
        self.price=price
        
    def config(self):
        print(f'Vehicle having a company of {self.company} and price {self.price}')
        
class Bus(Vehicle):
    pass

b=Bus('Toyota',250)
b.config()
'''
#Create a Bus class that inherits from the Vehicle class. 
# Give the capacity argument of Bus.seating_capacity() a default value of 50.
'''
class Vehicle:
    def __init__(self,comp,price):
        self.comp=comp
        self.price=price
    
    def capacity(self,capacity=200):
        print(f'Bus having a vehicle capacity {capacity}')
        
class Bus(Vehicle):
    def capacity(self,capacity=50):
        super().capacity(capacity=500)
        print("bus capacity")
        
        
b=Bus('Hyundai','250 $')
b.capacity()

'''
'''
str1 = "James"
s=''
m=len(str1)//2
s=s+str1[0]+str1[m]+str1[-1]
print(s)
'''
'''
s1 = "Ault"
s2 = "Kelly"
m=len(s1)//2
s=s1[0:m]+s2+s1[m:]
print(s)
'''

# Arrange string characters such that lowercase letters should come first
'''
s = "PyNaTive"
s1=''
for i in s:
    if i.islower():
        s1=s1+i     
for j in s:
    if j.isupper():
        s1=s1+j
print(s1)  
'''


  

        
















