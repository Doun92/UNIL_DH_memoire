"""
Ce script sert à "noramliser" un texte, c'est-à-dire qu'il efface tout ce qui n'est pas un caractère alpabétique
"""
def read_file():

    import re
    import collections

    x_1 = input('Veuillez entrer le texte entrant : ')

    #Tentative d'ouverture du fichier
    try:
        #Ouvre et lit le fichier texte
        with open(x_1 + '.txt', 'r') as file:
            numLines = 0
            numWords = 0
            numChars = 0

            x_2 = input('Veuillez entrer le nom du fichier texte intermédiaire : ')
            with open(x_2 + '.txt', 'w+') as x_file:

                #Suppression de la ponctuation et des retours à la ligne
                for line in file:
                    # print(line)

                    for char in "1234567890''':;-.,_!?\"\n\t":
                        line = line.replace(char, ' ')

                    line = line.lower()

                    x_file.write(line)

                    all_lines = "".join(line)

                    #Liste des mots
                    wordList = line.split()

                    #Nombre de lignes
                    numLines += 1

                    #Nombre de mots
                    numWords += len(wordList)

                    #Nombre de caractères
                    numChars += len(line)


            print('Lines: %d\nWords: %d\nCharacters: %d' % (numLines, numWords, numChars))
            # print(line)


            # except IOError:
            #     print("Couldn't open file.")
            #     return


    except IOError:
        print("Couldn't open file.")
        return

read_file()
