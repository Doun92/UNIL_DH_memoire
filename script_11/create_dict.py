def create_dictionary():
        # dictionary = open('dictionary_Mariale_T.py', 'w+')

        try:
            #Ouvre et lit le fichier texte
            x_1 = input('Veuillez entre le nom de la liste : ')

            with open(x_1 + '.txt', 'r') as file:

                x_2 = input('Veuillez entrer le nom du dictionnaire de mots : ')
                dictionary = open(x_2 + '.py', 'w+', encoding = 'utf-8')

                dictionary.write('dict = { \n')
                for line in file:
                    for char in "\n":
                        line = line.replace(char, '')

                        strip = line.strip()

                        dictionary.write('" " : "%s", \n' % strip)

                dictionary.write('}')

        except IOError:
            print("Couldn't open file.")
            return

create_dictionary()
