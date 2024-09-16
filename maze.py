#generer un carre de n*n en input
import sys
import random 
def generator(n, nom_fichier):
    with open("mon_fichier", "w") as file:
        for i in range(n):
            file.write('#'*n + '\n')
    pass
    # recursion backtracking
    i = 0
    while True:
        i += 1
        if i > 200:
            break
        direction = ['N','E','S','W']
        random.shuffle(direction)
        print(direction)


if __name__ == "__main__":
    generator(int(sys.argv[1]),sys.argv[2])