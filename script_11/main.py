"""
Ce script unit tous les autres scrits qui s'occupent de tâches plus ponctuelles.
Il parcourt chaque mot, lettre par lettre ou syllabe par syllabe, selon les particularités de chacun.

auteur : Daniel Escoval
license : license UNIL
"""

class EvolutionPhonetique:

    def __init__(self):
        return

    def evolution_phonetique(self):

        from syllabifier import Syllabifier
        syllabifier = Syllabifier()

        from AA1_syllabe_initiale import SyllabeInitiale
        syllabe_initiale = SyllabeInitiale()

        from AA2_syllabe_contrepénultième import SyllabeContrepenultieme
        syllabe_contrepenultieme = SyllabeContrepenultieme()

        from AA3_syllabe_contrefinale import SyllabeContrefinale
        syllabe_contrefinale = SyllabeContrefinale()

        from AA4_syllabe_antépénultième_tonique import SyllabeAntePenultieme
        syllabe_ante_penultieme = SyllabeAntePenultieme()

        from AA5_syllabe_pénultième import SyllabePenultieme
        syllabe_penultieme = SyllabePenultieme()

        from AA6_syllabe_finale import SyllabeFinale
        syllabe_finale = SyllabeFinale()

        from AA7_conjugaison import Conjugaison
        conjugaison1 = Conjugaison()

        syllabes = syllabifier.syllabify(self)
        print(syllabes)

        changements = list()

        #Importation de librairies diverses
        import re
        import collections

        #Première syllabe et/ou préfixe
        if len(syllabes) > 0:
            changements.append(syllabe_initiale.syllabe_initiale(self))

        #Syllabe contrepénultième
        if len(syllabes) > 5:
            changements.append(syllabe_contrepenultieme.syllabe_contrepenultieme(self))

        #Syllabe contrefinale
        if len(syllabes) > 4:
            changements.append(syllabe_contrefinale.syllabe_contrefinale(self))

        #Anté-pénultième syllabe
        if len(syllabes) > 3:
            changements.append(syllabe_ante_penultieme.syllabe_ante_penultieme(self))

        #Pénultième syllabe
        if len(syllabes) > 2:
            changements.append(syllabe_penultieme.syllabe_penultieme(self))

        #Dernière syllabe
        if len(syllabes) > 1:
            changements.append(syllabe_finale.syllabe_finale(self))

        flat_list = [item for sublist in changements for item in sublist]
        # print(flat_list)

        output = "".join(flat_list)
        # print(output)
        output = output.lower()

        return output



# def main():
#
#     #Importation de librairies diverses
#     import re
#     import collections
#
#
#
#     #Importation du dictionnaire de tous les mots du texte
#     # from dictionary import dict
#     # from Mariale_1_dict import dict
#     from Moine_dict import dict
#     keys = dict.keys()
#     values = dict.values()
#     # print(keys)
#     # print(values)
#
#     every_word = open('AA_every_word.txt', 'w', encoding = 'utf-8')
#     catch = open('AA_catch.txt', 'w+', encoding = 'utf-8')
#     dont_catch = open('AA_dont_catch.txt', 'w+', encoding = 'utf-8')
#
#     # print(len(dict_Marie))
#
#     for key in keys:
#         # print(key)
#         # print(dict[key])
#         print_final = EvolutionPhonetique.evolution_phonetique(key)
#
#         every_word.write('\n %s > %s \n \n' % (key, print_final) + '----------------------------------------- \n' )
#         # print(print_final)
#
#         if print_final == dict[key] or print_final in dict[key] or print_final in dict[key][0]: #Ce serait ici qu'il faudrait modifier
#             catch.write('\n %s > %s == %s \n \n' % (key, print_final, dict[key]) + '----------------------------------------- \n')
#         else:
#             dont_catch.write(('\n %s > %s != %s \n \n' % (key, print_final, dict[key]) + '----------------------------------------- \n'))
#
# main()
