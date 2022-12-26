lis=[20,4,21]

for i in range(len(lis)):
    lis[i]=str(lis[i])
print(type(lis[0]))
# lis=str(lis)
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[j]+lis[i]>lis[i]+lis[j]:
            lis[i],lis[j]=lis[j],lis[i]

res=''.join(lis)


print(res)
# for i in range(len(lis)):
#     lis[i]=str(lis[i])
# res=''.join(lis)

# print(res)

# # s="20421"
# # # s=int(s)
# # l=[]
# # for i in s:
# #     if i==2:
#         continue
#     l.append(i)

# print(l)

# lis=[5,56,7,'umesh']
# # for i in range(len(lis)):
# #     lis[i]=str(lis[i])
# lis=''.join(lis)
# print(lis)

# # s1 = "AAAXXXBBBYYIIIIIF"
# # Output = "A3X3B3Y2I5F1"
# # d1={}

# # for i in s1:
# #     d1[i]=s1.count(i)
# # s=""
# for i,j in d1.items():
#     s=s+str(i)+str(j)

# print(s)

# lst = [1,2,3,4,5,6,7,8,9]
# print(lst[-4:-7])

# 38.  Write a Python program to replace last value of tuples in a list. 
# lst= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# #Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]p
# l=[]
# for i in lst:
#     i=list(i)
#     l.append(i)
    
# print(l)

# for i in l:
#     i[2]=100
#     i=tuple(i)
#     l.append(i)
'''
Find the number pair (Level 1) (15 mins)
Given an array of integers that is already sorted in ascending order, find two numbers such that they
add up to a specific target number.
The function twoSum should return array of indices of the two numbers such that they add up to the
target, where index1 must be less than index2.
If no matched pairs exists, output should be a null value
Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same
element twice.
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3
Input: numbers = [-1,0], target = -1
Output: [1,2]
Example 4
Input: numbers = [11, 19, 78], target = 8
Output: null
Note:
Desired time complexity is O(n), space complexity O(1)
Your comments, in addition to your code are also evaluated
'''
# =============================================================================
'''
# Make Profit (Level 1) (15 mins)
# Say you have an array prices for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before
# you buy again).
# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4
# (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Note that you
# cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the
# same time. You must sell before buying again.
# Example 3:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# Constraints:
# 1 <= prices.length <= 3 * 10 ^ 4
# 0 <= prices[i] <= 10 ^ 4
# Note:
# Desired time complexity is O(n), space complexity O(1)
# space complexity O(1) => O(1) denotes constant space use: the algorithm allocates the same
# number of pointers irrespective to the list size. In contrast, O(N) denotes linear space use: the
# algorithm space use grows together with respect to the input size
# your comments, in addition to your code are also evaluated
'''
# =============================================================================
'''
# Divisible Problem (Level 1) (15 mins)
# You are given an array A of size N that contains integers. Here, N is an even number. You are required
# to perform the following operations:
# 1. Divide the array of numbers in two equal halves
# Note: Here, two equal parts of a test case are created by dividing the array into two equal parts.
# 2. Take the first digit of the numbers that are available in the first half of the array (first 50% of the test
# case)
# 3. Take the last digit of the numbers that are available in the second half of the array (second 50% of
# the test case)
# 4. Generate a number by using the digits that have been selected in the above steps
# Your task is to determine whether the newly-generated number is divisible by 11.
# Input format:
# First line: A single integer N denoting the size of array A
# Second line: N space-separated integers denoting the elements of array A
# Output format:
# If the newly-generated number is divisible by 11, then print OUI. Otherwise, print NON.
# Constraints:
# 1 <= n <= 105
# 1 <= A[i] <= 105
# Sample Input:
# 6
# 15478 8452 8232 874 985 4512
# Sample Output:
# OUI
# Explanation:
# The first digit of 15478 is 1.
# The first digit of 8452 is 8.

# The first digit of 8232 is 8.
# The last digit of 874 is 4.
# The last digit of 985 is 5.
# The last digit of 4512 is 2.
# The newly generated number will be 188452 which is divisible by 11.
'''
# =============================================================================
'''
# Finding Vaccines (Level 2) (30 mins)
# You are creating a vaccine to fight against a worldwide novel pandemic virus. A vaccine contains a
# weakened virus that is injected inside people to produce antibodies to let it fight against the virus. The
# study of interaction among RNA of various viruses is quite necessary for this. An RNA consists of four
# types of molecules Guanine (G), Adenine (A), Cytosine (C), and Uracil (U).
# You are given the structures of RNA for the pandemic virus and several vaccine viruses in the form of
# strings containing characters G, A, C, and U representing respective molecules. You know that if there
# is higher interaction between the pandemic virus and vaccine virus, then better the vaccine will be. You
# also know that the only interaction between any two RNAs is a result of the interaction between their
# Guanine (G) and Cytosine (C) molecules. Formally, if the strings for RNA structures are s1
# and s2
# , then

# you must consider the following points:

# One molecule of Guanine (G) of s1

# and one molecule of Cytosine (C) of s2

# will lead to one unit of

# interaction.
# One molecule of Guanine (G) of s2

# and one molecule of Cytosine (C) of s1

# will lead to one unit of

# interaction.
# Any other pair of molecules do not add to any interactions.
# In this way, the total interaction between s1
# and s2
# is calculated as the sum of individual molecule pair

# interactions (as discussed above).
# You must find the best available vaccine.
# Input format:
# The first line contains a single integer n denoting the number of vaccines
# The second line contains a single integer m denoting the length of the string denoting the RNA
# structure for the pandemic virus.
# The third line contains a string r denoting the RNA structure for the pandemic virus.
# Next 2n lines contains the following lines where:
# (2i - 1)th line contains a single integer l
# i
# denoting the length of the string denoting the RNA

# structure for the i

# th vaccine virus
# (2i)th line contains a string si

# denoting the RNA structure for the i

# th vaccine virus

# Output format:
# Print a single integer k if the k

# th vaccine is the best, that is, it has the maximum interaction with

# pandemic virus RNA, where 1 <= k <= n obviously holds.
# If there are more than one answers possible (in case of two or more have the maximum interaction
# value), then print the smallest answer possible.
# Constraints:
# 1 <= n, m, li
# <= 1000

# r, si
# contains {G, A, C, U} characters only
# Sample Input:
# 2
# 5
# ACGGU
# 6
# AGCAAA
# 8
# UAUAAGAG

# Sample Output:
# 1
# Explanation:
# RNA of MARS-20 virus contains 2 molecules of G and 1 molecule of C.
# Interaction with first vaccine = 3 units
# Interaction with second vaccine = 2 units
# Hence, first vaccine is better.
'''
# =============================================================================
'''
# String Clash (Level 2) (30 mins)
# You are given two strings S and T of equal lengths. You need to pick some characters from the first
# string, some from the second string and then form a new string by rearranging the characters you have
# picked. You need to find the length of the maximum string that you can make which will be a
# palindrome.
# Input:
# The first line contains a string S as input and the next line contains a string T as input.
# Output:
# In the output, you need to print an integer which denotes the maximum length of the palindrome that
# can be obtained.
# Constraints:
# 1 <= |S|, |T| <= 1000
# Sample Input:
# aab
# cba
# Sample Output:
# 5
# Explanation:
# In the sample test case, you can form the string baaab by picking the characters from both the strings.

'''

