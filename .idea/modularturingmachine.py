#!/usr/bin/python
import sys
exit = 0
back = 0
space = ' '
head = 0
def extendStringRight(str):
    str = str + '#'
    return str

def extendStringLeft(str):
    str = '#' + str
    return str

def Rsharp(str):
    "finds the first # after the string, returns int"
    for index in range(len(str)):
        # print (str[-(index+1)])
        if (str[-(index+1)].isalnum()):
            break
    # print (len(str)-(index))
    return len(str)-(index)

def Lsharp(str):
    "finds the first # before the String, returns int"
    for index in range(len(str)):
        if (str[index].isalnum()):
            break
    return index - 1

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
    "finds the nth # after the string"
    index = Rsharp(str)
    i=1
    while i < n:

        temp = R(str,index)
        index = temp[1]
        str = temp[0]
        i+=1
    return str,index

def Lnsharp(str,n):
    "find the nth # befor the string"
    index = Lsharp(str)
    i=1
    while i<n:
        print("computing")
        str,index = L(str,index)

        i+=1
    return str,index
# str = '#12#'
# head = 0
# str,head = Rnsharp(str,2)
# print(str)
# print(head)
# op = 'r1#'
#
# print (op[1:-1])


while exit != 1:
    back = 0
    string = input("what is the string? ")
    print("to go back type B\n")
    while back != 1:

        print(string)
        print(space * head + '^\n' )
        operation = input("operation? (L,R,L#,R#,Ln#,Rn#) ")

        if (operation == 'R' or operation == 'r'):
           string,head= R(string,head)

        elif (operation == 'l' or operation == 'L'):
           string,head = L(string,head)

        elif (operation == 'l#' or operation == 'L#'):
           head = Lsharp(string)

        elif (operation == 'R#' or operation == 'r#'):
           head = Rsharp(string)

        elif (operation[1:-1].isdigit() and (operation[0]== 'R' or operation[0]== 'r') and operation[-1]=='#'):
            string,head=Rnsharp(string,int(operation[1:-1]))

        elif (operation[1:-1].isdigit() and (operation[0]== 'L' or operation[0]== 'l') and operation[-1]=='#'):
            string,head=Lnsharp(string,int(operation[1:-1]))

        elif (operation == 'back' or operation == "b" or operation == 'B'):
            back = 1

        else :
            print("invalid input try again")

    exitS = input(" do you want to exit Y/N ?")
    if(exitS == 'y' or exitS == 'Y'):
        exit=1
    else:
        continue

print("end of program")
sys.exit(-1)




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


