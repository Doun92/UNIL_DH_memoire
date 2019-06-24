import re
import collections

def read_one_string_file():

    # liste = open('liste_Mariale.txt', 'w+')

    #Tentative d'ouverture du fichier
    try:
        #Ouvre et lit le fichier texte
        x_1 = input('Veuillez entrer le fichier normalisé : ')
        with open(x_1 + '.txt', 'r') as file:

            x_2 = input('Veuillez entrer le nom du fichier de la liste de mots du texte étudié : ')
            liste = open(x_2 + '.txt', 'w+')

            #Suppression de la ponctuation et des retours à la ligne
            for line in file:
                words = line.split()
                word_counts = collections.Counter(words)
                for word, count in sorted(word_counts.items()):

                    liste.write('%s \n' % (word))


    except IOError:
        print("Couldn't open file.")
        return

read_one_string_file()
