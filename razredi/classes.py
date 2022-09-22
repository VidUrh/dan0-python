#-*- coding: cp1250 -*-

class Pravokotnik(object):
    barva = 'modra'
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def ploscina(self):
        return self.a*self.b


class Kvadrat(Pravokotnik):
    def __init__(self,a):
        super(Kvadrat,self).__init__(a,a)


if __name__=='__main__':
    p1 = Pravokotnik(13,24)
    p2 = Pravokotnik(23,10)
    k1 = Kvadrat(2)
    print(k1.ploscina())
    p1.barva='rdeča'
    print(p1.barva)
    print(p2.barva)
    print(p1.ploscina())
    print(p2.ploscina())
    del p1