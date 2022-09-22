import pickle

if __name__ == "__main__":
    k = ''
    with open('tocka.pkl','rb') as h:
        k = pickle.load(h)
        print(k)