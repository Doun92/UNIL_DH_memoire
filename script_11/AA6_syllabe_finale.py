"""
auteur : Daniel Escoval
license : license UNIL
"""
import re

# from main import keys

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
'toutes_les_voyelles' : ["A", "Á", "E", "Ẹ", "Ę", "I", "Í", "Ī", "O", "Ǫ", "Ọ", "U", "Ú"],

'voyelles_toniques' : ["Ẹ", "Ę", "Á", "Ǫ", "Ọ", "Ú", 'Í'],

'voyelles_atones' : ["A", "E", "U", "I", "O"],

'voyelles_atones_sans_A' : ["E", "U", "I", "O"],

'consonnes_et_semi_consonnes' : ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],

'consonantisme_explosif_complexe_2_lettres' : [
'CB', 'DC', 'FB', 'GB', 'HB', 'LB', 'MB', 'NB', 'PB', 'RB', 'SB', 'TB', 'VB', 'WB', 'YB',
'BC', 'DC', 'FC', 'GC', 'HC', 'LC', 'MC', 'NC', 'PC', 'RC', 'SC', 'TC', 'VC', 'WC', 'YC',
'BD', 'CD', 'FD', 'GD', 'HD', 'LD', 'MD', 'ND', 'PD', 'RD', 'SD', 'TD', 'VD', 'WD', 'YD',
'BJ', 'CJ', 'DJ', 'FJ', 'GJ', 'HJ', 'LJ', 'MJ', 'NJ', 'PJ', 'RJ', 'SJ', 'TJ', 'VJ', 'WJ', 'YJ',
'BL', 'CL', 'DL', 'FL', 'GL', 'HL', 'LL', 'ML', 'NL', 'PL', 'RL', 'SL', 'TL', 'VL', 'WL', 'YL',
'BM', 'CM', 'DM', 'FM', 'GM', 'HM', 'LM', 'MM', 'NM', 'PM', 'RM', 'SM', 'TM', 'VM', 'WM', 'YM',
'BN', 'CN', 'DN', 'FN', 'GL', 'HL', 'LN', 'MN', 'NN', 'PN', 'RN', 'SN', 'TN', 'VN', 'WN', 'YN',
'BP', 'CP', 'DP', 'FP', 'GP', 'HP', 'LP', 'MP', 'NP', 'RP', 'SP', 'TP', 'VP', 'WP', 'YP',
'BR', 'CR', 'DR', 'FR', 'GR', 'HR', 'LR', 'MR', 'NR', 'PR', 'RR', 'SR', 'TR', 'VR', 'WR', 'YR',
'BS', 'CS', 'DS', 'FS', 'GS', 'HS', 'LS', 'MS', 'NS', 'PS', 'RS', 'SS', 'TS', 'VS', 'WS', 'YS',
'BT', 'CT', 'DT', 'FT', 'GT', 'HT', 'LT', 'MT', 'NT', 'PT', 'RT', 'ST', 'VT', 'WT', 'YT',
'BW', 'CW', 'DW', 'FW', 'GW', 'HW', 'LW', 'MW', 'NW', 'PW', 'QW', 'RW', 'SW', 'TW', 'VW', 'WW', 'YW',
'BY', 'CY', 'DY', 'FY', 'GY', 'HY', 'LY', 'MY', 'NY', 'PY', 'QY', 'RY', 'SY', 'TY', 'VY', 'WY', 'YY',
],

'consonantisme_explosif_complexe_3_lettres' : [
'SBR', 'SCR', 'SPR', 'STR',
],
}

