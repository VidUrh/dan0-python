import pickle

if __name__ == "__main__":
    l1 = [1, 2, 2, 5, 6, 7]

    with open('tocka.pkl','wb') as h:
        pickle.dump(l1,h, pickle.HIGHEST_PROTOCOL)