#Question1

# def twoSome(li,target):
#     j=len(li)
#     for i in range(len(li)):
#         if li[i]+li[j]==target:
#             print(i,j)
#         j=j-1

# twoSome([1,2,3,4,5],7)


# l=[1,2,3,4,5]
# tr=7
# lr=[]#6,5,4,3,2
# # for i in range(len(l)):
# #     if tr-l[i] in lr:
# #         print(l.index(tr-l[i],i))
#     else:
#         lr.append(tr-l[i])

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==tr:
#             print(i,j)
    
'''
li=[15478,8452,8232,874,985,4512]

n=len(li)
n1=int(n/2)
l1=li[0:n1]
l2=li[n1:]
l2=l2[::-1]
s1=''
for i in l1:
    i=str(i)
    s1=s1+i[0]
print(s1)

s2=''
for i in l2:
    i=str(i)
    s2=s2+i[0]
s=s1+s2
print(s)
if int(s)%11==0:
    print(True)
print(False)
...


class A(object):
   def __init__(self, a):
       self.num = a
   def mul_two(self):
       self.num *= 2
 
class B(A):
   def __init__(self, a):
        self.num = a
   def mul_three(self):
       self.num *= 3
 
obj = B(4)
print(obj.num)

obj.mul_two()
print(obj.num)
 
obj.mul_three()
print(obj.num)



 1:Max:4, 4:Ann:0, 2:Jim:4, 3:Tom:1
 Explanation:
 1:Max:4 represents

1 -> employee id
Max -> employee name
4 -> manager id
output:

 Ann
    -Max
        --Tom
    -Jim
'''
#  '''
# s1="1:max:4"
# s2="4:Ann:0"
# s3="2:Jim:4"
# s4="3:Tom:1"

# l1=s1.split(':')
# l2=s2.split(':')
# l3=s3.split(':')
# l4=s4.split(':')
# d1={}

# d1.update({"employee_id":[l1[0],l2[0],l3[0],l4[0]]})
# d1.update({"employee_name":[l1[1],l2[1],l3[1],l4[1]]})
# d1.update({"manager_id":[l1[2],l2[2],l3[2],l4[2]]})

# print(d1)


# d={"one":1}

# l=[1,6,44,50,7,2,5]


# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# l=[6, 7, 10, 11, 13]
# l1=[]
# for i in range(l[0],(l[-1]+1)):
#     if i not in l:
#         l1.append(i)

# print(l1)
# l1=list[set(range(max(l)+1))-set(l)]
# print(l1)

class A(object):
   def __init__(self, a):
       self.num = a
   def mul_two(self):
       self.num *= 2
 
class B(A):
     def __init__(self, a):
        self.num = a
     def mul_three(self):
       self.num *= 3
       self.num -= 12 
    

# obj = B(4)
# print(obj.num)#4

# obj.mul_two()#8
# print(obj.num)
 
# obj.mul_three()
# print(obj.num)#12


'''
Write a function that prints the number of times the string ‘bulb’ occurs 
in string. For example, if s = 'azcbulbulbegghakl', then your program should print 2
'''

s = 'azcbulbulbegghakl'



# def strOccurence(s,*args,**kwargs):
# d1 = {}
# s2='bulb'
# if s2 in s:
#     d1[s2]=s.count(s2)

# print(d1)






    


 
