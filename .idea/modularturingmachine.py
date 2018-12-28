#!/usr/bin/python
import sys
String = '##hello1101001####'
test = '#12#'
head = 3
def extendStringRight(str):
    str = str + '#'
    return str

def extendStringLeft(str):
    str = '#' + str
    return str

def Rsharp(str):
    "finds the right most # place"
    for head in range(len(str)):
        print (str[-(head+1)])
        if (str[-(head+1)].isalnum()):
            break
    print (len(str)-(head))
    return len(str)-(head)

def Lsharp(str):
    for head in range(len(str)):
        print (str[head])
        if (str[head].isalnum()):
            break
    print(head)
    return head

def R(str):
    global head
    if (head == (len(str)-1)):

        str = extendStringRight(str)
    head += 1
    return str

def L(str):
    global head
    if (head == 0):
        str = extendStringLeft(str)
    return str

# def R():

# var1 = 'Hello World!'
#
# head = 0
# var2 = "Python Programming"
#
#
# print ("var1[-1]: ", var1[-2])
# print ("var2[1:5]: ", var2[1:5])
# var1 = 'Hello World!'
# print ("Updated String :- ", var1[:6] + 'Python')
# print ("My name is %s and weight is %d kg!" % ('Zara', 21))
#
# String = extendStringRight(String)
# Rsharp(String)

test = R(test)
print (test)
print(head)
print(head)