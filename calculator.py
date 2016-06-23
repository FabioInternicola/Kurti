import os
import math
fcolor = open('color','r')
color = fcolor.read()
fcolor.close()
os.system('color %s' % color)
print("0: Done\n1: Addition\n2: Subtration\n3: Moltiplication\n4: Division\n5: Elevating power\n6: Square root\n")
operation = input("Number of the operation: ")
if operation == '0':
    print('Operation canceled.\n')
    os.system('pause')
if operation == '1' or operation=="I want to add":
    a = float(input(''))
    i=0
    while i==0:
        print('plus')
        a = a + float(input(''))
        print('Result: %d' % a)
if operation == '2' or operation=="I want to subtract":
    a = float(input(''))
    i=0
    while i==0:
        print('less')
        a = a - float(input(''))
        print('Result: %d' % a)
if operation == '3' or operation=="I want to multiply":
    a = float(input(''))
    i=0
    while i==0:
        print('per')
        a = a * float(input(''))
        print('Result: %d' % a)
if operation == '4' or operation=="I want to divide":
    a = float(input(''))
    i=0
    while i==0:
        print('devided')
        a = a / float(input(''))
        print('Result: %d' % a)
if operation == '5' or operation=="I want to elevate":
    a = float(input(''))
    i=0
    while i==0:
        print('to the')
        a = a ** float(input(''))
        print('Result: %d' % a)
if operation=='6' or operation=="I want to extrate the square root":
    a = float(input(''))
    a = math.sqrt(a)
    print('Result: %d' % a)
