#-*- coding: cp1250 -*-

import Tkinter as tk

class App():
    def __init__(self):
        self.root = tk.Tk()

        self.imenik = {
            'aleš' : "046044021",
            'ana' : "046044021",
            'alex' : "046044021",
            'andrej' : "046044021",
            'anica' : "046044021",
            'anamarija' : "046044021",
            'anton' : "046044021",
            'bine' : "0123456789",
            'gaber' : "046044021",
            'gorazd' : "046044021",
            'martin' : "046044021",
        }

        self.stevilo1 = tk.Label(self.root,text='Prva črka imena: ').grid(row=0,column=0)
        self.rezultat = tk.Label(self.root,text='Rezultat')
        self.rezultat.grid(row=2,column=1)
        

        self.a = tk.Entry(self.root)
        self.a.grid(row=0,column=1)

        tk.Button(self.root,text = 'Dobi imena',command=self.dobiImena).grid(row=3,column=0)

        self.root.mainloop()

    def dobiImena(self):
        crka = self.a.get().lower()
        for x in self.imenik:
                if x.startswith(crka):
                    print(self.imenik[x])

        imena = [x.capitalize() +' : '+ self.imenik[x] for x in self.imenik if x.startswith(crka)]
        self.rezultat.config(text= '\n'.join(imena))







def main():
    app = App()



if __name__ == '__main__':
    main()



"""    
def main():
    imenik = {
        'aleš' : "046044021",
        'ana' : "046044021",
        'alex' : "046044021",
        'andrej' : "046044021",
        'anica' : "046044021",
        'anamarija' : "046044021",
        'anton' : "046044021",
        'bine' : "0123456789",
        'gaber' : "046044021",
        'gorazd' : "046044021",
        'martin' : "046044021",
    }
    while 1:
        k = input("Vnesi črko: ")
        while not k.isalpha():
            k = input('Vnesi ČRKO: ')
        else:
            for x in imenik:
                if x.startswith(k):
                    print(imenik[x])

if __name__ == '__main__':
    main()
"""