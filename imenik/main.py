#-*- coding: cp1250 -*-

import copy

def main():
    l1 = [2,3,4,4]
    l2 = copy.copy(l1)
    l2.append(3)
    print(l1)
    print(l2)


if __name__ == '__main__':
    main()