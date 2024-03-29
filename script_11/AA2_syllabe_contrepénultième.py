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
'toutes_les_voyelles' : ["A", "Á", "E", "Ẹ", "Ę", "I", "Í", "Ī", "O", "Ǫ", "Ọ", "U", "Ú"],

'voyelles_toniques' : ["Ẹ", "Ę", "Á", "Ǫ", "Ọ", "Ú", 'Í'],

'voyelles_atones' : ["A", "E", "U", "I", "O"],

'voyelles_atones_sans_A' : ["E", "U", "I", "O"],

'consonnes_et_semi_consonnes' : ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],

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
'SBR', 'SCR', 'SPR', 'STR',
],
}
class SyllabeContrepenultieme:

    def __init__(self):
        return

    def syllabe_contrepenultieme(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        if syllabes[-5][0] == ' ':
            changements.append(syllabes[-5][1])

        #Consoantisme initial
        if syllabes[-5][0] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-5][0] == 'B':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-5][1] == 'C':
                        changements.append('g')
                    #Cette séquence se maintient en milieu intervocalique
                    elif syllabes[-5][1] == 'L':
                        if syllabes[-6][-1] == 'M' and syllabes[-5][2] == 'Í':
                            changements.append('br')
                        else:
                            changements.append('bl')
                    elif syllabes[-5][1] == 'R':
                        #En cas de mauvaise découpe syllabique
                        if syllabes[-5] == 'BR':
                            changements.append('')
                        #En milieu intervocalique
                        elif syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('vr')
                        #En situation explosive
                        else:
                            changements.append('br')
                    elif syllabes[-5][1] == 'Y':
                        #En milieu intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            #En milieu palatal
                            if syllabes[-6][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ọ'] and syllabes[-5][2] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'I', 'O', 'Ǫ', 'U', 'Ú']:
                                #En milieu palatal, mais avec une graphie différente
                                if syllabes[-6][-1] in ['A'] and syllabes[-5][2] in ['Ǫ']:
                                    changements.append('j')
                                else:
                                    changements.append('g')
                            #En milieu vélaire
                            elif syllabes[-6][-1] in ['Ǫ', 'Ú'] and syllabes[-5][2] in ['A', 'Á', 'E', 'Ẹ', 'I', 'O', 'U']:
                                changements.append('')
                        #En position explosive
                        else:
                            changements.append('g')
                    elif syllabes[-5][1] == 'W':
                        #En milieu intervocalique
                        #Amuïssement, non sans avoir provoqué un arrondissement de la voyelle tonique qui suit ou qui précède
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                    else:
                        changements.append(syllabes[-6][1])
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-6][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ọ'] and syllabes[-5][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'I', 'O', 'Ǫ', 'U', 'Ú']:
                            #Cas particulier
                            if syllabes[-6][-1] == syllabes[-5][-1] and syllabes[-6][-1] == 'A' and syllabes[-5][1] == 'Ú':
                                changements.append('')
                            else:
                                changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-6][-1] in ['Ǫ', 'Ú'] and syllabes[-5][1] in ['A', 'Á', 'E', 'Ẹ', 'I', 'O', 'U']:
                            changements.append('')
                    #En milieu explosif
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de C
            elif syllabes[-5][0] == 'C':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-5][1] == 'L':
                        #En milieu intervocalique
                        #Les palatales combinées avec un L aboutissent en un L mouill
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-6][-1] in ['I', 'Í', 'Ẹ', 'E']:
                                changements.append('l')
                            else:
                                changements.append('il')
                        elif syllabes[-6][-2] + syllabes[-6][-1] == 'EC' and syllabes[-5][2] == 'Ę':
                            changements.append('gl')
                        #Après S la séquence CL se simplifie en [l]
                        elif syllabes[-6][-1] == 'S':
                            changements.append('l')
                        else:
                            changements.append('cl')
                    elif syllabes[-5][1] == 'R':
                        #En milieu intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-6][-1] in ['I', 'Í', 'Ẹ', 'E', 'Ǫ']:
                                changements.append('r')
                            else:
                                changements.append('ir')
                        elif syllabes[-6][-1] == 'N':
                            changements.append('tr')
                        else:
                            changements.append('cr')
                    elif syllabes[-5][1] == 'T':
                        changements.append('c')
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] == 'D':
                            changements.append('gi')
                        elif syllabes[-6][-1] == 'S':
                            changements.append('s')
                        else:
                            changements.append('c')
                    elif syllabes[-5][1] == 'W':
                        #En milieu intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append('c')
                    else:
                        changements.append(syllabes[-5][1])
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-5][1] in ['I', 'Í', 'E', 'Ẹ', 'Ę']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-6][-1] in ['I', 'Í', 'Ẹ', 'E']:
                                changements.append('s')
                            else:
                                changements.append('is')
                        elif syllabes[-6][-1] in ['A', 'Á', 'I', 'Í', 'E', 'Ẹ', 'Ę'] and syllabes[-5][1] in ['A', 'Á']:
                            if syllabes[-6][-1] in ['I', 'Í', 'Ẹ', 'E']:
                                changements.append('')
                            else:
                                changements.append('i')
                        elif syllabes[-6][1] in ["O", "Ǫ", "Ọ", "Ú", 'U'] and syllabes[-5][1] in ['A', 'Á']:
                            changements.append('')
                        elif syllabes[-5][1] in ["O", "Ǫ", "Ọ", "Ú", 'U']:
                            if syllabes[-6][1] in ['Á', 'Í']:
                                changements.append('i')
                            else:
                                changements.append('')
                    #En position explosive
                    #Palatalisation de C devant A
                    elif syllabes[-5][1] in ['A', 'Á']:
                        if syllabes[-6][-1] in ['D', 'M']:
                            changements.append('g')
                        else:
                            changements.append('ch')
                    elif syllabes[-6][-1] in ['C', 'L']:
                        changements.append('c')
                    elif syllabes[-5][1] == "Ọ":
                        #Présence d'un préfixe
                        if syllabes[-6][-1] == ' ':
                            changements.append('c')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de D
            elif syllabes[-5][0] == 'D':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    if syllabes[-5][1] == 'C':
                        changements.append('g')
                    elif syllabes[-5][1] == 'F':
                        changements.append('f')
                    elif syllabes[-5][1] == 'L':
                        changements.append('l')
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-5][1] == 'R':
                        #En situation intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('r')
                        else:
                            changements.append('dr')
                    elif syllabes[-5][1] == 'Y':
                        #En situation intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        elif syllabes[-6][-1] == 'D':
                            changements.append('j')
                        elif syllabes[-6][-1] == 'N':
                            changements.append('')
                        else:
                            changements.append('g')
                    elif syllabes[-5][1] == 'W':
                        #En situation intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append('d')
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        changements.append('')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de F
            elif syllabes[-5][0] == 'F':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    changements.append(syllabes[-5][0] + syllabes[-5][1])
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-6][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ọ'] and syllabes[-5][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'I', 'O', 'Ǫ', 'U', 'Ú']:
                            changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-6][-1] in ['Ǫ', 'Ú'] and syllabes[-5][1] in ['A', 'Á', 'E', 'Ẹ', 'I', 'O', 'U']:
                            changements.append('')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de G
            elif syllabes[-5][0] == 'G':
                #Consonantisme complexe
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-5][1] == 'L':
                        #Position intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-6][-1] in ['I', 'Í', 'Ẹ', 'E']:
                                if len(syllabes[-5]) > 2 and syllabes[-5][2] == 'Á':
                                    changements.append('ll')
                                else:
                                    changements.append('l')
                            else:
                                if syllabes[-6][-1] == 'A' and syllabes[-5][2] == 'Á':
                                    changements.append('ill')
                                else:
                                    changements.append('il')
                        else:
                            changements.append('gl')
                    elif syllabes[-5][1] == 'N':
                        changements.append('gn')
                    elif syllabes[-5][1] == 'R':
                        #En milieu intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-6][-1] in ['I', 'Í', 'Ẹ', 'E',]:
                                changements.append('r')
                            else:
                                changements.append('ir')
                        else:
                            changements.append('gr')
                    elif syllabes[-5][1] == 'Y':
                        #En milieu intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-6][-1] == 'Í':
                                changements.append('')
                            else:
                                changements.append('i')
                        else:
                            cchangements.append('g')
                    elif syllabes[-5][1] == 'W':
                        #En milieu intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[-5][1])
                else:
                    #En milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-5][1] in ['I', 'Í', 'E', 'Ẹ', 'Ę']:
                            changements.append('')
                        elif syllabes[-6][-1] in ['A', 'Á', 'I', 'Í', 'E', 'Ẹ', 'Ę'] and syllabes[-5][1] in ['A', 'Á']:
                            changements.append('i')
                        elif syllabes[-6][1] in ["O", "Ǫ", "Ọ",] and syllabes[-5][1] in ['A', 'Á']:
                            changements.append('v')
                        elif syllabes[-6][1] in ["Ú", 'U'] and syllabes[-5][1] in ['A', 'Á']:
                            changements.append('')
                        elif syllabes[-5][1] in ["O", "Ǫ", "Ọ", "Ú", 'U']:
                            if syllabes[-6][-1] in ['I', 'Í']:
                                changements.append('i')
                            else:
                                changements.append('')
                    #En position explosive
                    else:
                        if syllabes[-6][-1] == 'N':
                            if syllabes[-6][-2] == 'A':
                                changements.append('g')
                            else:
                                changements.append('dr')
                        else:
                            changements.append(syllabes[-5][0])

            #Gestion de H (surtout utile pour les mots provenant du germain)
            elif syllabes[-5][0] == 'H':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][1])
                else:
                    changements.append('')

            #Gestion de J (Surtout utile pour les mots provenant du germain)
            elif syllabes[-5][0] == 'J':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][0])
                else:
                    changements.append(syllabes[-5][0])

            #Gestion de K (Surtout utile pour les mots provenant du germain)
            elif syllabes[-5][0] == 'K':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'W':
                        changements.append('qu')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    changements.append(syllabes[-5][0])

            #Gestion de L
            elif syllabes[-5][0] == 'L':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] in ['O'] and syllabes[-5][2] in ['Ę']:
                            changements.append('ill')
                        else:
                            changements.append('il')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #Épenthèse d'un B après M
                    if syllabes[-6][-1] == 'M':
                        changements.append('bl')
                    #Dénasalisation du N
                    elif syllabes[-6][-1] == 'N':
                        changements.append('gl')
                    elif syllabes[-6][-1] in ['Y']:
                        if syllabes[-6][-2] == 'A' and syllabes[-5][1] == 'Í':
                            changements.append('ll')
                        else:
                            changements.append('l')
                    elif syllabes[-6][-1] == 'Í' and syllabes[-5][1] == 'A':
                        changements.append('ll')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de M
            elif syllabes[-5][0] == 'M':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][0])
                else:
                    changements.append(syllabes[-5][0])

            #Gestion de N
            elif syllabes[-5][0] == 'N':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'T':
                        changements.append('nt')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #Assimilation à la nasale précédente
                    if syllabes[-6][-1] == 'M':
                        changements.append('')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de P
            elif syllabes[-5][0] == 'P':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'C':
                        changements.append('ch')
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-5][1] == 'L':
                        #En milieu intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('bl')
                        #En situation explosive
                        else:
                            changements.append('pl')
                    elif syllabes[-5][1] == 'R':
                        #En position intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('vr')
                        else:
                            changements.append('pr')
                    #L'occlusive sourde labiale se singularise
                    elif syllabes[-5][1] == 'Y':
                        changements.append('ch')
                    elif syllabes[-5][1] == 'W':
                        changements.append('')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #En milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-6][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'Ǫ', 'Ú', 'U'] and syllabes[-5][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'I', 'O', 'Ǫ', 'U', 'Ú']:
                            #Cas particulier
                            if syllabes[-6][-1] == syllabes[-5][-1] and syllabes[-6][-1] == 'A' and syllabes[-5][1] == 'Ú':
                                changements.append('')
                            else:
                                changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-6][-1] in ['O', 'Ọ',] and syllabes[-5][1] in ['A', 'Á', 'E', 'U', 'Ú']:
                            if syllabes[-5][1] in ['A', 'Á']:
                                changements.append('v')
                            else:
                                changements.append('')
                    #En milieu explosif
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de Q
            elif syllabes[-5][0] == 'Q':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    if syllabes[-5][1] == 'W':
                        if syllabes[-5][2] in ['A', 'Ọ']:
                            changements.append('c')
                        else:
                            changements.append('qu')
                    else:
                        changements.append('c')
                else:
                    changements.append(syllabes[-5][0])

            #Gestion de R
            elif syllabes[-5][0] == 'R':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'C':
                        changements.append('rg')
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] == 'E' and syllabes[-5][2] == 'Ǫ':
                            changements.append('r')
                        else:
                            changements.append('rj')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #Épenthèse d'un D après N
                    if syllabes[-6][-1] == 'N':
                        changements.append('dr')
                    #Épenthèse de B après M
                    elif syllabes[-6][-1] == 'M':
                        changements.append('br')
                    #Épenthèse d'un D après L
                    elif syllabes[-6][-1] in ['L', 'S']:
                        changements.append('dr')
                    #Épenthèse d'un T après X
                    elif syllabes[-6][-1] == 'X':
                        changements.append('tr')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de S
            elif syllabes[-5][0] == 'S':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'G':
                        if syllabes[-5][2] == 'L':
                            changements.append('sgl')
                        else:
                            changements.append('sg')
                    elif syllabes[-5][1] == 'R':
                        changements.append('sdr')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-5][1] == 'W':
                        changements.append(syllabes[-5][0])
                    #La sifflante sourde se palatalise au contact du yod
                    elif syllabes[-5][1] == 'Y':
                        if syllabes[-6][-1] == 'S':
                            changements.append('ss')
                        else:
                            changements.append('s')
                    else:
                        changements.append(syllabes[-5][0] + syllabes[-5][1])
                else:
                    changements.append(syllabes[-5][0])

            #Gestion de T
            elif syllabes[-5][0] == 'T':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'C':
                        if syllabes[-5][2] == 'Á':
                            changements.append('ch')
                        else:
                            changements.append('c')
                    elif syllabes[-5][1] == 'L':
                        #Voyelles dans lesquelles le i est déjà présent
                        if syllabes[-6][-1] in ['I', 'Í', 'Ẹ', 'E']:
                            changements.append('l')
                        elif syllabes[-6][-1] in ['B', 'T']:
                            changements.append('l')
                        else:
                            changements.append('il')
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-5][1] == 'R':
                        #En situation intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-6][-1] == 'O' and syllabes[-5][2] == 'Í':
                                changements.append('rr')
                            else:
                                changements.append('r')
                        else:
                            changements.append('tr')
                    elif syllabes[-5][1] == 'S':
                        changements.append('c')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-5][1] == 'W':
                        #Position intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-5][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[-5][1] == 'Y':
                        #En situation intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('s')
                        else:
                            if syllabes[-6][-1] == 'C':
                                changements.append('st')
                            elif syllabes[-5][2] in ['A', 'O', 'Ọ', 'Ǫ', 'U', 'Ú']:
                                changements.append('ç')
                            else:
                                changements.append('c')
                    else:
                        changements.append(syllabes[-5][1])
                else:
                    #En situation intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-6][-1] == 'O' and syllabes[-5][1] == 'Á':
                            changements.append('d')
                        elif syllabes[-6][-1] == 'A' and syllabes[-5][1] == 'Í':
                            changements.append('c')
                        elif syllabes[-6][-1] == 'A' and syllabes[-5][1] == 'Á':
                            changements.append('t')
                        else:
                            changements.append('')
                    else:
                        if syllabes[-6][-1] == 'C':
                            changements.append('c')
                        elif syllabes[-6][-2] + syllabes[-6][-1] == 'ỌG':
                            if syllabes[-5][1] == 'Í':
                                changements.append('t')
                            else:
                                changements.append('d')
                        else:
                            changements.append(syllabes[-5][0])

            #Gestion de V (wau ancien)
            elif syllabes[-5][0] == 'V':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5][1] == 'R':
                        changement.append('vr')
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    if syllabes[-5][1] == 'Y':
                        #En milieu intervocalique
                        if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('j')
                        else:
                            changements.append('j')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #En milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-6][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ọ'] and syllabes[-5][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'I', 'O', 'Ǫ', 'U', 'Ú']:
                            changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-6][-1] in ['Ǫ', 'Ú'] and syllabes[-5][1] in ['A', 'Á', 'E', 'Ẹ', 'I', 'O', 'U']:
                            changements.append('')
                    else:
                        if syllabes[-5][1] == 'A':
                            if len(syllabes[-5]) > 2 and syllabes[-5][1] in ['D', 'L', 'S']:
                                changements.append('v')
                            else:
                                changements.append('g')
                        else:
                            changements.append(syllabes[-5][0])

            #Gestion de W (wau récent) (Probablement inexistant en cette position)
            elif syllabes[-5][0] == 'W':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-5] == 'WS':
                        changements.append('')
                    elif syllabes[-5][1] == 'Y':
                        changements.append('j')
                    else:
                        changements.append(syllabes[-5][0])
                else:
                    #En milieu intervocalique
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-6][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ọ'] and syllabes[-5][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'I', 'O', 'Ǫ', 'U', 'Ú']:
                            changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-6][-1] in ['Ǫ', 'Ú'] and syllabes[-5][1] in ['A', 'Á', 'E', 'Ẹ', 'I', 'O', 'U']:
                            changements.append('')
                    else:
                        if syllabes[-6][-1] == 'N':
                            changements.append('')
                        elif syllabes[-5][1] in ['Á', 'E', 'Ẹ', 'Ę', 'I', 'Í']:
                            changements.append('gu')
                        else:
                            changements.append('g')

            #Gestion de X (Probablement inexistant en cette position)
            elif syllabes[-5][0] == 'X':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][0])
                else:
                    if syllabes[-6][-1] in ['A', 'E'] and syllabes[-5][1] in ['Á', 'A']:
                        changements.append('ss')
                    else:
                        changements.append(syllabes[-5][0])

            #Gestion de Y
            elif syllabes[-5][0] == 'Y':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][1])
                else:
                    if syllabes[-6][-1] == 'S':
                        changements.append('')
                    elif syllabes[-6][-1] == 'M':
                        if syllabes[-5][1] == 'Á':
                            changements.append('g')
                        else:
                            changements.append('j')
                    elif syllabes[-6][-1] == 'N':
                        changements.append('')
                    elif syllabes[-6][-1] == 'E' and syllabes[-5][1] == 'Á':
                        changements.append('ii')
                    elif syllabes[-6][-1] == 'G' and syllabes[-5][1] == 'Á':
                        changements.append('gi')
                    elif syllabes[-6][-1] == 'V' and syllabes[-5][1] == 'Á':
                        changements.append('g')
                    elif syllabes[-6][-1] == 'Q' and syllabes[-5][1] == 'Á':
                        changements.append('ci')
                    elif syllabes[-6][-1] == 'Y':
                        changements.append('')
                    else:
                        changements.append('j')

            #Gestion de Z (Probablement inexistant en cette position)
            elif syllabes[-5][0] == 'Z':
                if syllabes[-5][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-5][0])
                else:
                    changements.append(syllabes[-5][0])

        #Vocalisme atone
        #A
        if 'A' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                if syllabes[-4][0] + syllabes[-4][1] == 'TY':
                    changements.append('ei')
                else:
                    changements.append('e')
            #Si A se trouve en position ouvert
            elif syllabes[-5][-1] == 'A':
                if syllabes[-4][0] + syllabes[-4][1] in ['GY', 'TR']:
                    changements.append('ai')
                else:
                    changements.append('e')
            #Si A se trouve en position pénultième
            elif syllabes[-5][-2] == 'A':
                if syllabes[-5][-1] + syllabes[-4][0] + syllabes[-4][1] == 'STR':
                    changements.append('ai')
                elif syllabes[-5][-1] + syllabes[-4][0] in ['LC', 'ND']:
                    changements.append('a')
                else:
                    changements.append('e')
            #Si se trouve en position antépénultième
            elif syllabes[-5][-3] == 'A':
                changements.append('e')
            #Tous les autres cas de figure
            else:
                changements.append('e')

        #E
        elif 'E' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                changements.append('')
            #Si E se trouve en position ouvert
            elif syllabes[-5][-1] == 'E':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('e')
                else:
                    changements.append('')
            #Si E se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'E':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('e')
                else:
                    changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-5][-3] == 'E':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('e')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #I
        elif 'I' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                changements.append('')
            #Si I se trouve en position ouvert
            elif syllabes[-5][-1] == 'I':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('i')
                else:
                    changements.append('')
            #Si I se trouve en position pénultième
            elif syllabes[-5][-2] == 'I':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('i')
                else:
                    changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-5][-3] == 'I':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('i')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #O
        elif 'O' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                changements.append('')
            #Si O se trouve en position ouvert
            elif syllabes[-5][-1] == 'O':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('o')
                else:
                    changements.append('')
            #Si O se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'O':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('o')
                else:
                    changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-5][-3] == 'O':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('o')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #U
        elif 'U' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                changements.append('')
            #Si U se trouve en position ouvert
            elif syllabes[-5][-1] == 'U':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('u')
                else:
                    changements.append('')
            #Si U se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'U':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('u')
                else:
                    changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-5][-3] == 'U':
                #Présence d'un préfixe
                if syllabes[-5][0] == ' ' or syllabes[-6][-1] == ' ':
                    changements.append('u')
                else:
                    changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #Vocalisme
        #Á tonique
        if 'Á' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                #influence des nasales
                if syllabes[-4][0] in ['M', 'N']:
                    changements.append('ai')
                elif  syllabes[-4][0] + syllabes[-4][1] in ['CW']:
                    changements.append('ui')
                #Ouverture s'il y a un A
                if syllabes[-6][-1] == 'A':
                    changements.append('a')
                else:
                    changements.append('e')
            #Si A tonique se trouve en position ouverte
            elif syllabes[-5][-1] == 'Á':
                #Loi de Bartsh
                if syllabes[-5][-2] in ['C', 'X']:
                    if syllabes[-6][-1] == 'O':
                        changements.append('e')
                    else:
                        changements.append('ie')
                elif len(syllabes[-5]) > 2 and syllabes[-5][-3] + syllabes[-5][-2] in ['CT', 'BY', 'SY', 'YT', 'TY', 'GR', 'GL']:
                    changements.append('ie')
                elif syllabes[-6][-1] + syllabes[-5][0] in ['CT', 'GT', 'YT', 'MY', 'SY', 'VY']:
                    changements.append('ie')
                #influence des nasales
                elif syllabes[-4][0] in ['M', 'N']:
                    changements.append('ai')
                elif syllabes[-4][0] + syllabes[-4][1] in ['RY']:
                    if syllabes[-6] == syllabes[0] == 'BRE':
                        changements.append('iai')
                    else:
                        changements.append('ie')
                elif syllabes[-4][0] + syllabes[-4][1] in ['CL', 'LY']:
                    changements.append('a')
                elif syllabes[-4][0] + syllabes[-4][1] in ['CT', 'CY', 'GT', 'YT', 'MY', 'SY', 'TY', 'VY']:
                    changements.append('ai')
                else:
                    changements.append('e')
            #Si A tonique se trouve au milieu de la syllabe
            elif syllabes[-5][-2] == 'Á':
                #Loi de Bartsh
                if syllabes[-5][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[-5]) > 2 and syllabes[-5][-3] + syllabes[-5][-2] in ['CT']:
                    changements.append('ie')
                #Fermeture de A tonique face à un wau
                elif syllabes[-5][-1] == 'W':
                    changements.append('o')
                elif syllabes[-5][-1] + syllabes[-4][0] == 'GD':
                    changements.append('au')
                else:
                    changements.append('a')
            #Si se trouve en position antépénultième
            elif syllabes[-5][-3] == 'Á':
                #Loi de Bartsh
                if syllabes[-5][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[-5]) > 2 and syllabes[-5][-3] + syllabes[-5][-2] in ['CT']:
                    changements.append('ie')
                else:
                    changements.append('a')
            #Autres cas de figure, plus rare ou A tonique ne se trouve dans aucune de ces positions
            else:
                changements.append('a')

        #Ẹ fermé
        elif 'Ẹ' in syllabes[-5]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                #influence des nasales
                if syllabes[-4][0] in ['M', 'N']:
                    if syllabes[-4][1] == 'A':
                        changements.append('ei')
                    elif syllabes[-4][-1] == 'Ī':
                        changements.append('i')
                    else:
                        changements.append('e')
                #Métaphonie
                elif syllabes[-4][-1] == 'Ī':
                    changements.append('i')
                #Anaphonie
                elif syllabes[-4][0] == 'Y':
                    changements.append('i')
                elif syllabes[-4][0] + syllabes[-4][1] in ['BY', 'CY', 'DY', 'FY', 'GY' 'LY', 'RY', 'TY', 'VY']:
                    changements.append('i')
                elif syllabes[-4][0] + syllabes[-4][1] in ['GA', 'GÁ', 'GĘ', 'GE', 'GI', 'GÍ', 'GN']:
                    changements.append('i')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position ouverte
            elif syllabes[-5][-1] == 'Ẹ':
                #Fermeture occasionnée par le groupe PW qui suit
                if len(syllabes[-4]) > 1 and syllabes[-4][0] + syllabes[-4][1] == 'PW':
                    changements.append('u')
                #Sous l'influence de la palatale qui suit, la diphtongue se ferme
                elif len(syllabes[-4]) > 1 and syllabes[-4][0] + syllabes[-4][1] == 'GY':
                    changements.append('e')
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                elif syllabes[-5][-2] == 'C':
                    if syllabes[-6][-1] in listes_lettres['toutes_les_voyelles']:
                        changements.append('i')
                    else:
                        changements.append('ei')
                #influence des nasales
                elif syllabes[-4][0] in ['M', 'N']:
                    if syllabes[-4][1] == 'A':
                        changements.append('ei')
                    elif syllabes[-4][-1] == 'Ī':
                        changements.append('i')
                    else:
                        changements.append('e')
                #Métaphonie
                elif syllabes[-4][-1] == 'Ī':
                    changements.append('i')
                #Anaphonie
                elif syllabes[-4][0] == 'Y':
                    changements.append('i')
                elif syllabes[-4][0] + syllabes[-4][1] in ['BY', 'CY', 'DY', 'FY', 'LY', 'RY', 'TY', 'VY']:
                    changements.append('i')
                elif syllabes[-4][0] + syllabes[-4][1] in ['GA', 'GÁ', 'GĘ', 'GE', 'GI', 'GÍ', 'GN']:
                    changements.append('i')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position fermée
            elif syllabes[-5][-2] == 'Ẹ':
                #influence des nasales
                if syllabes[-5][-1] in ['M', 'N']:
                    #Contact avec un groupe consonantique dégageant un yod
                    if syllabes[-4][0] == 'C':
                        if syllabes[-4][1] in ['Y', 'U']:
                            changements.append('e')
                        else:
                            changements.append('ei')
                    elif syllabes[-4][-1] == 'Ī':
                        changements.append('i')
                    else:
                        changements.append('e')
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                #Arrondissement dû aux séquences intervocaliques CW PW
                elif len(syllabes[-5]) > 3 and syllabes[-5][-4] + syllabes[-5][-3] in ['CW', 'PW']:
                    changements.append('u')
                elif syllabes[-5][-3] == 'C':
                    changements.append('i')
                #Fermeture en [i]
                elif syllabes[-5][-1] + syllabes[-4][0] in ['YS', 'YY']:
                    changements.append('i')
                #influence d'un I long
                elif syllabes[-4][-1] == 'Ī':
                    changements.append('i')
                #Problème lors de la répartition des syllabes
                elif syllabes[-5][-1] + syllabes[-4][0] == 'CT':
                    changements.append('ei')
                else:
                    changements.append('e')
            #Si se trouve en position antépénultième
            elif syllabes[-5][-3] == 'Ẹ':
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                if syllabes[-5][-3] == 'C':
                    changements.append('i')
                #Métaphonie
                elif syllabes[-4][-1] == 'Ī':
                    changements.append('i')
                else:
                    changements.append('e')
            #Si E fermé se trouve en position fermée
            else:
                #Métaphonie
                if syllabes[-4][-1] == 'Ī':
                    changements.append('i')
                else:
                    changements.append('e')

        #Ę ouvert
        elif 'Ę' in syllabes[-5]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                if syllabes[-4][0] + syllabes[-4][1] in ['CT', 'BY', 'SY', 'TY']:
                    changements.append('i')
                elif syllabes[-4][0] == 'X':
                    changements.append('i')
                elif syllabes[-4][0] + syllabes[-4][1] in ['TW']:
                    changements.append('ui')
                elif syllabes[-4][0] + syllabes[-4][1] in ['CW']:
                    changements.append('iu')
                else:
                    changements.append('ie')
            #Si E ouvert se trouve en position finale
            elif syllabes[-5][-1] == 'Ę':
                if syllabes[-4][0] + syllabes[-4][1] in ['CT', 'BY', 'SY', 'TY']:
                    changements.append('i')
                elif syllabes[-4][0] == 'X':
                    changements.append('i')
                elif syllabes[-4][0] + syllabes[-4][1] in ['TW']:
                    changements.append('ui')
                elif syllabes[-4][0] + syllabes[-4][1] in ['CW']:
                    changements.append('iu')
                else:
                    changements.append('ie')
            #Si E ouvert se trouve en position pénultième
            elif syllabes[-5][-2] == 'Ę':
                if syllabes[-5][-1] + syllabes[-4][0] in ['MT', 'RT', 'PT', 'TT', 'PD', 'DC']:
                    changements.append('ie')
                #Influence d'un groupe dégageant un yod
                elif syllabes[-5][-1] + syllabes[-4][0] in ['CT', 'SY', 'YC', 'YD', 'YY', 'YN', 'QW']:
                    changements.append('i')
                elif syllabes[-5][-1] + syllabes[-4][0] + syllabes[-4][1] == 'SCR':
                    changements.append('ei')
                else:
                    changements.append('e')
            #Si E ouvert se trouve en position antépénultième
            elif syllabes[-5][-3] == 'Ę':
                changements.append('e')
            #Si E ouvert se trouve en position fermée
            else:
                changements.append('e')

        #Í tonique
        elif 'Í' in syllabes[-5]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-5]) == 1:
                changements.append('i')
            #Si I tonique se trouve en position finale
            elif syllabes[-5][-1] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position pénultième
            elif syllabes[-5][-2] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position antépénultième
            elif syllabes[-5][-3] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position fermée
            else:
                changements.append('i')

        #Ọ fermé
        elif 'Ọ' in syllabes[-5]:
            if len(syllabes[-5]) == 1:
                #influence des nasales
                if syllabes[-4][0] in ['M', 'N']:
                    changements.append('o')
                #Métaphonie
                elif syllabes[-4][-1] == 'Ī':
                    changements.append('u')
                #Anaphonie
                elif syllabes[-4][0] == 'Y':
                    changements.append('u')
                elif syllabes[-4][0] + syllabes[-4][1] in ['BY', 'CY', 'DY', 'FY', 'GY', 'LY', 'RY', 'TY', 'VY']:
                    changements.append('u')
                elif syllabes[-4][0] + syllabes[-4][1] in ['GÁ', 'GĘ', 'GE', 'GI', 'GÍ', 'GN']:
                    changements.append('u')
                else:
                    changements.append('ou')
            #Si O fermé se trouve en position finale
            elif syllabes[-5][-1] == 'Ọ':
                #influence des nasales
                if syllabes[-4][0] in ['M', 'N']:
                    changements.append('o')
                #Métaphonie
                elif syllabes[-4][-1] == 'Ī':
                    changements.append('u')
                #Anaphonie
                elif syllabes[-4][0] == 'Y':
                    changements.append('u')
                elif syllabes[-4][0] + syllabes[-4][1] in ['BY', 'CY', 'DY', 'FY', 'GY', 'LY', 'TY', 'VY']:
                    changements.append('u')
                elif syllabes[-4][0] + syllabes[-4][1] in ['GÁ', 'GĘ', 'GE', 'GI', 'GÍ', 'GN']:
                    changements.append('u')
                elif syllabes[-4][0] + syllabes[-4][1] == 'RY':
                    changements.append('oi')
                else:
                    changements.append('ou')
            #Si O fermé se trouve en position pénultième
            elif syllabes[-5][-2] == 'Ọ':
                #Métaphonie
                if syllabes[-4][-1] == 'Ī':
                    changements.append('u')
                elif syllabes[-5][-1] + syllabes[-4][0] == 'NY':
                    changements.append('oi')
                elif syllabes[-5][-1] + syllabes[-4][0] + syllabes[-4][1] == 'NDY':
                    changements.append('oi')
                else:
                    changements.append('o')
            #Si O fermé se trouve en position antépénultième
            elif syllabes[-5][-3] == 'Ọ':
                #Métaphonie
                if syllabes[-4][-1] == 'Ī':
                    changements.append('u')
                else:
                    changements.append('o')
            #Toutes les autres positions
            else:
                #Métaphonie
                if syllabes[-4][-1] == 'Ī':
                    changements.append('u')
                else:
                    changements.append('o')

        #Ǫ ouvert
        elif 'Ǫ' in syllabes[-5]:
            if len(syllabes[-5]) == 1:
                #influence des nasales
                if syllabes[-2][0] in ['M', 'N']:
                    if syllabes[-2][1] == 'O':
                        changements.append('ue')
                    else:
                        changements.append('o')
                elif syllabes[-4][0] + syllabes[-4][1] in ['CT', 'CW']:
                    changements.append('ui')
                else:
                    changements.append('ue')
            #Si O ouvert se trouve en position finale
            elif syllabes[-5][-1] == 'Ǫ':
                if len(syllabes[-5]) > 2 and syllabes[-5][-3] + syllabes[-5][-2] == 'TY':
                    changements.append('io')
                elif syllabes[-4][0]  + syllabes[-4][1] == 'PY':
                    changements.append('o')
                #influence des nasales et de la sifflante sourde
                elif syllabes[-4][0] in ['M', 'N', 'S']:
                    changements.append('o')
                elif syllabes[-4][0] == 'X':
                    changements.append('ui')
                elif syllabes[-4][0] + syllabes[-4][1] in ['CT', 'CW']:
                    changements.append('ui')
                elif syllabes[-4][-1] == 'Ī':
                    changements.append('oi')
                else:
                    changements.append('ue')
            #Si O ouvert se trouve en position pénultième
            elif syllabes[-5][-2] == 'Ǫ':
                #Présence d'un groupe consonantique dégageant un yod
                if syllabes[-5][-1] + syllabes[-4][0] in ['CT', 'YY']:
                    changements.append('ui')
                elif syllabes[-5][-1] + syllabes[-4][0] in ['YN']:
                    changements.append('oi')
                else:
                    changements.append('o')
            #Si O ouvert se trouve en position antépénultième
            elif syllabes[-5][-3] == 'Ǫ':
                if syllabes[-5][-2] + syllabes[-5][-1] == 'YS':
                    changements.append('ui')
                else:
                    changements.append('o')
            #Toutes les autres positions
            else:
                changements.append('o')

        #Ú tonique
        elif 'Ú' in syllabes[-5]:
            if len(syllabes[-5]) == 1:
                changements.append('u')
            #Si U tonique se trouve en position finale
            elif syllabes[-5][-1] == 'Ú':
                changements.append('u')
            #SiU tonique se trouve en position pénultième
            elif syllabes[-5][-2] == 'Ú':
                changements.append('u')
            #Si U tonique se trouve en position antépénultième
            elif syllabes[-5][-3] == 'Ú':
                changements.append('u')
            #Toutes les autres positions
            else:
                changements.append('u')

        #Consonantisme final
        if syllabes[-5][-1] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-5][-1] == 'B':
                if syllabes[-4][0] + syllabes[-4][1] == 'TR':
                    changements.append('z')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de C
            elif syllabes[-5][-1] == 'C':
                if syllabes[-5][-2] == 'N':
                    changements.append('nc')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de D
            elif syllabes[-5][-1] == 'D':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de F
            elif syllabes[-5][-1] == 'F':
                if syllabes[-5][-2] == 'Ọ' and syllabes[-4][0] + syllabes[-4][1] == 'FR':
                    changements.append('f')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de G
            elif syllabes[-5][-1] == 'G':
                #Assimilation au N suivant
                if syllabes[-4][0] == 'N':
                    if syllabes[-4] == syllabes[-1]:
                        changements.append('')
                    else:
                        changements.append('g')
                elif syllabes[-5][-2] in ['A', 'Ẹ', 'Ọ'] and syllabes[-4][0] in ['S', 'D', 'T']:
                    changements.append('i')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('')

            #Gestion de H (ne devrait pas exister ou cas très très rare)
            elif syllabes[-5][-1] == 'H':
                changements.append('')

            #Gestion de L
            elif syllabes[-5][-1] == 'L':
                if syllabes[-4][0] == 'L':
                    if syllabes[-5][-2] in ['A', 'E', 'Ẹ', 'Ę'] and syllabes[-4][1] in ['A', 'Ę', 'Ọ']:
                        changements.append('l')
                    else:
                        changements.append('')
                #Dernière lettre d'un préfixe
                elif syllabes[-5][0] == ' ':
                    changements.append('l')
                elif syllabes[-4][0] + syllabes[-4][1] == 'GR':
                    if syllabes[-5][-2] == 'Ọ':
                        changements.append('u')
                    else:
                        changements.append('l')
                elif syllabes[-4][0] + syllabes[-4][1] == 'CT':
                    changements.append('l')
                else:
                    #La liquide se vocalise en [w]
                    changements.append('u')

            #Gestion de M
            elif syllabes[-5][-1] == 'M':
                if syllabes[-4][0]  in ['B', 'C', 'T', 'Y']:
                    changements.append('n')
                elif syllabes[-4][0] + syllabes[-4][1] in ['BY', 'QW']:
                    changements.append('n')
                elif syllabes[-4][0] == 'M':
                    changements.append('')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('m')

            #Gestion de N
            elif syllabes[-5][-1] == 'N':
                if syllabes[-4][0] == 'Y':
                    changements.append('gn')
                elif syllabes[-4][0] + syllabes[-4][1] == 'DY':
                    changements.append('gn')
                elif syllabes[-4][0] == 'N':
                    if syllabes[-5][-2] in ['Ẹ', 'Ǫ'] and syllabes[-4][1] in ['A', 'Á']:
                        changements.append('n')
                    else:
                        changements.append('')
                else:
                    changements.append('n')

            #Gestion de P
            elif syllabes[-5][-1] == 'P':
                #Si c'est un mot venant de l'adstrat grec
                if syllabes[-4][0] == 'H':
                    changements.append('p')
                elif syllabes[-4][0] == 'P':
                    if syllabes[-5][-2] == 'A' and syllabes[-4][1] == 'Ę':
                        changements.append('p')
                    else:
                        changements.append('')
                #Assimilation à la consonne suivante
                else:
                    changements.append('')

            #Gestion de Q
            elif syllabes[-5][-1] == 'Q':
                if syllabes[-4][0] == 'W':
                    if syllabes[-5][-2] in ['A', 'Ę', 'Í'] and syllabes[-4][1] in ['A', 'R']:
                        changements.append('v')
                    elif syllabes[-5][-2] in ['E', 'Í'] and syllabes[-4][1] in ['Ę', 'U']:
                        changements.append('')
                    else:
                        changements.append('qu')
                else:
                    changements.append('')

            #Gestion de R
            elif syllabes[-5][-1] == 'R':
                if syllabes[-4][0] == 'R':
                    if syllabes[-5][-2] in ['E', 'Ę', 'O'] and syllabes[-4][1] in ['A', 'Ọ']:
                        changements.append('r')
                    else:
                        changements.append('')
                #En cas de mauvaise découpe syllabique
                elif syllabes[-5] in ['FR', 'TR']:
                    changements.append('')
                else:
                    #La vibrante est très stable
                    changements.append(syllabes[-5][-1])

            #Gestion de S
            elif syllabes[-5][-1] == 'S':
                if syllabes[-4][0] == 'S':
                    if syllabes[-5][-2] in ['A', 'E', 'Ẹ', 'Ǫ', 'U'] and syllabes[-4][1] in ['A', 'Á', 'Ę', 'Í', 'Y']:
                        changements.append('s')
                    else:
                        changements.append('')
                #En cas de mauvaise découpe syllabique
                elif syllabes[-5] == 'TS':
                    changements.append('')
                else:
                    changements.append('s')

            #Gestion de T
            elif syllabes[-5][-1] == 'T':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de V
            elif syllabes[-5][-1] == 'V':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de W
            elif syllabes[-5][-1] == 'W':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de X
            elif syllabes[-5][-1] == 'X':
                changements.append('s')

            #Gestion de Y
            elif syllabes[-5][-1] == 'Y':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Z
            elif syllabes[-5][-1] == 'Z':
                #Assimilation à la consonne suivante
                changements.append('')

        return changements
