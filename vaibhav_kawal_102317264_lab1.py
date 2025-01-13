# -*- coding: utf-8 -*-
"""Vaibhav_kawal_102317279_Lab1.ipynb





# Write a Python program to print "Anything You find cool."
print("Anything you find cool")

# Write a program to add two numbers and print the result.
a = 5
b = 7

c = a + b

print("Answer = ",c)

# Write a program to concatenate two strings and print the result.

a = "Hello"
b = " World"
c = a + b

print("Answer = ",c)

# Write a program to concatenate a string and a number and print the result
a = 5
b = " Hello "

c = str(a) + b
print("Answer = ",c)

#  Write a Python program to check if a number is positive, negative, or zero
# using an if-else statement.

num = int(input("Please enter number: "))

if num > 0:
  print("Number is positive")
elif num==0:
  print("Entered 0")
else:
  print("Number entered is negative")

# Write a program to check if a given number is odd or even

num = int(input("Please enter number: "))

if num%2==0:
  print("Number is even")
else:
  print("Number is odd")

# Write a program to print numbers from 1 to 10 using a
# for loop

for i in range(1,11):
  print(i)

# Write a program to print numbers from 1 to 10 using a
# while loop.

i = 1

while i < 11:
  print(i)
  i+=1

# Write a program to calculate the sum of numbers from 1 to 100 using a loop.

sum = 0

# Including the numebr 100 as well
for i in range(1,101):
  sum+=i

print("Sum is = ",sum)

# 5.1 Create a list of 5 numbers. Write a program to find the largest and smallest
# numbers in the list

arr = [1,2,3,4,5]

max = -1000000000
min =  1000000000

for i in arr:
  if i > max:
    max = i
  if i < min:
    min = i
print("Max is = ",max)
print("Min is = ",min)

# 5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve
# the value of a given key.

myFirstDict = {
    "Name" : "Vaibhav",
    "Age" : 20 ,
    "Interests" : ["music","swimming"]
}

print(myFirstDict["Name"])

# 5.3 Write a program to sort a list of numbers in ascending and descending order

# First we will implement a normal bubble sort and then a reverse

arr = [2,8,4,90,1,75,3,1]

for i in range(len(arr) - 1):
  for j in range(len(arr) - i - 1):

    if arr[j]>arr[j+1]:
      arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)

arr.reverse()

print(arr)

#  5.4 Write a program to merge two dictionaries into one.

dict_1  = {
    "Name" : "Vaibhav",
    "Age" : 20 ,
    "Interests" : ["music","swimming"]
}

dict_2 = {
    "Username" : "VaibhavKawal",
    "Password" : 123455
}

for key,value in dict_1.items():
  dict_2[key] = value

print(dict_2)

#  6.1 Write a program to count the number of vowels in a given string.

ans = "Hello there my name is Vaibhav"
ans.lower()
count = 0

for i in range(len(ans)):
  if ans[i]=="a" or ans[i]=="e" or ans[i]=="i" or ans[i]=="o" or ans[i]=="u":
      count+=1

print(count)

#  6.2 Write a program to reverse a string and print it.

input1 = "Hello there my name is Vaibhav"
string = list(input1)

for i in range(len(string)//2):
  string[i],string[len(string)-i-1] = string[len(string)-i-1],string[i]

ans = ''.join(string)
print(ans)

# A shorter approach could be

ans_v2 = input1[::-1]
print(ans_v2)

#  7.1 Write a program to create a text file, write some text into it, and then read and
# print the content

file = open("myFirstFile.txt","r+")

file.writelines("My First Text in the file , Yay!!!")
content = file.readline()

print(content)


file.close()

# 7.2 Write a program to append text to an existing file and print the updated
# content

file = open("myFirstFile.txt" , "a+")

file.writelines("New data coming your way. yayyy \n")
file.close()

file = open("myFirstFile.txt" , "r")
content = file.readline()

print(content)

file.close()

#  7.3 Write a program to count the number of lines in a text file.
file = open("myFirstFile.txt" , "r")

count = len(file.readlines())

print(count)

# 8.1 Write a program to handle division by zero using a
# try-except block

n_1 = int(input('Please enter numerator: '))
n_2 = int(input('Please enter denominator: '))

try:
    n3 = n_1 / n_2
    print("Result:", n3)
except ZeroDivisionError:
    print("Cannot divide by 0.")

#8.2 Write a program to handle invalid input (e.g., when the user enters a string
# instead of a number)

try:
  n_1 = int(input("Please enter an integer: "));

except ValueError:
  print("Invalid input entered")

# 3 Write a program to demonstrate the use of
# finally in exception handling.

try:
  n_1 = int(input("Enter your age: "))
except ValueError:
  print("Invalid Age entered")
else:
  print("You look young for your age: ",n_1)
finally:
  print("Thanks for checking your age")

#  9.1 Write a program to generate 5 random numbers between 1 and 100 and print
# them.

import random

print("generating 5 randoms : ")

for i in range(5):
  print("random #",i+1,' is ', random.randint(1,100))

#Write a program to generate a random number and check if it is prime.

import random
import math

num = random.randint(1,100)
print("The number is = " , num)

if(num<=1):
  print("The number is not prime")
elif(num==2):
  print("The number is prime")
else:
  ans = True
  for i in range(2,math.ceil(math.sqrt(num))+1):
    if num%i==0:
      ans = False
      break
  print("The number is prime: " ,ans )

# Write a program to simulate rolling a six-sided die

import random

face = random.randint(1,6)

while True:
  print("Die face: ",face)
  print("Press 0 to quit")
  x = int(input())
  if x==0:
    break
  face = random.randint(1,6)

# Write a program to shuffle a list of numbers.

import random

arr = ["ciao" , "Good" , "voila"]
random.shuffle(arr)
print(arr)

# Write a program to randomly select an item from a list.
import random

arr = ["ciao" , "Good" , "voila"]
ind = random.randint(0,len(arr)-1)
print(arr[ind])

# Write a program to generate a random password of given length.


import random

password = ""
length = int(input("Enter the length of password: "))

if length < 4:
  print("Invalid length entered , minimum length is 4")
length = 4

uppercas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercas = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbols = "!@#$%^"

password += random.choice(uppercas)+random.choice(lowercas)+random.choice(number)+random.choice(symbols)

allSum = uppercas + lowercas + number + symbols

for i in range(length - 4):
  password += random.choice(allSum)

passwordFinal = list(password)
random.shuffle(passwordFinal)
password = "".join(passwordFinal)

print("Password is : " , password)

#  Write a program to pick a random card from a standard deck of 52 cards.

suit = ['Hearts' , 'Diamonds' , 'Clubs' , 'Spades']
number_card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

ans = random.choice(number_card) + " " + random.choice(suit)

print(ans)

# Write a program to accept two numbers as command-line arguments, add
# them, and print the result.
# DOUBT
import sys

num1 = sys.argv[1]
num2 = sys.argv[2]
result = num1 + num2
print(f"The sum of {num1} and {num2} is: {result}")

# Write a program to accept a string as a command-line argument and print its
#length.
#DOUBT

import sys

input_string = sys.argv[1]
print(f"The length of the string '{input_string}' is: {len(input_string)}")

# Write a program to use the
# math library to calculate the square root of a given
# number

import math

num = int(input("enter number to find square root of: "))

print("Square root of number = ",math.sqrt(num))

# Write a program to use the
# datetime library to print the current date and time.

from datetime import *

print("Date is = ", date.today())
print("Time is = " , datetime.now().time())

# Write a program to use the
# os library to list all files in the current directory

import os

print("All files in current directory are as follows = ")

print(os.listdir())