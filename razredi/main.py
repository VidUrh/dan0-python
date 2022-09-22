#-*- coding: cp1250 -*-
import Tkinter as tk

class App():
    def __init__(self):
        self.root = tk.Tk()
         #vpisnaSt,ime,letnik,ocene
        tk.Label(self.root,text='Ime: ').grid(row=0,column=0)
        tk.Label(self.root,text='Vpisna številka: ').grid(row=1,column=0)
        tk.Label(self.root,text='Letnik: ').grid(row=2,column=0)

        self.ime = tk.Entry(self.root)
        self.vpisna = tk.Entry(self.root)
        self.letnik = tk.Entry(self.root)
        self.ime.grid(row=0,column=1)
        self.vpisna.grid(row=1,column=1)
        self.letnik.grid(row=2,column=1)
        self.faks = Fakulteta()
        tk.Button(self.root,text = 'Vpiši',command=lambda : self.faks.vpisi(Student(self.vpisna.get(),self.ime.get(),self.letnik.get(),{}))).grid(row=3,column=0)
        tk.Button(self.root,text = 'Izpiši',command=lambda : self.faks.izpisi(Student(self.vpisna.get(),self.ime.get(),self.letnik.get(),{}))).grid(row=3,column=1)
        tk.Button(self.root,text = 'DobiImena',command=self.dobiImena).grid(row=3,column=2)
        
        tk.Label(self.root,text = 'Vpisani').grid(row = 0,column = 2)

        self.imena=tk.Label(self.root)
        self.imena.grid(row=1,column=2)

        self.root.mainloop()

    def dobiImena(self):
        imena = self.faks.vrniImena()
        self.imena.config(text='\n'.join(imena)) 
        print(imena)




class Student():
    def __init__(self,vpisnaSt,ime,letnik,ocene):
        self.vpisnaSt = vpisnaSt
        self.ime = ime
        self.letnik = letnik
        self.ocene = ocene

    def oceni(self,ocena,predmet):
        self.ocene[predmet].append(ocena)

    def napreduj(self):
        self.letnik+=1

class Fakulteta():
    def __init__(self):
        self.spisek = {}
    
    def vpisi(self,Student):
        self.spisek[Student.vpisnaSt] = Student
        print(self.spisek)
    
    def izpisi(self,Student):
        try:
            del self.spisek[Student.vpisnaSt]
        except KeyError:
            print('Študent ni vpisan')
    def vrniImena(self):
        return [self.spisek[x].ime for x in self.spisek]


if __name__=='__main__':
    App()
    s1 = Student('1234','Ante Emeršič',1,{'oe1':9})
    s2 = Student('4321','Mate Emeršič',1,{'oe1':6})
    faks = Fakulteta()
    faks.vpisi(s1)
    faks.vpisi(s2)
    faks.izpisi(s2)
    print(faks.spisek)