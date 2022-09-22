#-*- coding: cp1250 -*-

import Tkinter as tk

class App():
    def __init__(self):
        self.root = tk.Tk()
        
        self.stevilo1 = tk.Label(self.root,text='Število 1: ').grid(row=0,column=0)
        self.stevilo1 = tk.Label(self.root,text='Število 2: ').grid(row=1,column=0)
        self.rezultat = tk.Label(self.root,text='Rezultat')
        self.rezultat.grid(row=2,column=1)
        

        self.a = tk.Entry(self.root)
        self.b = tk.Entry(self.root)
        self.a.grid(row=0,column=1)
        self.b.grid(row=1,column=1)

        tk.Button(self.root,text = '+',command=self.sestej).grid(row=3,column=0)
        tk.Button(self.root,text = '-',command=self.odstej).grid(row=3,column=1)
        tk.Button(self.root,text = '/',command=self.zdeli).grid(row=3,column=2)
        tk.Button(self.root,text = '*',command=self.zmnozi).grid(row=3,column=3)

        self.root.mainloop()

    def sestej(self):
        self.rezultat.config(text= str(int(self.a.get()) + int(self.b.get())))

    def odstej(self):
        self.rezultat.config(text= str(int(self.a.get()) - int(self.b.get())))

    def zdeli(self):
        self.rezultat.config(text= str(float(self.a.get()) / float(self.b.get())))

    def zmnozi(self):
        self.rezultat.config(text= str(int(self.a.get()) * int(self.b.get())))
        







def main():
    app = App()



if __name__ == '__main__':
    main()



"""
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
        print('Produkt = '+str(a*b))"""