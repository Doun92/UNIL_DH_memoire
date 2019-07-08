"""
auteur : Daniel Escoval
license : license UNIL
"""
import re

#Importation des autres scripts
# from vocalisme import Vocalisme
# vocalisme = Vocalisme()

# from vocalisme_non_tonique import VocalismeNonTonique
# vocalisme_non_tonique = VocalismeNonTonique()

# from consonantisme_initial import ConsonantismeInitial
# consonantisme_initial = ConsonantismeInitial()

# from consonantisme_final import ConsonantismeFinal
# consonantisme_final = ConsonantismeFinal()

from syllabifier import Syllabifier
syllabifier = Syllabifier()


#Listes de toutes les lettres traitées dans le script
listes_lettres = {
'toutes_les_voyelles' : ["A", "Á", "E", "Ẹ", "Ę", "I", "Í", "Ī", "O", "Ǫ", "Ọ", "U", "Ú", 'W', 'Y'],

'voyelles_toniques' : ["Ẹ", "Ę", "Á", "Ǫ", "Ọ", "Ú", 'Í'],

'voyelles_atones' : ["A", "E", "U", "I", "O"],

'voyelles_atones_sans_A' : ["E", "U", "I", "O"],

'consonnes_et_semi_consonnes' : ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],

'consonantisme_complexe_2_lettres' : [
'CB', 'DC', 'FB', 'GB', 'HB', 'LB', 'MB', 'NB', 'PB', 'RB', 'SB', 'TB', 'VB', 'YB',
'BC', 'DC', 'FC', 'GC', 'HC', 'LC', 'MC', 'NC', 'PC', 'RC', 'SC', 'TC', 'VC', 'YC',
'BD', 'CD', 'FD', 'GD', 'HD', 'LD', 'MD', 'ND', 'PD', 'RD', 'SD', 'TD', 'VD', 'YD',
'BJ', 'CJ', 'DJ', 'FJ', 'GJ', 'HJ', 'LJ', 'MJ', 'NJ', 'PJ', 'RJ', 'SJ', 'TJ', 'VJ', 'YJ',
'BL', 'CL', 'DL', 'FL', 'GL', 'HL', 'LL', 'ML', 'NL', 'PL', 'RL', 'SL', 'TL', 'VL', 'YL',
'BM', 'CM', 'DM', 'FM', 'GM', 'HM', 'LM', 'MM', 'NM', 'PM', 'RM', 'SM', 'TM', 'VM', 'YM',
'BN', 'CN', 'DN', 'FN', 'GL', 'HL', 'LN', 'MN', 'NN', 'PN', 'RN', 'SN', 'TN', 'VN', 'YN',
'BP', 'CP', 'DP', 'FP', 'GP', 'HP', 'LP', 'MP', 'NP', 'RP', 'SP', 'TP', 'VP', 'YP',
'BR', 'CR', 'DR', 'FR', 'GR', 'HR', 'LR', 'MR', 'NR', 'PR', 'RR', 'SR', 'TR', 'VR', 'YR',
'BS', 'CS', 'DS', 'FS', 'GS', 'HS', 'LS', 'MS', 'NS', 'PS', 'RS', 'SS', 'TS', 'VS', 'YS',
'BT', 'CT', 'DT', 'FT', 'GT', 'HT', 'LT', 'MT', 'NT', 'PT', 'RT', 'ST', 'VT', 'YT'
'BW', 'CW', 'DW', 'FW', 'GW', 'HW', 'LW', 'MW', 'NW', 'PW', 'QW', 'RW', 'SW', 'TW', 'VW', 'YW',
'BY', 'CY', 'DY', 'FY', 'GY', 'HY', 'LY', 'MY', 'NY', 'PY', 'QY', 'RY', 'SY', 'TY', 'VY', 'YY',
],

'consonantisme_explosif_complexe_3_lettres' : [
'SBR', 'SCR', 'SDR', 'SLR', 'SPR', 'STR',
],
}