class SyllabeFinale:

    def __init__(self):
        return

    def syllabe_finale(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #Consoantisme initial
        if syllabes[-1][0] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-1][0] == 'B':
                #Consonantisme complexe
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    #Cette séquence se maintient en milieu intervocalique
                    if syllabes[-1][1] == 'L':
                        changements.append('bl')
                    elif syllabes[-1][1] == 'R':
                        #En milieu intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('vr')
                        #En situation explosive
                        else:
                            changements.append('br')
                    elif syllabes[-1][1] == 'T':
                        changements.append('d')
                    elif syllabes[-1][1] == 'Y':
                        #En milieu intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #En milieu palatal
                            if syllabes[-2][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ǫ', 'Ọ'] and syllabes[-1][2] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                                #Position finale
                                if syllabes[-1][2] in ['I', 'O', 'E']:
                                    if syllabes[-1][2] == 'O' and syllabes[-1][2] == syllabes[-1][-1]:
                                        changements.append('')
                                    else:
                                        changements.append('v')
                                elif syllabes[-1][2] == 'U':
                                    if syllabes[-2][-1] in ['Á']:
                                        changements.append('v')
                                    else:
                                        changements.append('g')
                                else:
                                    changements.append('g')
                            #En milieu palatal, mais avec une graphie différente
                            elif syllabes[-2][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í' 'O', 'Ǫ', 'Ọ'] and syllabes[-1][2] in ['Ǫ']:
                                changements.append('j')
                            #En milieu vélaire
                            elif syllabes[-2][-1] in ['Ọ', 'Ú'] and syllabes[-1][2] in ['A', 'E', 'U']:
                                changements.append('')
                        #En milieu explosif
                        else:
                            changements.append('g')
                    elif syllabes[-1][1] == 'W':
                        #En milieu intervocalique
                        #Amuïssement, non sans avoir provoqué un arrondissement de la voyelle tonique qui suit ou qui précède
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-2][-1] in ['A', 'Á', 'Ẹ', 'Ę', 'Í' 'O', 'Ǫ', 'Ọ'] and syllabes[-1][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                            #Cas particulier
                            if syllabes[-2][-1] == syllabes[0][-1] and syllabes[-2][-1] == 'A' and syllabes[-1][1] == 'Ú':
                                changements.append('')
                            elif syllabes[-1][1] in ['E', 'I', 'U', 'O']:
                                changements.append('f')
                            else:
                                changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-2][-1] in ['E', 'Ọ', 'Ú'] and syllabes[-1][1] in ['A', 'E', 'U']:
                            changements.append('')
                    #En milieu explosif
                    else:
                        if syllabes[-1][1] in ['O', 'I', 'U', 'E']:
                            changements.append('p')
                        else:
                            changements.append(syllabes[-1][0])

            #Gestion de C
            elif syllabes[-1][0] == 'C':
                #Consonantisme complexe
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    if syllabes[-1][1] == 'N':
                        changements.append('sn')
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-1][1] == 'L':
                        #En milieu intervocalique
                        #Les palatales combinées avec un L aboutissent en un L mouill
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-2][-1] in ['Á', 'I', 'Ẹ']:
                                if syllabes[-1][2] == syllabes[-1][-1] == 'U':
                                    changements.append('cl')
                                else:
                                    changements.append('l')
                            elif syllabes[-2][-1] == 'Í':
                                changements.append('l')
                            elif syllabes[-2][-1] == 'E' and syllabes[-1][2] == 'U':
                                changements.append('gl')
                            else:
                                changements.append('il')
                        else:
                            #Après S la séquence CL se simplifie en [l]
                            if syllabes[-2][-1] == 'S':
                                changements.append('l')
                            else:
                                changements.append('cl')
                    elif syllabes[-1][1] == 'P':
                        if syllabes[-2][-1] == 'S':
                            changements.append('qu')
                        else:
                            changements.append('c')
                    elif syllabes[-1][1] == 'R':
                        #En milieu intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-2][-1] in ['I', 'Í', 'Ẹ', 'E', 'Ǫ']:
                                changements.append('r')
                            elif syllabes[-2][-1] == 'Á':
                                if syllabes[-1][2] == 'O':
                                    changements.append('gr')
                                elif syllabes[-1][2] == 'A':
                                    changements.append('cr')
                                else:
                                    changements.append('ir')
                            else:
                                changements.append('ir')
                        else:
                            if syllabes[-2][-1] in ['N', 'R', 'S']:
                                changements.append('tr')
                            else:
                                changements.append('cr')
                    elif syllabes[-1][1] == 'T':
                        if syllabes[-1][2] == 'S':
                            changements.append('')
                        elif syllabes[-1][2] in ['U', 'E', 'I', 'O'] and len(syllabes[-1]) > 3 and syllabes[-1][3] == 'S':
                            changements.append('')
                        else:
                            changements.append('t')
                    elif syllabes[-1][1] == 'Y':
                        if syllabes[-1][2] in ['O', 'U']:
                            if syllabes[-2][-1] in ['Á', 'Ẹ']:
                                if len(syllabes[-1]) > 3 and syllabes[-1][3] == 'S':
                                    changements.append('')
                                else:
                                    changements.append('z')
                            else:
                                changements.append('g')
                        else:
                            changements.append('c')
                    elif syllabes[-1][1] == 'W':
                        #En milieu intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            if syllabes[-1][2] == 'A':
                                changements.append('qu')
                            else:
                                changements.append('c')
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-1][1] in ['I', 'Í', 'E', 'Ẹ', 'Ę']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-2][-1] in ['I', 'Í', 'Ẹ']:
                                changements.append('s')
                            elif syllabes[-1][1] == syllabes[-1][-1] in ['I', 'E']:
                                changements.append('z')
                            elif syllabes[-1][2] == 'S':
                                changements.append('i')
                            else:
                                changements.append('is')
                        elif syllabes[-2][-1] in ['A', 'Á', 'I', 'Í', 'E', 'Ẹ', 'Ę'] and syllabes[-1][1] in ['A', 'Á']:
                            if syllabes[-2][-1] in ['I', 'Í', 'Ẹ', 'E']:
                                changements.append('')
                            else:
                                changements.append('i')
                        elif syllabes[-2][-1] in ["O", "Ǫ", "Ọ", "Ú", 'U'] and syllabes[-1][1] in ['A', 'Á']:
                            changements.append('')
                        elif syllabes[-1][1] in ["O", "Ǫ", "Ọ", "Ú", 'U']:
                            if syllabes[-2][-1] in ['Á']:
                                changements.append('i')
                            else:
                                changements.append('')
                    #En position explosive
                    #Palatalisation de C devant A
                    elif syllabes[-1][1] in ['A', 'Á']:
                        if syllabes[-2][-1] in ['R']:
                            if syllabes[-2][-2] in ['A', 'E']:
                                changements.append('ch')
                            elif syllabes[-2][-2] == 'B':
                                changements.append('g')
                            else:
                                changements.append('c')
                        elif syllabes[-2][-1] == 'L' and syllabes[-1][1] == 'A':
                            changements.append('c')
                        else:
                            changements.append('ch')
                    elif syllabes[-2][-1] in ['D', 'N']:
                        if syllabes[-2][-2] == 'Ẹ':
                            if syllabes[-1][1] == syllabes[-1][-1] == 'U':
                                changements.append('ch')
                            else:
                                changements.append('')
                        elif syllabes[-2][-2] == 'E':
                            changements.append('c')
                        else:
                            changements.append('z')
                    elif syllabes[-1][1] in ['I', 'O', 'U', 'E']:
                        if syllabes[-2][-1] == 'Y':
                            changements.append('s')
                        elif syllabes[-2][-1] == 'L':
                            changements.append('ts')
                        elif syllabes[-2][-1] in ['M', 'R']:
                            changements.append('c')
                        else:
                            changements.append('')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de D
            elif syllabes[-1][0] == 'D':
                #Consonantisme complexe
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    if syllabes[-1][1] == 'B':
                        changements.append('b')
                    elif syllabes[-1][1] == 'C':
                        changements.append('z')
                    elif syllabes[-1][1] == 'L':
                        changements.append('l')
                    elif syllabes[-1][1] == 'N':
                        if syllabes[-1] == 'DN':
                            changements.append('')
                        else:
                            changements.append('dn')
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-1][1] == 'R':
                        #En situation intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('r')
                        else:
                            changements.append('dr')
                    elif syllabes[-1][1] == 'T':
                        changements.append('t')
                    elif syllabes[-1][1] == 'Y':
                        #En situation intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        elif syllabes[-2][-1] == 'N':
                            changements.append('')
                        else:
                            changements.append('g')
                    elif syllabes[-1][1] == 'W':
                        #En situation intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append('d')
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][-1] == 'Í' and syllabes[-1][1] == 'Ę':
                            changements.append('d')
                        else:
                            changements.append('')
                    elif syllabes[-2][-1] == 'Y' and syllabes[-1][1] == syllabes[-1][-1] == 'E':
                        changements.append('')
                    elif syllabes[-2][-1] in ['G', 'P']:
                        changements.append('d')
                    elif syllabes[-1][1] in ['E', 'I', 'O', 'U'] and syllabes[-1][1] == syllabes[-1][-1]:
                        if len(syllabes[-1]) > 2 and syllabes[-1][-1] == 'S':
                            changements.append('t')
                        elif syllabes[-1][1] == syllabes[-1][-1]:
                            changements.append('t')
                        elif len(syllabes[-1]) > 2 and syllabes[-1][2] == 'T':
                            changements.append('')
                        else:
                            changements.append('d')
                    elif syllabes[-1][1] == 'A' and syllabes[-2][-1] == 'T':
                        changements.append('t')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de F
            elif syllabes[-1][0] == 'F':
                #Consonantisme complexe
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-1][1] == 'L':
                        #Position intervocalique
                        if syllabes[-2][-1] == 'Ǫ' and syllabes[-1][2] == 'A':
                            changements.append('l')
                        else:
                            changements.append('fl')
                    elif syllabes[-1][1] == 'R':
                        changements.append('fr')
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-2][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í' 'O', 'Ǫ', 'Ọ'] and syllabes[-1][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                            changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-2][-1] in ['Ọ', 'Ú'] and syllabes[-1][1] in ['A', 'E', 'U']:
                            changements.append('')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de G
            elif syllabes[-1][0] == 'G':
                #Consonantisme complexe
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-1][1] == 'L':
                        #Position intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-2][-1] in ['I', 'Í', 'Ẹ']:
                                if syllabes[-1][2] in ['A', 'Á', 'Ę']:
                                    changements.append('ll')
                                else:
                                    changements.append('l')
                            else:
                                if syllabes[-2][-1] in ['A'] and syllabes[-1][2] in ['Á', 'A', 'Ę']:
                                    changements.append('ill')
                                else:
                                    changements.append('il')
                        else:
                            changements.append('gl')
                    elif syllabes[-1][1] == 'N':
                        if syllabes[-1][2] in ['E', 'U', 'I', 'O']:
                            changements.append('ng')
                        else:
                            changements.append('gn')
                    elif syllabes[-1][1] == 'R':
                        #En milieu intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-2][-1] in ['I', 'Í', 'Ẹ']:
                                changements.append('r')
                            elif syllabes[-2][-1] == 'E' and syllabes[-1][2] == 'Ọ':
                                changements.append('gr')
                            else:
                                changements.append('ir')
                        else:
                            if syllabes[-2][-1] in ['L', 'R']:
                                if syllabes[-2][-2] == 'Ọ':
                                    changements.append('gr')
                                else:
                                    changements.append('dr')
                            elif syllabes[-2][-1] == 'N':
                                if syllabes[-2][-2] == 'O':
                                    changements.append('gr')
                                else:
                                    changements.append('dr')
                            else:
                                changements.append('gr')
                    elif syllabes[-1][1] == 'T':
                        changements.append('t')
                    elif syllabes[-1][1] == 'Y':
                        #En milieu intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] == 'A':
                                changements.append('')
                            else:
                                changements.append('i')
                        else:
                            changements.append('g')
                    elif syllabes[-1][1] == 'W':
                        #En milieu intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            if syllabes[-1][2] == 'A':
                                changements.append('gu')
                            else:
                                changements.append('g')
                else:
                    #En milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-1][1] in ['I', 'Í', 'E', 'Ẹ', 'Ę']:
                            changements.append('')
                        elif syllabes[-2][-1] in ['A', 'Á', 'I', 'Í', 'E', 'Ẹ', 'Ę'] and syllabes[-1][1] in ['A', 'Á']:
                            changements.append('i')
                        elif syllabes[-2][1] in ["O", "Ǫ", "Ọ",] and syllabes[-1][1] in ['A', 'Á']:
                            changements.append('v')
                        elif syllabes[-2][1] in ["Ú", 'U'] and syllabes[-1][1] in ['A', 'Á']:
                            changements.append('')
                        elif syllabes[-1][1] in ["O", "Ǫ", "Ọ", "Ú", 'U']:
                            if syllabes[-2][-1] in ['I', 'Í']:
                                changements.append('')
                            else:
                                changements.append('')
                    #En position explosive
                    #Palatalisation de G devant A (graphie en j)
                    elif syllabes[-1][1] in ['A', 'Á']:
                        if syllabes[-2][-1] == 'G':
                            changements.append('i')
                        else:
                            changements.append('g')
                    elif syllabes[-1][1] in ['I', 'O', 'U', 'E']:
                        changements.append('c')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de H (surtout utile pour les mots provenant du germain)
            elif syllabes[-1][0] == 'H':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-1][1])
                else:
                    changements.append('')

            #Gestion de J (Surtout utile pour les mots provenant du germain)
            elif syllabes[-1][0] == 'J':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-1][0])
                else:
                    changements.append(syllabes[-1][0])

            #Gestion de K (Surtout utile pour les mots provenant du germain)
            elif syllabes[-1][0] == 'K':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'W':
                        changements.append('qu')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    changements.append(syllabes[-1][0])

            #Gestion de L
            elif syllabes[-1][0] == 'L':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #L mouillé
                    if syllabes[-1][1] == 'Y':
                        #Voyelles dans lesquelles le i est déjà présent
                        if syllabes[-2][-1] in ['I', 'Í', 'Ẹ']:
                            if syllabes[-1][2] == 'A':
                                changements.append('ll')
                            elif syllabes[-2][-1] == 'L':
                                changements.append('ll')
                            else:
                                changements.append('l')
                        else:
                            if syllabes[-1][2] == 'A':
                                changements.append('ill')
                            elif syllabes[-1][2] == 'O':
                                changements.append('l')
                            else:
                                changements.append('il')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #Épenthèse d'un B après M
                    if syllabes[-2][-1] == 'M':
                        changements.append('bl')
                    #Dénasalisation du N
                    elif syllabes[-2][-1] == 'N':
                        changements.append('gl')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de M
            elif syllabes[-1][0] == 'M':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'R':
                        if syllabes[-1][1] == syllabes[-1][-1]:
                            changements.append('bre')
                        else:
                            changements.append('r')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #Position finale
                    if syllabes[-1][1] in ['I', 'U', 'E']:
                        if syllabes[-2][-1] in ['D', 'M', 'X']:
                            changements.append('m')
                        elif len(syllabes[-2]) > 1 and syllabes[-2][-2] + syllabes[-2][-1] == 'GY':
                            changements.append('m')
                        else:
                            changements.append('n')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de N
            elif syllabes[-1][0] == 'N':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'T':
                        if syllabes[-1] == 'NT':
                            changements.append('')
                        else:
                            changements.append('nt')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #Assimilation à la nasale précédente
                    if syllabes[-2][-1] in ['M']:
                        changements.append('')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de P
            elif syllabes[-1][0] == 'P':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-1][1] == 'C':
                        changements.append('c')
                    elif syllabes[-1][1] == 'L':
                        #En milieu intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('bl')
                        #En situation explosive
                        else:
                            changements.append('pl')
                    elif syllabes[-1][1] == 'R':
                        #En position intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('vr')
                        else:
                            changements.append('pr')
                    elif syllabes[-1][1] == 'T':
                        changements.append('t')
                    #L'occlusive sourde labiale se singularise
                    elif syllabes[-1][1] == 'Y':
                        changements.append('ch')
                    elif syllabes[-1][1] == 'W':
                        changements.append('')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #En milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-2][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'Ǫ', 'Ú', 'U'] and syllabes[-1][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'Ọ', 'U', 'Ú']:
                            #En position de finale absolue
                            if syllabes[-1][1] in ['E', 'O', 'U','I']:
                                # if syllabes[-1][-1] == 'T' or syllabes[-2][-1] == 'Ǫ':
                                if syllabes[-1][-1] == 'T':
                                    changements.append('')
                                else:
                                    changements.append('f')
                            #Cas particulier
                            elif syllabes[-2][-1] == syllabes[0][-1] and syllabes[-2][-1] == 'A' and syllabes[-1][1] == 'Ú':
                                changements.append('')
                            else:
                                changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-2][-1] in ['O', 'Ọ'] and syllabes[-1][1] in ['A', 'Á', 'E', 'U', 'Ú']:
                            if syllabes[-1][1] in ['A', 'Á']:
                                changements.append('v')
                            else:
                                changements.append('')
                    #En milieu explosif
                    else:
                        if syllabes[-2][-1] == 'N' and syllabes[-1][1] == 'I':
                            changements.append('v')
                        else:
                            changements.append(syllabes[-1][0])

            #Gestion de Q
            elif syllabes[-1][0] == 'Q':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    if syllabes[-1][1] == 'W':
                        if syllabes[-1][2] in ['Ọ']:
                            changements.append('c')
                        elif syllabes[-1][2] == 'Ǫ':
                            changements.append('z')
                        else:
                            changements.append('qu')
                    else:
                        changements.append('c')
                else:
                    changements.append(syllabes[-1][0])

            #Gestion de R
            elif syllabes[-1][0] == 'R':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'D':
                        changements.append('rt')
                    elif syllabes[-1][1] == 'Y':
                        if syllabes[-2][-1] in ['A', 'Á', 'Ę', 'Ọ']:
                            changements.append('r')
                        else:
                            changements.append('rg')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #Épenthèse d'un D après N
                    if syllabes[-2][-1] == 'N':
                        changements.append('dr')
                    #Épenthèse de B après M
                    elif syllabes[-2][-1] == 'M':
                        changements.append('br')
                    #Épenthèse d'un D après L ou d'une sifflante sonore
                    elif syllabes[-2][-1] in ['L', 'S']:
                        changements.append('dr')
                    elif syllabes[-2] == 'LW':
                        changements.append('dr')
                    #Épenthèse d'un T après X
                    elif syllabes[-2][-1] == 'X':
                        changements.append('tr')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de S
            elif syllabes[-1][0] == 'S':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'R':
                        if syllabes[-1][1] == syllabes[-1][-1]:
                            changements.append('stre')
                        elif syllabes[-1][2] in ['E', 'U', 'I', 'O']:
                            changements.append('str')
                        else:
                            changements.append('sdr')
                    elif syllabes[-1][1] == 'T':
                        if len(syllabes[-1]) > 2 and syllabes[-1][2] == 'R':
                            changements.append('str')
                        elif syllabes[-1][-1] == 'Ī':
                            changements.append('s')
                        else:
                            changements.append('st')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-1][1] == 'W':
                        changements.append(syllabes[-1][0])
                    #La sifflante sourde se palatalise au contact du yod
                    elif syllabes[-1][1] == 'Y':
                        changements.append('s')
                    else:
                        changements.append(syllabes[-1][0] + syllabes[-1][1])
                else:
                    changements.append(syllabes[-1][0])

            #Gestion de T
            elif syllabes[-1][0] == 'T':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'C':
                        changements.append('ch')
                    elif syllabes[-1][1] == 'L':
                        #Voyelles dans lesquelles le i est déjà présent
                        if syllabes[-2][-1] in ['I', 'Í', 'Ẹ']:
                            changements.append('l')
                        elif syllabes[-2][-1] in ['B', 'T']:
                            changements.append('l')
                        else:
                            changements.append('il')
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-1][1] == 'M':
                        changements.append('m')
                    elif syllabes[-1][1] == 'N':
                        changements.append('gn')
                    elif syllabes[-1][1] == 'R':
                        #En situation intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] == 'Í':
                                changements.append('tr')
                            else:
                                if syllabes[-2][-1] == 'O' and syllabes[-1][2] == 'Ę':
                                    changements.append('rr')
                                else:
                                    changements.append('r')
                        else:
                            changements.append('tr')
                    elif syllabes[-1][1] == 'S':
                        if syllabes[-1] == 'TS':
                            changements.append('')
                        else:
                            changements.append('t')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-1][1] == 'W':
                        #Position intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-1][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[-1][1] == 'Y':
                        #En situation intervocalique
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-1][2] == 'S':
                                changements.append('')
                            elif syllabes[-2][-1] == 'Ǫ' and syllabes[-1][2] == 'A':
                                changements.append('d')
                            else:
                                changements.append('s')
                        elif syllabes[-2][-1] == 'S':
                            changements.append('')
                        elif syllabes[-2][-1] == 'C':
                            changements.append('st')
                        else:
                            if syllabes[-1][2] in ['O', 'Ọ', 'Ǫ', 'U', 'Ú']:
                                changements.append('ç')
                            else:
                                changements.append('c')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #En situation intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][-1] == 'Í' and syllabes[-1][1] == 'A':
                            changements.append('t')
                        else:
                            changements.append('')
                    elif len(syllabes[-1]) > 2 and syllabes[-1][1] in ['U'] and syllabes[-1][2] == 'S':
                        changements.append('')
                    elif syllabes[-2][-1] == 'G':
                        changements.append('')
                    elif syllabes[-2][-1] == 'S' and syllabes[-1][1] == 'Ī':
                        changements.append('')
                    elif syllabes[-2][-1] == 'B':
                        if syllabes[-1][1] == syllabes[-1][-1] == 'U':
                            changements.append('t')
                        else:
                            changements.append('d')
                    elif syllabes[-2][-1] == 'C' and syllabes[-1][1] == 'A':
                        if syllabes[-2][-2] == 'Ǫ':
                            changements.append('d')
                        else:
                            changements.append('t')
                    else:
                        changements.append(syllabes[-1][0])

            #Gestion de V (wau ancien)
            elif syllabes[-1][0] == 'V':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'R':
                        if syllabes[-2][-1] == 'L':
                            changements.append('dr')
                        else:
                            changements.append('vr')
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    elif syllabes[-1][1] == 'Y':
                        changements.append('j')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #En milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-2][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ǫ', 'Ọ'] and syllabes[-1][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                            #En position finale
                            if syllabes[-1][1] in ['I', 'O', 'E', 'U']:
                                if syllabes[-1][1] == syllabes[-1][-1] or len(syllabes[-1]) > 2 and syllabes[-1][2] == 'S' == syllabes[-1][-1]:
                                    changements.append('f')
                                else:
                                    changements.append('v')
                            else:
                                changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-2][-1] in ['Ọ', 'Ú'] and syllabes[-1][1] in ['A', 'E', 'U']:
                            changements.append('')
                    else:
                        if syllabes[-1][1] == 'A':
                            if len(syllabes[-1]) > 2 and syllabes[-1][1] in ['D', 'L', 'S']:
                                changements.append('v')
                            else:
                                changements.append('g')
                        elif syllabes[-1][1] in ['I', 'O', 'U', 'E']:
                            if syllabes[-2][-1] == 'R':
                                changements.append('')
                            else:
                                changements.append('f')
                        else:
                            changements.append(syllabes[-1][0])

            #Gestion de W (wau récent) (Probablement inexistant en cette position)
            elif syllabes[-1][0] == 'W':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'R':
                        if syllabes[-2][-1] == 'N':
                            changements.append('dr')
                        else:
                            changements.append('r')
                    elif syllabes[-1][1] == 'Y':
                        changements.append('j')
                    elif syllabes[-1][1] == 'T':
                        if len(syllabes[-1]) == 2:
                            changements.append('')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    #En milieu intervocalique
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-2][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í' 'O', 'Ǫ', 'Ọ'] and syllabes[-1][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                            #En position de finale absolue
                            if syllabes[-1][1] in ['E', 'I', 'O', 'U']:
                                changements.append('f')
                            else:
                                changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-2][-1] in ['Ọ', 'Ú'] and syllabes[-1][1] in ['A', 'E', 'U']:
                            changements.append('')
                    else:
                        if syllabes[-2][-1] in ['N', 'Q', 'V']:
                            changements.append('')
                        elif syllabes[-2][-1] == 'W':
                            changements.append('v')
                        elif syllabes[-1][1] in ['Á', 'E', 'Ẹ', 'Ę', 'I', 'Í']:
                            changements.append('gu')
                        else:
                            changements.append('g')

            #Gestion de X (Probablement inexistant en cette position)
            elif syllabes[-1][0] == 'X':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1][1] == 'Y':
                        changements.append('s')
                    else:
                        changements.append(syllabes[-1][0])
                else:
                    if syllabes[-2][-1] in ['Ǫ'] and syllabes[-1][1] == 'A':
                        changements.append('ss')
                    elif syllabes[-2][-1] in ['Ę'] and syllabes[-1][1] == 'I':
                        changements.append('s')
                    elif syllabes[-2][-1] == 'A' and syllabes[-1][1] == 'Ī':
                        changements.append('x')
                    else:
                        changements.append('s')

            #Gestion de Y
            elif syllabes[-1][0] == 'Y':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-1] == 'YT':
                        changements.append('')
                    elif syllabes[-1][1] == 'C':
                        changements.append('')
                    else:
                        changements.append(syllabes[-1][1])
                else:
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        changements.append('i')
                    elif syllabes[-2][-1] in ['N', 'S', 'Y']:
                        # if syllabes[-2][-2] == 'Á' and syllabes[-1][1] == 'A':
                        #     changements.append('i')
                        # else:
                            changements.append('')
                    #Positin finale
                    elif syllabes[-1] in ['YO']:
                        changements.append('e')
                    elif syllabes[-1] == 'YA':
                        changements.append('')
                    elif syllabes[-1] == 'YU':
                        if syllabes[-2][-1] == 'Q':
                            changements.append('z')
                        else:
                            changements.append('')
                    elif syllabes[-2][-1] in ['R', 'V']:
                        changements.append('g')
                    else:
                        changements.append('j')

            #Gestion de Z (Probablement inexistant en cette position)
            elif syllabes[-1][0] == 'Z':
                if syllabes[-1][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-1][0])
                else:
                    changements.append(syllabes[-1][0])

        #Vocalisme atone
        #A
        if 'A' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('e')
            #Si A se trouve en position ouvert
            elif syllabes[-1][-1] == 'A':
                changements.append('e')
            #Si A se trouve en position pénultième
            elif syllabes[-1][-2] == 'A':
                changements.append('e')
            #Si se trouve en position antépénultième
            elif syllabes[-1][-3] == 'A':
                changements.append('e')
            #Tous les autres cas de figure
            else:
                changements.append('e')

        #E
        elif 'E' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('')
            #Si E se trouve en position ouvert
            elif syllabes[-1][-1] == 'E':
                #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                if len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                    if syllabes[-1][0] + syllabes[-1][1] in ['DR', 'PT']:
                        if syllabes[-2][-1] == 'N':
                            changements.append('e')
                        else:
                            changements.append('')
                    else:
                        changements.append('e')
                elif syllabes[-2][-1] + syllabes[-1][0] in ['DM', 'DC', 'MC', 'MT', 'MN', 'NR', 'LR', 'SR', 'VN', 'VR', 'YN', 'ST']:
                    changements.append('e')
                else:
                    changements.append('')
            #Si E se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'E':
                #E d'appui au pluriel
                if syllabes[-1][-1] == 'S':
                    #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                    if len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                        changements.append('e')
                    else:
                        changements.append('')
                else:
                    changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-1][-3] == 'E':
                changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #I
        elif 'I' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('')
            #Si I se trouve en position ouvert
            elif syllabes[-1][-1] == 'I':
                #E d'appui
                if syllabes[-2][-1] + syllabes[-1][0] in ['NP', 'QW']:
                    changements.append('e')
                else:
                    changements.append('')
            #Si I se trouve en position pénultième
            elif syllabes[-1][-2] == 'I':
                if syllabes[-1][-3] == 'T' and syllabes[-1][-1] == 'S':
                    changements.append('e')
                else:
                    changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-1][-3] == 'I':
                changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #O
        elif 'O' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                if syllabes[-2][-1] == 'Í':
                    changements.append('on')
                else:
                    changements.append('')
            #Si O se trouve en position ouvert
            elif syllabes[-1][-1] == 'O':
                #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                if len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                    if syllabes[-1][0] + syllabes[-1][1] in ['GY', 'CY', 'RY']:
                        changements.append('')
                    else:
                        changements.append('e')
                #E d'appui pour d'autres séquences
                elif syllabes[-2][-1] == 'S' and syllabes[-1][0] == 'L':
                    changements.append('e')
                else:
                    changements.append('')
            #Si O se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'O':
                #E d'appui au pluriel
                if syllabes[-1][-1] == 'S':
                    #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                    if len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                        if syllabes[-1][0] + syllabes[-1][1] in ['CT', 'CY']:
                            changements.append('')
                        else:
                            changements.append('e')
                    else:
                        changements.append('')
                else:
                    changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-1][-3] == 'O':
                if syllabes[-1][-2] == 'N':
                    changements.append('o')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #U
        elif 'U' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('e')
            #Si U se trouve en position ouvert
            elif syllabes[-1][-1] == 'U':
                #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                if len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                    if syllabes[-1][0] + syllabes[-1][1] in ['CT', 'DY', 'GY',  'LY', 'TY', 'TL', 'RD']:
                        changements.append('')
                    elif syllabes[-1][0] + syllabes[-1][1] in ['CY', 'RY']:
                        if syllabes[-2][-1] in ['B', 'R', 'T']:
                            changements.append('e')
                        else:
                            changements.append('')
                    elif syllabes[-2][-1] + syllabes[-1][0] + syllabes[-1][1] == 'ÁLY':
                        changements.append('')
                    elif syllabes[-2][-1] in listes_lettres['toutes_les_voyelles'] and syllabes[-1][0] + syllabes[-1][1] == 'CL':
                        if syllabes[-2][-1] == syllabes[0][-1] == 'E' and syllabes[-1][2] == 'U':
                            changements.append('e')
                        elif syllabes[-2][-1] == 'Á' and syllabes[-1][2] == 'U':
                            changements.append('e')
                        else:
                            changements.append('')
                    else:
                        changements.append('e')
                elif syllabes[-2][-1] + syllabes[-1][0] in ['XN', 'XM', 'BT', 'PT', 'GD', 'SN', 'PD', 'NC', 'WW', 'RY', 'VY', 'ST']:
                    if syllabes[-2][-2] == 'Í':
                        changements.append('')
                    else:
                        changements.append('e')
                elif syllabes[-2][-1] + syllabes[-1][0] in ['MY', 'NY']:
                    if syllabes[-2][-2] == 'Í':
                        changements.append('e')
                    else:
                        changements.append('')
                else:
                    changements.append('')
            #Si U se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'U':
                #E d'appui au pluriel
                if syllabes[-1][-1] == 'S':
                    #La plupart des groupes consonantiques ont besoin d'un e d'appui à la fin
                    if len(syllabes[-1]) > 2 and syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe_2_lettres']:
                        if syllabes[-1][0] + syllabes[-1][1] in ['CT', 'DY', 'GY',  'LY', 'TY', 'TL', 'RD', 'RY']:
                            changements.append('')
                        else:
                            changements.append('e')
                    else:
                        changements.append('')
                else:
                    changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-1][-3] == 'U':
                if syllabes[-1][-2] + syllabes[-1][-1] == 'NT':
                    changements.append('e')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #Vocalisme
        #Á tonique
        if 'Á' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('e')
            #Si A tonique se trouve en position ouverte
            elif syllabes[-1][-1] == 'Á':
                #Loi de Bartsh
                if syllabes[-1][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[-1]) > 2 and syllabes[-1][-3] + syllabes[-1][-2] in ['CT', 'TY']:
                    changements.append('ie')
                else:
                    changements.append('ai')
            #Si A tonique se trouve au milieu de la syllabe
            elif syllabes[-1][-2] == 'Á':
                #Loi de Bartsh
                if syllabes[-1][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[-1]) > 2 and len(syllabes[-1]) > 2 and syllabes[-1][-3] + syllabes[-1][-2] in ['CT']:
                    changements.append('ie')
                else:
                    changements.append('e')
            #Si se trouve en position antépénultième
            elif syllabes[-1][-3] == 'Á':
                if syllabes[-2][-1] == 'I' and syllabes[-1][-2] + syllabes[-1][-1] == 'CS':
                    changements.append('a')
                #Loi de Bartsh
                elif syllabes[-1][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[-1]) > 2 and syllabes[-1][-3] + syllabes[-1][-2] in ['CT']:
                    changements.append('ie')
                elif len(syllabes[-1]) > 4 and syllabes[-1][-5] + syllabes[-1][-4] == 'PY':
                    changements.append('ie')
                elif syllabes[-1][-2] + syllabes[-1][-1] == 'NS':
                    changements.append('a')
                else:
                    changements.append('e')
            #Autres cas de figure, plus rare ou A tonique ne se trouve dans aucune de ces positions
            else:
                changements.append('e')

        #Ẹ fermé
        elif 'Ẹ' in syllabes[-1]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('ei')
            #Si E fermé se trouve en position ouverte
            elif syllabes[-1][-1] == 'Ẹ':
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                if syllabes[-1][-2] == 'C':
                    changements.append('i')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position fermée
            elif syllabes[-1][-2] == 'Ẹ':
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                if syllabes[-1][-3] == 'C':
                    changements.append('i')
                else:
                    changements.append('e')
            #Si se trouve en position antépénultième
            elif syllabes[-1][-3] == 'Ẹ':
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                if syllabes[-1][-4] == 'C':
                    changements.append('i')
                else:
                    changements.append('e')
            #Si E fermé se trouve en position fermée
            else:
                changements.append('e')

        #Ę ouvert
        elif 'Ę' in syllabes[-1]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('ie')
            #Si E ouvert se trouve en position finale
            elif syllabes[-1][-1] == 'Ę':
                changements.append('ie')
            #Si E ouvert se trouve en position pénultième
            elif syllabes[-1][-2] == 'Ę':
                if syllabes[-1][-1] == 'T':
                    changements.append('oi')
                else:
                    changements.append('e')
            #Si E ouvert se trouve en position antépénultième
            elif syllabes[-1][-3] == 'Ę':
                changements.append('e')
            #Si E ouvert se trouve en position fermée
            else:
                changements.append('e')

        #Í tonique
        elif 'Í' in syllabes[-1]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-1]) == 1:
                changements.append('i')
            #Si I tonique se trouve en position finale
            elif syllabes[-1][-1] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position pénultième
            elif syllabes[-1][-2] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position antépénultième
            elif syllabes[-1][-3] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position fermée
            else:
                changements.append('i')

        elif 'Ī' in syllabes[-1]:
            if syllabes[-1] == 'Ī':
                if syllabes[-2][-1] == 'Ọ':
                    changements.append('i')
                else:
                    changements.append('')
            elif syllabes[-1][-1] == 'Ī':
                if len(syllabes[-1]) > 1 and syllabes[-1][-2] == syllabes[-1][0] in ['L', 'M', 'N', 'T', 'X']:
                    if syllabes[-2][-1] == syllabes[-1][0]:
                        changements.append('')
                    else:
                        changements.append('i')
                else:
                    changements.append('')


        #Ọ fermé
        elif 'Ọ' in syllabes[-1]:
            if len(syllabes[-1]) == 1:
                changements.append('ou')
            #Si O fermé se trouve en position finale
            elif syllabes[-1][-1] == 'Ọ':
                changements.append('ou')
            #Si O fermé se trouve en position pénultième
            elif syllabes[-1][-2] == 'Ọ':
                changements.append('o')
            #Si O fermé se trouve en position antépénultième
            elif syllabes[-1][-3] == 'Ọ':
                changements.append('o')
            #Toutes les autres positions
            else:
                changements.append('o')

        #Ǫ ouvert
        elif 'Ǫ' in syllabes[-1]:
            if len(syllabes[-1]) == 1:
                changements.append('ue')
            #Si O ouvert se trouve en position finale
            elif syllabes[-1][-1] == 'Ǫ':
                changements.append('ue')
            #Si O ouvert se trouve en position pénultième
            elif syllabes[-1][-2] == 'Ǫ':
                if syllabes[-1][-3] == 'Y' and  syllabes[-1][-1] == 'R':
                    changements.append('ou')
                else:
                    changements.append('o')
            #Si O ouvert se trouve en position antépénultième
            elif syllabes[-1][-3] == 'Ǫ':
                changements.append('o')
            #Toutes les autres positions
            else:
                changements.append('o')

        #Ú tonique
        elif 'Ú' in syllabes[-1]:
            if len(syllabes[-1]) == 1:
                changements.append('u')
            #Si U tonique se trouve en position finale
            elif syllabes[-1][-1] == 'Ú':
                changements.append('u')
            #SiU tonique se trouve en position pénultième
            elif syllabes[-1][-2] == 'Ú':
                changements.append('u')
            #Si U tonique se trouve en position antépénultième
            elif syllabes[-1][-3] == 'Ú':
                changements.append('u')
            #Toutes les autres positions
            else:
                changements.append('u')

        #Consonantisme final
        if syllabes[-1][-1] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-1][-1] == 'B':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de C
            elif syllabes[-1][-1] == 'C':
                if syllabes[-1][-2] == 'Ę':
                    changements.append('c')
                elif syllabes[-1][-2] == 'N':
                    changements.append('nc')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de D
            elif syllabes[-1][-1] == 'D':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de F
            elif syllabes[-1][-1] == 'F':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de G
            elif syllabes[-1][-1] == 'G':
                #Assimilation au N suivant
                if syllabes[-1][0] == 'N':
                    if syllabes[-1] == syllabes[-1]:
                        changements.append('')
                    else:
                        changements.append('g')
                elif syllabes[-1][-2] == 'R':
                    changements.append('rc')
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de H (ne devrait pas exister ou cas très très rare)
            elif syllabes[-1][-1] == 'H':
                changements.append('')

            #Gestion de L
            elif syllabes[-1][-1] == 'L':
                if syllabes[-1][-2] == 'L':
                    changements.append('l')
                else:
                    #La liquide se vocalise en [w]
                    changements.append('u')

            #Gestion de M
            elif syllabes[-1][-1] == 'M':
                #Assimilation à la consonne suivante
                changements.append('n')

            #Gestion de N
            elif syllabes[-1][-1] == 'N':
                if syllabes[-1] == 'DN':
                    changements.append('ng')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('n')

            #Gestion de P
            elif syllabes[-1][-1] == 'P':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Q
            elif syllabes[-1][-1] == 'Q':
                changements.append('')

            #Gestion de R
            elif syllabes[-1][-1] == 'R':
                if syllabes[-1][-2] not in listes_lettres['toutes_les_voyelles']:
                    changements.append('')
                elif len(syllabes[-1]) > 2 and syllabes[-1][-3] + syllabes[-1][-2] == 'YO':
                    #Épenthèse d'un D après L
                    if len(syllabes[-1]) > 3 and syllabes[-1][-4] == 'L':
                        changements.append('dre')
                    else:
                        changements.append('re')
                else:
                    #La vibrante est très stable
                    changements.append(syllabes[-1][-1])


            #Gestion de S
            elif syllabes[-1][-1] == 'S':
                if syllabes[-1][-2] in ['E', 'U', 'O'] and len(syllabes[-1]) > 2 and syllabes[-1][-3] in ['C', 'D', 'T']:
                    changements.append('z')
                elif syllabes[-1][-2] == 'R':
                    changements.append('rs')
                elif syllabes[-1][-2] == 'N':
                    changements.append('ns')
                elif syllabes[-1][-2] in ['C', 'T']:
                    changements.append('z')
                else:
                    changements.append('s')

            #Gestion de T
            elif syllabes[-1][-1] == 'T':
                if syllabes[-1][-2] in  ['A', 'Á', 'D']:
                    changements.append('')
                else:
                    if syllabes[-1][-2] == 'N':
                        changements.append('nt')
                    else:
                        changements.append('t')

            #Gestion de V
            elif syllabes[-1][-1] == 'V':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de W
            elif syllabes[-1][-1] == 'W':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de X
            elif syllabes[-1][-1] == 'X':
                changements.append('s')

            #Gestion de Y
            elif syllabes[-1][-1] == 'Y':
                if syllabes[-1][-2] == 'N':
                    changements.append('ng')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de Z
            elif syllabes[-1][-1] == 'Z':
                #Assimilation à la consonne suivante
                changements.append('')

        return changements
