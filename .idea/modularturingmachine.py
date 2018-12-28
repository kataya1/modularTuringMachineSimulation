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
    "finds the first # after the string, returns int"
    for index in range(len(str)):
        print (str[-(index+1)])
        if (str[-(index+1)].isalnum()):
            break
    print (len(str)-(index))
    return len(str)-(index)

def Lsharp(str):
    "finds the first # before the String, returns int"
    for index in range(len(str)):
        print (str[index])
        if (str[index].isalnum()):
            break
    print(index)
    return index

def R(str,head):
    "shifts the head to the right and adds # if endofstring "
    # global head
    if (head == (len(str)-1)):
        str = extendStringRight(str)
    head += 1
    return str,head

def L(str,head):
    "shifts the head to the left and adds # if endofString"
    # global head
    if (head == 0):
        str = extendStringLeft(str)
    else:
        head -= 1
    return str,head

def Rnsharp(str,n):
    "finds the nth # after the string, returns int"
    index = Rsharp(str)
    for i in range(n):
        index = R(str,index)



string = input("what is the string? ")
temp = L(string,0)
print(temp[0])


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


