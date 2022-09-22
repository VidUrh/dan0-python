#-*- coding: cp1250 -*-

while 1:
    op = input("Vnesi operacijo: ")
    a = int(input('vnesi št. 1 '))
    b = int(input('vnesi št. 2 '))

    if op == '+':
        print('Vsota = '+str(a+b))
    elif op == '-':
        print('Razlika = '+str(a-b))
    elif op == '/':
        print('Koeficient = '+str(a/b))
    elif op == '*':
        print('Produkt = '+str(a*b))