class SyllabeInitiale:

    def __init__(self):
        return

    def syllabe_initiale(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #Consoantisme initial
        if syllabes[0][0] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[0][0] == 'B':
                #Consonantisme complexe
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    if syllabes[0][1] == 'Y':
                        changements.append('g')
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    #Nous avons préféré généraliser la règle à toutes les consonnes ou semi consonnes sauf Y
                    else:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                #Consonantisme simple
                else:
                    changements.append(syllabes[0][0])

            #Gestion de C
            elif syllabes[0][0] == 'C':
                #Consonantisme complexe
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    if syllabes[0][1] == 'H':
                        changements.append('ch')
                    elif syllabes[0][1] == 'Y':
                        if syllabes[0][2] == 'O':
                            changements.append('ç')
                        else:
                            changements.append('c')
                    elif syllabes[0][1] == 'W':
                        changements.append('c')
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    else:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                #Consonantisme simple
                else:
                    #Palatalisation de C devant A
                    if syllabes[0][1] in ['A', 'Á']:
                        changements.append('ch')
                    else:
                        changements.append(syllabes[0][0])

            #Gestion de D
            elif syllabes[0][0] == 'D':
                #Consonantisme complexe
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    if syllabes[0][1] == 'Y':
                        #Attaque
                        if syllabes[0][2] in ['E', 'Ọ', 'Ǫ', 'Ú', 'O']:
                            changements.append('j')
                        elif syllabes[0][2] == 'A':
                            changements.append('de')
                        else:
                            changements.append('g')
                    elif syllabes[0][1] == 'W':
                        changements.append('d')
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    else:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                #Consonantisme simple
                else:
                    changements.append(syllabes[0][0])

            #Gestion de F
            elif syllabes[0][0] == 'F':
                #Consonantisme complexe
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    changements.append(syllabes[0][0] + syllabes[0][1])
                #Consonantisme simple
                else:
                    changements.append(syllabes[0][0])

            #Gestion de G
            elif syllabes[0][0] == 'G':
                #Consonantisme complexe
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    if syllabes[0][1] == 'Y':
                        if syllabes[0][2] == 'Ǫ':
                            changements.append('ge')
                        else:
                            changements.append('g')
                    elif syllabes[0][1] == 'W':
                        changements.append('g')
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    else:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                else:
                    #Palatalisation de G devant A (graphie en j)
                    if syllabes[0][1] in ['A', 'Á']:
                        changements.append('j')
                    else:
                        changements.append(syllabes[0][0])

            #Gestion de H (surtout utile pour les mots provenant du germain)
            elif syllabes[0][0] == 'H':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][1])
                else:
                    changements.append('')

            #Gestion de J (Surtout utile pour les mots provenant du germain)
            elif syllabes[0][0] == 'J':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de K (Surtout utile pour les mots provenant du germain)
            elif syllabes[0][0] == 'K':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[0][1] == 'W':
                        changements.append('qu')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de L
            elif syllabes[0][0] == 'L':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de M
            elif syllabes[0][0] == 'M':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de N
            elif syllabes[0][0] == 'N':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de P
            elif syllabes[0][0] == 'P':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #L'occlusive sourde labiale se singularise
                    if syllabes[0][1] == 'Y':
                        changements.append('ch')
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    else:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de Q
            elif syllabes[0][0] == 'Q':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    if syllabes[0][1] == 'W':
                        if syllabes[0][2] in ['A', 'Ọ']:
                            changements.append('c')
                        else:
                            changements.append('qu')
                    else:
                        changements.append('c')
                else:
                    changements.append(syllabes[0][0])

            #Gestion de R
            elif syllabes[0][0] == 'R':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de S
            elif syllabes[0][0] == 'S':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[0][1] + syllabes[0][2] == 'CL':
                        changements.append('escl')
                    elif syllabes[0][1] + syllabes[0][2] == 'TR':
                        changements.append('estr')
                    elif syllabes[0][1] + syllabes[0][2] == 'CR':
                        changements.append('escr')
                    elif syllabes[0][1] == 'C':
                        if syllabes[0][2] in ['A', 'Á']:
                            changements.append('esch')
                        else:
                            changements.append('esc')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[0][1] == 'W':
                        changements.append(syllabes[0][0])
                    #La sifflante sourde se palatalise au contact du yod
                    elif syllabes[0][1] == 'Y':
                        changements.append('s')
                    else:
                        #Prosthèse
                        changements.append('e'+ syllabes[0][0] + syllabes[0][1])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de T
            elif syllabes[0][0] == 'T':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    if syllabes[0][1] == 'W':
                        changements.append(syllabes[0][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[0][1] == 'Y':
                        if syllabes[0][2] in ['A', 'O', 'Ọ', 'Ǫ', 'U', 'Ú']:
                            changements.append('ç')
                        else:
                            changements.append('c')
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    else:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de V (wau ancien)
            elif syllabes[0][0] == 'V':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    if syllabes[0][1] == 'Y':
                        changements.append('j')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    if syllabes[0][1] == 'A':
                        if len(syllabes[0]) > 2 and syllabes[0][2] in ['D', 'L', 'S']:
                            changements.append('v')
                        elif len(syllabes) > 1 and syllabes[1][0] == 'D':
                            changements.append('v')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[0][0])

            #Gestion de W (wau récent) (Probablement inexistant en cette position)
            elif syllabes[0][0] == 'W':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[0][1] == 'Y':
                        changements.append('j')
                    else:
                        changements.append(syllabes[0][0])
                else:
                    if syllabes[0][1] in ['Á', 'E', 'Ẹ', 'Ę', 'I', 'Í']:
                        changements.append('gu')
                    else:
                        changements.append('g')

            #Gestion de X (Probablement inexistant en cette position)
            elif syllabes[0][0] == 'X':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

            #Gestion de Y
            elif syllabes[0][0] == 'Y':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append('j')

            #Gestion de Z (Probablement inexistant en cette position)
            elif syllabes[0][0] == 'Z':
                if syllabes[0][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[0][0])
                else:
                    changements.append(syllabes[0][0])

        #Vocalisme contretonique
        #A
        if 'A' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                if len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['BÚ', 'WÚ']:
                    changements.append('e')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['DY', 'GN']:
                    changements.append('ai')
                #Fermeture à cause de la séquence BW
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['BW', 'PW']:
                    if len(syllabes) > 2 and syllabes[2][0] + syllabes[2][1] == 'SS':
                        changements.append('eu')
                    else:
                        changements.append('o')
                else:
                    changements.append('a')
            #Si A se trouve en position ouvert
            elif syllabes[0][-1] == 'A':
                #Fermeture de A face à O
                if len(syllabes) > 1 and syllabes[1][0] in ['Ọ', 'Ú']:
                    changements.append('e')
                elif len(syllabes) > 1 and syllabes[0][-2] in ['C', 'G'] and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['BÁ', 'LÍ', 'PẸ']:
                    changements.append('e')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['GỌ', 'VỌ', 'WÚ', 'PR', 'PW']:
                    changements.append('e')
                elif len(syllabes) > 1 and syllabes[1][0] == 'X':
                    changements.append('ai')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] == 'TY':
                    changements.append('ai')
                elif (len(syllabes[0]) > 1 or len(syllabes[0]) > 2) and syllabes[0][0] + syllabes[0][1] in ['GR', 'SM']:
                    changements.append('e')
                elif len(syllabes) > 2 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] + syllabes[2][0] == 'BRC':
                    changements.append('o')
                #Fermeture due à la séquence CW
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] == 'CW':
                    if len(syllabes) > 2 and syllabes[2][0] + syllabes[2][1] == 'SS':
                        changements.append('eu')
                    else:
                        changements.append('o')
                else:
                    changements.append('a')
            #Si A se trouve en position pénultième
            elif syllabes[0][-2] == 'A':
                #Diphtongue AU
                if syllabes[0][-1] == 'U':
                    if len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] == 'DY':
                        changements.append('oi')
                    elif len(syllabes) > 1 and len(syllabes[1]) > 2 and syllabes[1][0] + syllabes[1][1] + syllabes[1][2] == 'DWĪ':
                        changements.append('oi')
                    else:
                        changements.append('o')
                elif syllabes[0][-1] == 'X':
                    changements.append('ai')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['CT', 'YY', 'YD', 'PT', 'NX', 'SY', 'YL']:
                    changements.append('ai')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] + syllabes[1][1] in ['NDY', 'NGR', 'SSY']:
                    changements.append('ai')
                #Fermeture due à la séquence QW
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'QW':
                    changements.append('e')
                #Fermeture sur un monosyllabique
                elif len(syllabes) == 1 and syllabes[0][-1] == 'G':
                    changements.append('ou')
                else:
                    changements.append('a')
            #Si se trouve en position antépénultième
            elif syllabes[0][-3] == 'A':
                #Diphtongue AU
                if syllabes[0][-2] == 'U':
                    if len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'SY':
                        changements.append('oi')
                    else:
                        changements.append('o')
                elif syllabes[0][-2]+ syllabes[0][-1] in ['NT', 'ST']:
                    changements.append('ai')
                else:
                    changements.append('a')
            #Tous les autres cas de figure
            else:
                changements.append('a')

        #E
        elif 'E' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                changements.append('e')
            #Si E se trouve en position ouvert
            elif syllabes[0][-1] == 'E':
                if len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['BÚ', 'CR']:
                    changements.append('i')
                elif len(syllabes[0]) > 2 and syllabes[0][0] + syllabes[0][1] == 'PR':
                    if len(syllabes) > 1 and syllabes[1][0] == 'M':
                        changements.append('e')
                    else:
                        changements.append('i')
                #Fermeture à cause de la séquence DW
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] == 'DW':
                    changements.append('eu')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['GN', 'TY']:
                    changements.append('ei')
                else:
                    changements.append('e')
            #Si E se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'E':
                if len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['DT', 'YT', 'NY']:
                    changements.append('ei')
                else:
                    changements.append('e')
            #Si se trouve en position antépénultième
            elif syllabes[0][-3] == 'E':
                changements.append('e')
            #Tous les autres cas de figure
            else:
                changements.append('e')

        #I
        elif 'I' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                changements.append('i')
            #Si I se trouve en position ouvert
            elif syllabes[0][-1] == 'I':
                changements.append('i')
            #Si I se trouve en position pénultième
            elif syllabes[0][-2] == 'I':
                changements.append('i')
            #Si se trouve en position antépénultième
            elif syllabes[0][-3] == 'I':
                changements.append('i')
            #Tous les autres cas de figure
            else:
                changements.append('i')

        #O
        elif 'O' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                if len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'CL':
                    changements.append('e')
                else:
                    changements.append('o')
            #Si O se trouve en position ouvert
            elif syllabes[0][-1] == 'O':
                #Fermeture due à la séquence TW
                if len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] == 'TW':
                    changements.append('eu')
                #Fermeture due à la séquence CW
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] == 'CW':
                    changements.append('e')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['DY']:
                    changements.append('ui')
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('oi')
                else:
                    changements.append('o')
            #Si O se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'O':
                if len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'VW':
                    changements.append('eu')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'GD':
                    changements.append('ou')
                else:
                    changements.append('o')
            #Si se trouve en position antépénultième
            elif syllabes[0][-3] == 'O':
                if syllabes[0][-2] + syllabes[0][-1] == 'CS':
                    changements.append('oi')
                else:
                    changements.append('o')
            #Tous les autres cas de figure
            else:
                changements.append('o')

        #U
        elif 'U' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                changements.append('u')
            #Si U se trouve en position ouvert
            elif syllabes[0][-1] == 'U':
                changements.append('u')
            #Si U se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'U':
                if len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'ND':
                    changements.append('ai')
                else:
                    changements.append('u')
            #Si se trouve en position antépénultième
            elif syllabes[0][-3] == 'U':
                changements.append('u')
            #Tous les autres cas de figure
            else:
                changements.append('u')

        #Vocalisme tonique
        #Á tonique
        if 'Á' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                #influence des nasales
                if len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    changements.append('ai')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['CW']:
                    changements.append('ui')
                elif syllabes[1] == 'BWĪ':
                    changements.append('oi')
                else:
                    changements.append('e')
            #Si A tonique se trouve en position ouverte
            elif syllabes[0][-1] == 'Á':
                #Loi de Bartsh
                if syllabes[0][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[0]) > 2 and syllabes[0][-3] + syllabes[0][-2] in ['CT', 'TY']:
                    changements.append('ie')
                #influence des nasales
                elif len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    changements.append('ai')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['BY', 'CL']:
                    changements.append('ai')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['RY']:
                    changements.append('ie')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'BW':
                    changements.append('o')
                else:
                    changements.append('e')
            #Si A tonique se trouve au milieu de la syllabe
            elif syllabes[0][-2] == 'Á':
                #Loi de Bartsh
                if syllabes[0][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[0]) > 2 and syllabes[0][-3] + syllabes[0][-2] in ['CT']:
                    changements.append('ie')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['NC', 'NT', 'NX', 'SY', 'YL']:
                    if syllabes[1][1] == 'R':
                        changements.append('a')
                    else:
                        changements.append('ai')
                else:
                    changements.append('a')
            #Si se trouve en position antépénultième
            elif syllabes[0][-3] == 'Á':
                #Loi de Bartsh
                if syllabes[0][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[0]) > 2 and syllabes[0][-3] + syllabes[0][-2] in ['CT']:
                    changements.append('ie')
                elif syllabes[0][-2] + syllabes[0][-1] == 'BT':
                    changements.append('o')
                elif syllabes[0][-2] + syllabes[0][-1] == 'NS':
                    changements.append('ai')
                elif syllabes[0][-2] + syllabes[0][-1] == 'PT':
                    changements.append('e')
                else:
                    changements.append('a')
            #Autres cas de figure, plus rare ou A tonique ne se trouve dans aucune de ces positions
            else:
                changements.append('a')

        #Ẹ fermé
        elif 'Ẹ' in syllabes[0]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                #influence des nasales
                if len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    if syllabes[1][1] == 'A':
                        changements.append('ei')
                    elif syllabes[1][-1] == 'Ī':
                        changements.append('i')
                    else:
                        changements.append('e')
                #Métaphonie
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('i')
                #Anaphonie
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    changements.append('i')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['BY', 'CY', 'DY', 'FY', 'GY', 'LY', 'RY', 'TY', 'VY']:
                    changements.append('i')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['BR', 'GA', 'GÁ', 'GĘ', 'GE', 'GI', 'GÍ', 'GN']:
                    changements.append('i')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position ouverte
            elif syllabes[0][-1] == 'Ẹ':
                if len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    if syllabes[1][1] == 'A':
                        changements.append('ei')
                    elif syllabes[1] == syllabes[-1] and syllabes[1][1] in ['E', 'U', 'I', 'O'] and syllabes[1][1] == syllabes[1][-1] or len(syllabes[1]) > 2 and syllabes[1][2] == 'S':
                        changements.append('ei')
                    elif syllabes[1][-1] == 'Ī':
                        changements.append('i')
                    else:
                        changements.append('e')
                elif len(syllabes) > 1 and len(syllabes[1]) > 2 and syllabes[1][0] + syllabes[1][1] + syllabes[1][2] in ['BWĪ']:
                    changements.append('ui')
                #Fermeture due aux séquences DW et TW
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['DW', 'GW', 'TW']:
                    if syllabes[1][-1] == 'Ī':
                        changements.append('ui')
                    else:
                        changements.append('u')
                #Fermeture à cause de la séquence BW:
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] == 'BW':
                    changements.append('e')
                #Fermeture à cause de la séquence CW:
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] == 'CW':
                    if syllabes[1][-1] == 'Ī':
                        changements.append('ui')
                    else:
                        changements.append('eu')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['BY', 'CY', 'DY', 'FY', 'GY', 'LY', 'RY', 'TY', 'VY']:
                    changements.append('i')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['GA', 'GÁ', 'GĘ', 'GE', 'GI', 'GÍ', 'GN']:
                    changements.append('i')
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                elif syllabes[0][-2] == 'C':
                    if syllabes[1][0] + syllabes[1][1] == 'CR':
                        changements.append('ei')
                    else:
                        changements.append('i')
                    #Métaphonie
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('i')
                    #Anaphonie
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    changements.append('i')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position fermée
            elif syllabes[0][-2] == 'Ẹ':
                #influence des nasales
                if syllabes[0][-1] in ['M', 'N']:
                    #Contact avec un groupe consonantique dégageant un yod
                    if len(syllabes) > 1 and syllabes[1][0] == 'C':
                        if syllabes[1][1] == 'Y':
                            changements.append('e')
                        else:
                            changements.append('ei')
                    elif len(syllabes) > 1 and syllabes[1][0] in ['R', 'W']:
                        changements.append('i')
                    elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                        changements.append('i')
                    else:
                        changements.append('e')
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                #Fermeture en [i]
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['YS', 'SR', 'SY', 'YY']:
                    changements.append('i')
                #Fermeture due au groupe VW
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'VW':
                    if syllabes[1][-1] == 'Ī':
                        changements.append('ui')
                    else:
                        changements.append('u')
                #influence d'un I long
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('i')
                #Problème lors de la répartition des syllabes
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['CT', 'SC']:
                    if syllabes[0][-3] == 'Y':
                        changements.append('i')
                    else:
                        changements.append('ei')
                elif len(syllabes[0]) > 2 and syllabes[0][-3] == 'C':
                    changements.append('i')
                elif len(syllabes) == 1 and syllabes[0][-1] == 'S':
                    changements.append('ei')
                else:
                    changements.append('e')
            #Si se trouve en position antépénultième
            elif syllabes[0][-3] == 'Ẹ':
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                if syllabes[0][-2] == 'C':
                    changements.append('i')
                elif syllabes[0][-2] + syllabes[0][-1] == 'ST':
                    changements.append('i')
                #Métaphonie
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('i')
                else:
                    changements.append('e')
            #Si E fermé se trouve en position fermée
            else:
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                if syllabes[0][-2] == 'C':
                    changements.append('i')
                #Métaphonie
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('i')
                else:
                    changements.append('e')

        #Ę ouvert
        elif 'Ę' in syllabes[0]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                if len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['CT', 'BY', 'SY', 'TY']:
                    changements.append('i')
                elif len(syllabes) > 1 and syllabes[1][0] == 'X':
                    changements.append('i')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['TW']:
                    changements.append('ui')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['CW']:
                    changements.append('iu')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'BL':
                    changements.append('ie')
                else:
                    changements.append('je')
            #Si E ouvert se trouve en position finale
            elif syllabes[0][-1] == 'Ę':
                #Contact avec un groupe dégageat un yod
                if len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['CT', 'BY', 'SY', 'TY']:
                    changements.append('i')
                elif len(syllabes) > 1 and syllabes[1][0] == 'X':
                    changements.append('i')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['TW']:
                    changements.append('ui')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['CW']:
                    changements.append('iu')
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('i')
                else:
                    changements.append('ie')
            #Si E ouvert se trouve en position pénultième
            elif syllabes[0][-2] == 'Ę':
                #Influence d'une nasale finale
                if syllabes[0][-1] == syllabes[-1][-1] == 'M':
                    changements.append('ie')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['MT', 'RT', 'PT', 'TT', 'PD', 'DC']:
                    changements.append('ie')
                #Contact avec un groupe dégageant un yod
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['CT', 'SY', 'YC', 'YD', 'YY', 'YN', 'QW']:
                    changements.append('i')
                elif len(syllabes) == 1 and syllabes[0][-1] == 'T':
                    changements.append('oi')
                else:
                    changements.append('e')
            #Si E ouvert se trouve en position antépénultième
            elif syllabes[0][-3] == 'Ę':
                if len(syllabes) == 1 and syllabes[0][-2] + syllabes[0][-1] == 'YS':
                    changements.append('oi')
                else:
                    changements.append('e')
            #Si E ouvert se trouve en position fermée
            else:
                changements.append('e')

        #Í tonique
        elif 'Í' in syllabes[0]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[0]) == 1:
                changements.append('i')
            #Si I tonique se trouve en position finale
            elif syllabes[0][-1] == 'Í':
                #Fermeture de I face à O
                if len(syllabes) > 1 and syllabes[1][0] == 'O':
                    changements.append('iu')
                elif len(syllabes) == 2 and syllabes[1][0] + syllabes[1][1] == 'NE':
                    changements.append('a')
                else:
                    changements.append('i')
            #Si I tonique se trouve en position pénultième
            elif syllabes[0][-2] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position antépénultième
            elif syllabes[0][-3] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position fermée
            else:
                changements.append('i')

        #Ọ fermé
        elif 'Ọ' in syllabes[0]:
            if len(syllabes[0]) == 1:
                #influence des nasales
                if len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    changements.append('o')
                #Métaphonie
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('u')
                #Anaphonie
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    changements.append('u')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['BY', 'CY', 'DY', 'FY', 'GY', 'LY', 'RY', 'TY', 'VY']:
                    changements.append('u')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['GA', 'GÁ', 'GĘ', 'GE', 'GI', 'GÍ', 'GN']:
                    changements.append('u')
                else:
                    changements.append('ou')
            #Si O fermé se trouve en position finale
            elif syllabes[0][-1] == 'Ọ':
                #influence des nasales
                if len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    changements.append('o')
                #Action fermante de la palatale sourde devant I et E
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['CI', 'CE', 'GN']:
                    changements.append('oi')
                #Métaphonie
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('u')
                #Anaphonie
                elif len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    changements.append('u')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['BY', 'CY', 'DY', 'FY', 'GY', 'LY', 'RY', 'TY', 'VY']:
                    changements.append('u')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['GÁ', 'GĘ', 'GE', 'GI', 'GÍ', 'GN']:
                    changements.append('u')
                else:
                    changements.append('ou')
            #Si O fermé se trouve en position pénultième
            elif syllabes[0][-2] == 'Ọ':
                #Métaphonie
                if len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    if syllabes[0][-1] + syllabes[1][0] == 'TT':
                        changements.append('ui')
                    else:
                        changements.append('u')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] + syllabes[1][1] in ['STR', 'STY', 'YTS']:
                    changements.append('ui')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['SY', 'VY']:
                    changements.append('ui')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'GT':
                    changements.append('u')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'MN':
                    changements.append('a')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['NG', 'NT', 'NY']:
                    if syllabes[1][1] == syllabes[-1][-1] == 'A':
                        changements.append('o')
                    else:
                        changements.append('oi')
                elif len(syllabes) > 1 and syllabes[0][-1] == 'L' and syllabes[1] == 'CA':
                    changements.append('o')
                elif len(syllabes) == 1 and syllabes[0][-1] == 'S':
                    changements.append('ou')
                else:
                    changements.append('o')
            #Si O fermé se trouve en position antépénultième
            elif syllabes[0][-3] == 'Ọ':
                #Métaphonie
                if len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('u')
                else:
                    changements.append('o')
            #Toutes les autres positions
            else:
                #Métaphonie
                if len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('u')
                else:
                    changements.append('o')

        #Ǫ ouvert
        elif 'Ǫ' in syllabes[0]:
            if len(syllabes[0]) == 1:
                #influence des nasales
                if len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    if syllabes[1][1] in ['E', 'O']:
                        changements.append('ue')
                    else:
                        changements.append('o')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['CT', 'CW']:
                    changements.append('ui')
                else:
                    changements.append('ue')
            #Si O ouvert se trouve en position finale
            elif syllabes[0][-1] == 'Ǫ':
                #influence des nasales
                if len(syllabes) > 1 and syllabes[1][0] in ['M', 'N']:
                    if syllabes[1][1] in ['E', 'O']:
                        changements.append('ue')
                    else:
                        changements.append('o')
                elif len(syllabes) > 1 and syllabes[1][0] in ['X']:
                    changements.append('ui')
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] in ['CR', 'CW', 'PR', 'TY']:
                    changements.append('ui')
                    #fermeture due à la séquence TW
                elif len(syllabes) > 1 and len(syllabes[1]) > 1 and syllabes[1][0] + syllabes[1][1] == 'TW':
                    changements.append('ou')
                elif len(syllabes) > 1 and syllabes[1][-1] == 'Ī':
                    changements.append('oi')
                #Fermeture dü à une attaque très forte
                elif len(syllabes[0]) > 3 and syllabes[0][0] + syllabes[0][1] + syllabes[0][2] == 'SCR':
                    changements.append('oe')
                else:
                    changements.append('ue')
            #Si O ouvert se trouve en position pénultième
            elif syllabes[0][-2] == 'Ǫ':
                #Présence d'un groupe consonantique dégageant un yod
                if len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['CT', 'ST', 'YY', 'XM']:
                    changements.append('ui')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] + syllabes[1][1] == 'SSY':
                    changements.append('ui')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['CD', 'YN']:
                    changements.append('oi')
                elif len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] in ['VN', 'VT']:
                    changements.append('ue')
                else:
                    changements.append('o')
            #Si O ouvert se trouve en position antépénultième
            elif syllabes[0][-3] == 'Ǫ':
                if syllabes[0][-2] + syllabes[0][-1] in ['CT', 'YS']:
                    changements.append('ui')
                else:
                    changements.append('o')
            #Toutes les autres positions
            else:
                changements.append('o')

        #Ú tonique
        elif 'Ú' in syllabes[0]:
            if len(syllabes[0]) == 1:
                changements.append('u')
            #Si U tonique se trouve en position finale
            elif syllabes[0][-1] == 'Ú':
                changements.append('u')
            #SiU tonique se trouve en position pénultième
            elif syllabes[0][-2] == 'Ú':
                if len(syllabes) > 1 and syllabes[0][-1] + syllabes[1][0] == 'CT':
                    changements.append('ui')
                else:
                    changements.append('u')
            #Si U tonique se trouve en position antépénultième
            elif syllabes[0][-3] == 'Ú':
                if syllabes[0][-2] + syllabes[0][-1] == 'ST':
                    changements.append('ui')
                else:
                    changements.append('u')
            #Toutes les autres positions
            else:
                changements.append('u')

        #Consonantisme final
        if syllabes[0][-1] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[0][-1] == 'B':
                if len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'TR':
                    changements.append('z')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de C
            elif syllabes[0][-1] == 'C':
                if syllabes[0][-2] == 'N':
                    changements.append('nc')
                elif len(syllabes) == 1:
                    if syllabes[0][-2] in ['Í', 'Ǫ']:
                        changements.append('')
                    else:
                        changements.append('i')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de D
            elif syllabes[0][-1] == 'D':
                if len(syllabes) == 1:
                    if syllabes[0][-2] + syllabes[0][-1] == 'ND':
                        changements.append('nt')
                    else:
                        changements.append('t')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de F
            elif syllabes[0][-1] == 'F':
                if len(syllabes) > 1 and syllabes[0][-2] == 'Ọ' and syllabes[1][0] + syllabes[1][1] == 'FR':
                    changements.append('f')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de G
            elif syllabes[0][-1] == 'G':
                #Assimilation au N suivant
                if len(syllabes) > 1 and syllabes[1][0] == 'N':
                    if syllabes[1] == syllabes[-1]:
                        changements.append('')
                    else:
                        changements.append('g')
                elif len(syllabes) > 1 and syllabes[0][-2] in ['A', 'Ẹ', 'Ọ'] and syllabes[1][0] in ['S', 'D', 'T']:
                    changements.append('i')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de H (ne devrait pas exister ou cas très très rare)
            elif syllabes[0][-1] == 'H':
                changements.append('')

            #Gestion de L
            elif syllabes[0][-1] == 'L':
                if len(syllabes) > 1 and syllabes[1][0] == 'L':
                    if syllabes[0][-2] in ['A', 'E'] and syllabes[1][1] in ['Ę', 'Ọ']:
                        changements.append('l')
                    else:
                        changements.append('')
                elif len(syllabes) > 1 and syllabes[1][0] == ' ':
                    changements.append('l')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'GR':
                    if syllabes[0][-2] == 'Ọ':
                        changements.append('u')
                    else:
                        changements.append('l')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'CT':
                    changements.append('l')
                elif len(syllabes) > 1 and syllabes[0][-2] == syllabes[0][0] == 'Á' and syllabes[1][0] == 'M':
                    changements.append('r')
                elif len(syllabes) > 1 and syllabes[1] == syllabes[-1] and syllabes[1][0] == 'V':
                    if syllabes[0][-2] == 'Ǫ':
                        changements.append('u')
                    else:
                        changements.append('l')
                elif len(syllabes) == 1:
                    changements.append('l')
                else:
                    #La liquide se vocalise en [w]
                    changements.append('u')

            #Gestion de M
            elif syllabes[0][-1] == 'M':
                if len(syllabes) > 1 and syllabes[1][0] in ['B', 'C', 'T', 'Y']:
                    if syllabes[0][-2] == 'Í' and syllabes[1] == syllabes[-1] == 'YU':
                        changements.append('ng')
                    else:
                        changements.append('n')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] in ['BY', 'QW']:
                    changements.append('n')
                elif len(syllabes) > 1 and syllabes[1][0] == 'P':
                    if syllabes[0][-2] == 'O':
                        changements.append('m')
                    else:
                        changements.append('n')
                elif len(syllabes) > 1 and syllabes[1][0] == 'M':
                    changements.append('')
                else:
                    #Position de finale absolue pour les monosyllabiques
                    if len(syllabes) == 1:
                        changements.append('n')
                    else:
                        #Assimilation à la consonne suivante
                        changements.append('m')

            #Gestion de N
            elif syllabes[0][-1] == 'N':
                if len(syllabes) > 1 and syllabes[1][0] == 'Y':
                    if syllabes[1][1] in ['A', 'C', 'Ọ', 'Ǫ']:
                        changements.append('gn')
                    else:
                        changements.append('ng')
                elif len(syllabes) > 1 and syllabes[1][0] == 'N':
                    changements.append('')
                elif len(syllabes) > 1 and syllabes[1][0] + syllabes[1][1] == 'DY':
                    changements.append('gn')
                else:
                    changements.append('n')

            #Gestion de P
            elif syllabes[0][-1] == 'P':
                #Si c'est un mot venant de l'adstrat grec
                if len(syllabes) > 1 and syllabes[1][0] == 'H':
                    changements.append('p')
                elif len(syllabes) > 1 and syllabes[1][0] == 'P':
                    if len(syllabes) > 1 and syllabes[0][-2] == 'A' and syllabes[1][1] == 'Ę':
                        changements.append('p')
                    else:
                        changements.append('')
                else:
                #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de Q
            elif syllabes[0][-1] == 'Q':
                if len(syllabes) > 1:
                    if syllabes[1][0] == 'W':
                        if syllabes[0][-2] in ['A', 'Ę', 'Í'] and syllabes[1][1] in ['A', 'R']:
                            changements.append('v')
                        elif syllabes[0][-2] in ['E', 'Í'] and syllabes[1][1] in ['Ę', 'U']:
                            changements.append('')
                        else:
                            changements.append('u')
                    else:
                        changements.append('')
                else:
                    changements.append('')

            #Gestion de R
            elif syllabes[0][-1] == 'R':
                if len(syllabes) > 1 and syllabes[1][0] == 'R':
                    if syllabes[0][-2] in ['E', 'Ę', 'O'] and syllabes[1][1] in ['A', 'Ọ']:
                        changements.append('r')
                    else:
                        changements.append('')
                else:
                    #La vibrante est très stable
                    changements.append(syllabes[0][-1])

            #Gestion de S
            elif syllabes[0][-1] == 'S':
                #Pluriel des mots monosyllabiques
                if syllabes[0][-2] in listes_lettres['consonnes_et_semi_consonnes']:
                    if len(syllabes) == 1 and syllabes[0][-2] == 'C':
                        changements.append('z')
                    elif syllabes[0][-2] in ['P', 'Y']:
                        changements.append('s')
                    else:
                        changements.append(syllabes[0][-2] + 's')
                elif len(syllabes) > 1 and syllabes[1][0] == 'S':
                    if syllabes[0][-2] in ['A', 'E', 'Ẹ', 'Ǫ', 'U'] and syllabes[1][1] in ['A', 'Á', 'Ę', 'Í', 'Y']:
                        changements.append('s')
                    else:
                        changements.append('')
                elif len(syllabes) > 1 and len(syllabes[1]) > 2 and syllabes[1][0] + syllabes[1][1] + syllabes[1][2] == 'TYS':
                    changements.append('')
                else:
                    changements.append('s')

            #Gestion de T
            elif syllabes[0][-1] == 'T':
                if len(syllabes) == 1:
                    if syllabes[0][-2] + syllabes[0][-1] == 'CT':
                        changements.append('st')
                    elif syllabes[0][-2] + syllabes[0][-1] in ['BT', 'PT']:
                        changements.append('t')
                    elif syllabes[0][-2] in listes_lettres['toutes_les_voyelles']:
                        changements.append('t')
                    else:
                        changements.append(syllabes[0][-2] + syllabes[0][-1])
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de V
            elif syllabes[0][-1] == 'V':
                if syllabes[0][-2] == 'Í' and syllabes[1][0] == 'R':
                    changements.append('v')
                else:
                #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de W
            elif syllabes[0][-1] == 'W':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de X
            elif syllabes[0][-1] == 'X':
                changements.append('s')

            #Gestion de Y
            elif syllabes[0][-1] == 'Y':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Z
            elif syllabes[0][-1] == 'Z':
                #Assimilation à la consonne suivante
                changements.append('')

        return changements
