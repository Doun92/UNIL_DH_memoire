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

'consonnes_et_semi_consonnes' : ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],

'consonantisme_explosif_complexe_2_lettres' : [
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

class SyllabePenultieme:

    def __init__(self):
        return

    def syllabe_penultieme(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        if syllabes[-2][0] == ' ':
            changements.append(syllabes[-2][1])

        #Consoantisme initial
        if syllabes[-2][0] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-2][0] == 'B':
                #Consonantisme complexe
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    #Cette séquence se maintient en milieu intervocalique
                    if syllabes[-2][1] == 'C':
                        changements.append('g')
                    elif syllabes[-2][1] == 'D':
                        changements.append('d')
                    elif syllabes[-2][1] == 'L':
                        if syllabes[-3][-1] == 'M' and syllabes[-2][2] == 'Í':
                            changements.append('br')
                        else:
                            changements.append('bl')
                    elif syllabes[-2][1] == 'R':
                        if syllabes[-2] == 'BR':
                            changements.append('')
                        #En milieu intervocalique
                        elif syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('vr')
                        #En situation explosive
                        else:
                            changements.append('br')
                    elif syllabes[-2][1] == 'Y':
                        #En milieu intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            #En milieu palatal
                            if syllabes[-3][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ǫ'] and syllabes[-2][2] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'U', 'Ú']:
                                changements.append('g')
                            #En milieu palatal, mais avec une graphie différente
                            elif syllabes[-3][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ǫ'] and syllabes[-2][2] in ['Ǫ']:
                                changements.append('j')
                            #En milieu vélaire
                            elif syllabes[-3][-1] in ['Ọ', 'Ú'] and syllabes[-2][2] in ['A', 'E', 'U']:
                                changements.append('')
                        #En milieu explosif
                        else:
                            changements.append('g')
                    elif syllabes[-2][1] == 'W':
                        #En milieu intervocalique
                        #Amuïssement, non sans avoir provoqué un arrondissement de la voyelle tonique qui suit ou qui précède
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-3][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ǫ'] and syllabes[-2][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ǫ', 'U', 'Ú']:
                            #Cas particulier
                            if syllabes[-3][-1] == syllabes[0][-1] and syllabes[-3][-1] == 'A' and syllabes[-2][1] == 'Ú':
                                changements.append('')
                            else:
                                changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-3][-1] in ['Ọ', 'Ú'] and syllabes[-2][1] in ['A', 'Á', 'E', 'Ẹ', 'U']:
                            if syllabes[-1][0] in ['D', 'R']:
                                changements.append('v')
                            else:
                                changements.append('')
                    #En milieu explosif
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de C
            elif syllabes[-2][0] == 'C':
                #Consonantisme complexe
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-2][1] == 'L':
                        #En milieu intervocalique
                        #Les palatales combinées avec un L aboutissent en un L mouill
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-3][-1] in ['I', 'Í', 'Ẹ', 'E',]:
                                changements.append('l')
                            else:
                                changements.append('il')
                        elif syllabes[-3][-2] + syllabes[-3][-1] == 'EC' and syllabes[-2][2] == 'Ę':
                            changements.append('gl')
                        #Après S la séquence CL se simplifie en [l]
                        elif syllabes[-3][-1] == 'S':
                            changements.append('l')
                        else:
                            changements.append('cl')
                    elif syllabes[-2][1] == 'T':
                        changements.append('c')
                    elif syllabes[-2][1] == 'R':
                        #En milieu intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-3][-1] in ['I', 'Í', 'Ẹ', 'E', 'Ǫ']:
                                changements.append('r')
                            else:
                                changements.append('ir')
                        elif syllabes[-3][-1] == 'N':
                            changements.append('tr')
                        else:
                            changements.append('cr')
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] == 'D':
                            changements.append('gi')
                        elif syllabes[-3][-1] == 'S':
                            changements.append('s')
                        elif syllabes[-3][-1] == 'Á' and syllabes[-2][2] == 'Á':
                            changements.append('s')
                        else:
                            changements.append('c')
                    elif syllabes[-2][1] == 'W':
                        #En milieu intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append('c')
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][1] in ['I', 'Í', 'E', 'Ẹ', 'Ę']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-3][-1] in ['I', 'Í', 'Ẹ', 'E',]:
                                changements.append('s')
                            else:
                                changements.append('is')
                        elif syllabes[-3][-1] in ['A', 'Á', 'I', 'Í', 'E', 'Ẹ', 'Ę'] and syllabes[-2][1] in ['A', 'Á']:
                            if syllabes[-3][-1] in ['I', 'Í', 'Ẹ', 'E']:
                                changements.append('')
                            else:
                                changements.append('i')
                        elif syllabes[-3][-1] in ["O", "Ǫ", "Ọ", "Ú", 'U'] and syllabes[-2][1] in ['A', 'Á']:
                            changements.append('')
                        elif syllabes[-2][1] in ["O", "Ǫ", "Ọ", "Ú", 'U']:
                            if syllabes[-3][-1] in ['Á', 'Í']:
                                changements.append('i')
                            else:
                                changements.append('')
                    #En position explosive
                    #Palatalisation de C devant A
                    elif syllabes[-2][1] in ['A', 'Á']:
                        if syllabes[-3][-1] == 'M':
                            changements.append('g')
                        else:
                            changements.append('ch')
                    elif syllabes[-3][-1] in ['C', 'L']:
                        changements.append('c')
                    elif syllabes[-2][1] == "Ọ":
                        if syllabes[-3][-1] == ' ':
                            changements.append('c')
                        else:
                            changements.append('g')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de D
            elif syllabes[-2][0] == 'D':
                #Consonantisme complexe
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    if syllabes[-2][1] == 'C':
                        changements.append('g')
                    elif syllabes[-2][1] == 'L':
                        changements.append('l')
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-2][1] == 'R':
                        #En situation intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('r')
                        else:
                            changements.append('dr')
                    elif syllabes[-2][1] == 'Y':
                        #En situation intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        elif syllabes[-3][-1] == 'D':
                            changements.append('j')
                        elif syllabes[-3][-1] == 'N':
                            changements.append('')
                        else:
                            changements.append('g')
                    elif syllabes[-2][1] == 'W':
                        #En situation intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append('d')
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        changements.append('')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de F
            elif syllabes[-2][0] == 'F':
                #Consonantisme complexe
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-2][1] == 'L':
                        changements.append('fl')
                    elif syllabes[-2][1] == 'R':
                        changements.append('fr')
                #Consonantisme simple
                else:
                    #En milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-3][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ǫ'] and syllabes[-2][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                            changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-3][-1] in ['Ọ', 'Ú'] and syllabes[-2][1] in ['A', 'E', 'U']:
                            changements.append('')
                    else:
                        if syllabes[-3][-2] + syllabes[-3][-1] == 'E ' and syllabes[-2][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                            if syllabes[-3][-1] == ' ':
                                changements.append('f')
                            else:
                                changements.append('v')
                        else:
                            changements.append(syllabes[-2][0])


            #Gestion de G
            elif syllabes[-2][0] == 'G':
                #Consonantisme complexe
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Consonantisme explosif complexe
                    #En position initiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    if syllabes[-2][1] == 'L':
                        #Position intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-3][-1] in ['I', 'Í', 'Ẹ', 'E',]:
                                if syllabes[-2][2] == 'Á':
                                    changements.append('ll')
                                else:
                                    changements.append('l')
                            else:
                                if syllabes[-3][-1] in ['A'] and syllabes[-2][2] == 'Á':
                                    changements.append('ill')
                                else:
                                    changements.append('il')
                        else:
                            changements.append('gl')
                    elif syllabes[-2][1] == 'N':
                        changements.append('gn')
                    elif syllabes[-2][1] == 'R':
                        #En milieu intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            #Voyelles dans lesquelles le i est déjà présent
                            if syllabes[-3][-1] in ['I', 'Í', 'Ẹ', 'E',]:
                                changements.append('r')
                            else:
                                changements.append('ir')
                        else:
                            changements.append('gr')
                    elif syllabes[-2][1] == 'T':
                        changements.append('t')
                    elif syllabes[-2][1] == 'Y':
                        #En milieu intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-3][-1] == 'Í':
                                changements.append('')
                            else:
                                changements.append('i')
                        else:
                            cchangements.append('g')
                    elif syllabes[-2][1] == 'W':
                        #En milieu intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append('g')
                else:
                    #En milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-3][-1] == 'Í' and syllabes[-2][1] == 'Í':
                            changements.append('g')
                        elif syllabes[-2][1] in ['I', 'Í', 'E', 'Ẹ', 'Ę']:
                            changements.append('')
                        elif syllabes[-3][-1] in ['A', 'Á', 'I', 'Í', 'E', 'Ẹ', 'Ę'] and syllabes[-2][1] in ['A', 'Á']:
                            changements.append('i')
                        elif syllabes[-3][-1] in ["O", "Ǫ", "Ọ",] and len(syllabes[-2]) > 1 and syllabes[-2][1] in ['A', 'Á']:
                            changements.append('v')
                        elif syllabes[-3][-1] in ["Ú", 'U'] and syllabes[-2][1] in ['A', 'Á']:
                            changements.append('')
                        elif syllabes[-2][1] in ["O", "Ǫ", "Ọ", "Ú", 'U']:
                            if syllabes[-3][-1] in ['I', 'Í']:
                                changements.append('i')
                            else:
                                changements.append('')
                    #En position explosive
                    #Palatalisation de G devant A (graphie en j)
                    elif syllabes[-2][1] in ['A', 'Á']:
                        changements.append('g')
                    else:
                        if syllabes[-3][-1] == 'N':
                            if syllabes[-3][-2] == 'A':
                                changements.append('g')
                            else:
                                changements.append('dr')
                        else:
                            changements.append(syllabes[-2][0])

            #Gestion de H (surtout utile pour les mots provenant du germain)
            elif syllabes[-2][0] == 'H':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][1])
                else:
                    if syllabes[-3][-1] == 'P':
                        changements.append('h')
                    else:
                        changements.append('')

            #Gestion de J (Surtout utile pour les mots provenant du germain)
            elif syllabes[-2][0] == 'J':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][0])
                else:
                    changements.append(syllabes[-2][0])

            #Gestion de K (Surtout utile pour les mots provenant du germain)
            elif syllabes[-2][0] == 'K':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'W':
                        changements.append('qu')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    changements.append(syllabes[-2][0])

            #Gestion de L
            elif syllabes[-2][0] == 'L':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'M':
                        changements.append('lm')
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] in ['O'] and syllabes[-2][2] in ['Ę']:
                            changements.append('ill')
                        else:
                            changements.append('il')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #Épenthèse d'un B après M
                    if syllabes[-3][-1] == 'M':
                        changements.append('bl')
                    #Dénasalisation du N
                    elif syllabes[-3][-1] == 'N':
                        changements.append('gl')
                    elif syllabes[-3][-1] in ['Y']:
                        if syllabes[-3][-2] == 'A' and syllabes[-2][1] == 'Í':
                            changements.append('ll')
                        else:
                            changements.append('l')
                    elif syllabes[-3][-1] == 'Í' and syllabes[-2][1] == 'A':
                        changements.append('ll')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de M
            elif syllabes[-2][0] == 'M':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][0])
                else:
                    changements.append(syllabes[-2][0])

            #Gestion de N
            elif syllabes[-2][0] == 'N':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'T':
                        changements.append('nt')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #Assimilation à la nasale précédente
                    if syllabes[-3][-1] == 'M':
                        changements.append('')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de P
            elif syllabes[-2][0] == 'P':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'C':
                        changements.append('ch')
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-2][1] == 'L':
                        #En milieu intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-3][-1] == 'O' and syllabes[-2][2] == 'Í':
                                changements.append('pl')
                            else:
                                changements.append('bl')
                        #En situation explosive
                        else:
                            changements.append('pl')
                    elif syllabes[-2][1] == 'R':
                        #En position intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('vr')
                        else:
                            changements.append('pr')
                    elif syllabes[-2][1] == 'T':
                        changements.append('t')
                    #L'occlusive sourde labiale se singularise
                    elif syllabes[-2][1] == 'Y':
                        changements.append('ch')
                    elif syllabes[-2][1] == 'W':
                        changements.append('')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #En milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-3][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'Ǫ', 'Ú', 'U'] and syllabes[-2][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                            #Cas particulier
                            if syllabes[-3][-1] == syllabes[0][-1] and syllabes[-3][-1] == 'A' and syllabes[-2][1] == 'Ú':
                                changements.append('')
                            else:
                                changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-3][-1] in ['O', 'Ọ'] and syllabes[-2][1] in ['A', 'Á', 'E', 'U', 'Ú']:
                            #Le A récupère le [v]
                            if syllabes[-2][1] in ['A', 'Á']:
                                changements.append('v')
                            else:
                                changements.append('')
                    #En milieu explosif
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de Q
            elif syllabes[-2][0] == 'Q':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    if syllabes[-2][1] == 'W':
                        if len(syllabes[-2]) > 2 and syllabes[-2][2] in ['A', 'Ọ']:
                            changements.append('c')
                        else:
                            changements.append('qu')
                    else:
                        changements.append('c')
                else:
                    changements.append(syllabes[-2][0])

            #Gestion de R
            elif syllabes[-2][0] == 'R':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'C':
                        changements.append('rg')
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] == 'E' and syllabes[-2][2] == 'Ǫ':
                            changements.append('r')
                        else:
                            changements.append('rj')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #Épenthèse d'un D après N
                    if syllabes[-3][-1] == 'N':
                        changements.append('dr')
                    #Épenthèse de B après M
                    elif syllabes[-3][-1] == 'M':
                        changements.append('br')
                    #Épenthèse d'un D après L
                    elif syllabes[-3][-1] in ['L', 'S']:
                        changements.append('dr')
                    #Épenthèse d'un T après X
                    elif syllabes[-3][-1] == 'X':
                        changements.append('tr')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de S
            elif syllabes[-2][0] == 'S':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'G':
                        if syllabes[-2][2] == 'L':
                            changements.append('sgl')
                        else:
                            changements.append('sg')
                    elif syllabes[-2][1] == 'R':
                        changements.append('sdr')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-2][1] == 'W':
                        changements.append(syllabes[-2][0])
                    #La sifflante sourde se palatalise au contact du yod
                    elif syllabes[-2][1] == 'Y':
                        if syllabes[-3][-1] == 'S':
                            changements.append('ss')
                        else:
                            changements.append('s')
                    else:
                        changements.append(syllabes[-2][0] + syllabes[-2][1])
                else:
                    changements.append(syllabes[-2][0])

            #Gestion de T
            elif syllabes[-2][0] == 'T':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'C':
                        if syllabes[-2][2] == 'Á':
                            changements.append('ch')
                        else:
                            changements.append('c')
                    elif syllabes[-2][1] == 'L':
                        #Voyelles dans lesquelles le i est déjà présent
                        if syllabes[-3][-1] in ['I', 'Í', 'Ẹ', 'E',]:
                            changements.append('l')
                        elif syllabes[-3][-1] in ['B', 'T']:
                            changements.append('l')
                        else:
                            changements.append('il')
                    elif syllabes[-2][1] == 'M':
                        changements.append('m')
                    #En position intiale, tout élément consonantique complexe constitué d'une consonne et d'une liquide demeure intact
                    elif syllabes[-2][1] == 'R':
                        #En situation intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-3][-1] == 'O' and syllabes[-2][2] == 'Í':
                                changements.append('rr')
                            else:
                                changements.append('r')
                        else:
                            changements.append('tr')
                    #Les éléments en wau perdent généralement leur semi-voyelle
                    elif syllabes[-2][1] == 'W':
                        #Position intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('')
                        else:
                            changements.append(syllabes[-2][0])
                    #La palatale se combine avec le yod pour se stabiliser dans une zone un peu plus avancée que celle de sa sononre correspondante
                    elif syllabes[-2][1] == 'Y':
                        #En situation intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('s')
                        else:
                            if syllabes[-3][-1] in ['N', 'S']:
                                if syllabes[-2][2] == 'Á':
                                    changements.append('c')
                                else:
                                    changements.append('t')
                            elif syllabes[-3][-1] == 'C':
                                changements.append('st')
                            elif syllabes[-2][2] in ['A', 'O', 'Ọ', 'U', 'Ú']:
                                changements.append('ç')
                            else:
                                changements.append('c')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #En situation intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-3][-1] == 'A' and syllabes[-2][1] == 'Á':
                            changements.append('t')
                        else:
                            changements.append('')
                    else:
                        if syllabes[-3] == 'GY':
                            changements.append('d')
                        elif syllabes[-3][-2] + syllabes[-3][-1] == 'ỌG':
                            if syllabes[-2][1] == 'Í':
                                changements.append('t')
                            else:
                                changements.append('d')
                        elif syllabes[-3][-1] == 'C':
                            changements.append('c')
                        else:
                            changements.append(syllabes[-2][0])

            #Gestion de V (wau ancien)
            elif syllabes[-2][0] == 'V':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2][1] == 'R':
                        changement.append('vr')
                    #Les occlusives sonores combinées au yod trouvent leur point d'éqilibre dans la zone palatale
                    if syllabes[-2][1] == 'Y':
                        #En milieu intervocalique
                        if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                            changements.append('j')
                        else:
                            changements.append('v')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #En milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-3][-1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ǫ'] and syllabes[-2][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                            changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-3][-1] in ['Ọ', 'Ú'] and syllabes[-2][1] in ['A', 'E', 'U']:
                            changements.append('')
                    else:
                        if syllabes[-2][1] == 'A':
                            if len(syllabes[-2]) > 2 and syllabes[-2][1] in ['D', 'L', 'S']:
                                changements.append('v')
                            else:
                                changements.append('g')
                        else:
                            changements.append(syllabes[-2][0])

            #Gestion de W (wau récent) (Probablement inexistant en cette position)
            elif syllabes[-2][0] == 'W':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    if syllabes[-2] == 'WS':
                        changements.append('')
                    elif syllabes[-2][1] == 'Y':
                        changements.append('j')
                    else:
                        changements.append(syllabes[-2][0])
                else:
                    #En milieu intervocalique
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-3][-1] in ['Á', 'E', 'Ẹ', 'Ę', 'Í', 'O', 'Ǫ'] and syllabes[-2][1] in ['A', 'Á', 'E', 'Ẹ', 'Ę', 'O', 'Ǫ', 'U', 'Ú']:
                            changements.append('v')
                        #En milieu vélaire
                        elif syllabes[-3][-1] in ['Ọ', 'Ú'] and syllabes[-2][1] in ['A', 'E', 'U']:
                            changements.append('')
                    else:
                        if syllabes[-3][-1] in ['N', 'V']:
                            changements.append('')
                        elif syllabes[-3][-1] == 'Q' and syllabes[-2][1] == 'Ę':
                            changements.append('qu')
                        elif syllabes[-2][1] in ['Á', 'E', 'Ẹ', 'Ę', 'I', 'Í']:
                            changements.append('gu')
                        else:
                            changements.append('g')

            #Gestion de X (Probablement inexistant en cette position)
            elif syllabes[-2][0] == 'X':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][0])
                else:
                    if syllabes[-3][-1] in ['A', 'E'] and syllabes[-2][1] in ['Á', 'A']:
                        changements.append('ss')
                    else:
                        changements.append(syllabes[-2][0])

            #Gestion de Y
            elif syllabes[-2][0] == 'Y':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][1])
                else:
                    if syllabes[-3][-1] == 'S':
                        changements.append('')
                    elif syllabes[-3] == 'TR' and syllabes[-2][1] == 'Á':
                        changements.append('i')
                    elif syllabes[-3][-1] == 'M':
                        if syllabes[-2][1] == 'Á':
                            changements.append('g')
                        else:
                            changements.append('j')
                    elif syllabes[-3][-1] == 'N':
                        changements.append('')
                    elif syllabes[-3][-1] == 'E' and syllabes[-2][1] == 'Á':
                        changements.append('ii')
                    elif syllabes[-3][-1] == 'G' and syllabes[-2][1] == 'Á':
                        changements.append('gi')
                    elif syllabes[-3][-1] == 'V' and syllabes[-2][1] == 'Á':
                        changements.append('g')
                    elif syllabes[-3][-1] == 'Q' and syllabes[-2][1] == 'Á':
                        changements.append('ci')
                    elif syllabes[-3][-1] == 'Y':
                        changements.append('')
                    else:
                        changements.append('j')

            #Gestion de Z (Probablement inexistant en cette position)
            elif syllabes[-2][0] == 'Z':
                if syllabes[-2][1] in listes_lettres['consonnes_et_semi_consonnes']:
                    changements.append(syllabes[-2][0])
                else:
                    changements.append(syllabes[-2][0])

        #Vocalisme atone
        #A
        if 'A' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                changements.append('e')
            #Si A se trouve en position ouvert
            elif syllabes[-2][-1] == 'A':
                if syllabes[-2][0] == ' ':
                    changements.append('a')
                elif syllabes[-1][0] + syllabes[-1][1] in ['GY', 'TR']:
                    changements.append('ai')
                else:
                    changements.append('e')
            #Si A se trouve en position pénultième
            elif syllabes[-2][-2] == 'A':
                if syllabes[-2][0] == ' ' or syllabes[-3][-1] == ' ':
                    changements.append('a')
                elif syllabes[-2][-1] + syllabes[-1][0] + syllabes[-1][1] == 'STR':
                    changements.append('ai')
                elif syllabes[-2][-1] + syllabes[-1][0] in ['LC', 'ND']:
                    changements.append('a')
                elif syllabes[-2][-1] == 'U':
                    changements.append('o')
                else:
                    changements.append('e')
            #Si se trouve en position antépénultième
            elif syllabes[-2][-3] == 'A':
                changements.append('e')
            #Tous les autres cas de figure
            else:

                changements.append('e')

        #E
        elif 'E' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                changements.append('')
            #Si E se trouve en position ouvert
            elif syllabes[-2][-1] == 'E':
                if syllabes[-3][-1] == ' ':
                    changements.append('e')
                else:
                    changements.append('')
            #Si E se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'E':
                if syllabes[-2][-1] == ' ':
                    changements.append('e')
                elif syllabes[-3][-1] == ' ':
                    changements.append('e')
                else:
                    changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-2][-3] == 'E':
                changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #I
        elif 'I' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                changements.append('')
            #Si I se trouve en position ouvert
            elif syllabes[-2][-1] == 'I':
                changements.append('')
            #Si I se trouve en position pénultième
            elif syllabes[-2][-2] == 'I':
                changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-2][-3] == 'I':
                changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #O
        elif 'O' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                changements.append('o')
            #Si O se trouve en position ouvert
            elif syllabes[-2][-1] == 'O':
                if syllabes[-3][-1] == ' ':
                    changements.append('o')
                else:
                    changements.append('')
            #Si O se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'O':
                changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-2][-3] == 'O':
                changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #U
        elif 'U' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                changements.append('')
            #Si U se trouve en position ouvert
            elif syllabes[-2][-1] == 'U':
                changements.append('')
            #Si U se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'U':
                changements.append('')
            #Si se trouve en position antépénultième
            elif syllabes[-2][-3] == 'U':
                changements.append('')
            #Tous les autres cas de figure
            else:
                changements.append('')

        #Vocalisme
        #Á tonique
        if 'Á' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                #influence des nasales
                if syllabes[-1][0] in ['M', 'N']:
                    changements.append('ai')
                elif  syllabes[-1][0] + syllabes[-1][1] in ['CW']:
                    changements.append('ui')
                #Ouverture s'il y a un A
                if syllabes[-3][-1] == syllabes[0][-1] == 'A':
                    #Fermeture due au verbe
                    if syllabes[-1] == 'RE':

                        changements.append('e')
                    else:
                        changements.append('a')
                else:

                    changements.append('e')
            #Si A tonique se trouve en position ouverte
            elif syllabes[-2][-1] == 'Á':
                if syllabes[-1] == 'MUS':
                    changements.append('o')
                #Loi de Bartsh
                elif syllabes[-2][-2] in ['C', 'X']:
                    if syllabes[-3][-1] in ['O', 'E']:
                        changements.append('e')
                    else:
                        changements.append('ie')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-3] + syllabes[-2][-2] in ['CT', 'CY', 'DY', 'BY', 'SY', 'YT', 'TY', 'GR', 'GL']:
                    changements.append('ie')
                elif syllabes[-3][-1] + syllabes[-2][0] in ['CT', 'GT', 'YT', 'DT', 'MY', 'SY', 'VY']:
                    changements.append('ie')
                elif syllabes[-1][0] + syllabes[-1][1] in ['RY']:
                    if syllabes[-3] == syllabes[0] == 'BRE':
                        changements.append('iai')
                    else:
                        changements.append('ie')
                elif syllabes[-1][0] + syllabes[-1][1] in ['CL', 'LY']:
                    changements.append('a')
                elif syllabes[-1][0] + syllabes[-1][1] == 'TY':
                    changements.append('ai')
                #influence des nasales
                elif syllabes[-1][0] in ['M', 'N']:
                    changements.append('ai')
                else:

                    changements.append('e')
            #Si A tonique se trouve au milieu de la syllabe
            elif syllabes[-2][-2] == 'Á':
                #Loi de Bartsh
                if syllabes[-2][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-3] + syllabes[-2][-2] in ['CT']:
                    changements.append('ie')
                elif syllabes[-2][-1] + syllabes[-1][0] in ['CT', 'NY']:
                    changements.append('ai')
                #Fermeture de A tonique face à un wau
                elif syllabes[-2][-1] == 'W':
                    changements.append('o')
                elif syllabes[-2][-1] + syllabes[-1][0] == 'GD':
                    changements.append('au')
                else:
                    changements.append('a')
            #Si se trouve en position antépénultième
            elif syllabes[-2][-3] == 'Á':
                #Loi de Bartsh
                if syllabes[-2][-2] in ['C', 'X']:
                    changements.append('ie')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-3] + syllabes[-2][-2] in ['CT']:
                    changements.append('ie')
                else:
                    changements.append('a')
            #Autres cas de figure, plus rare ou A tonique ne se trouve dans aucune de ces positions
            else:
                changements.append('a')

        #Ẹ fermé
        elif 'Ẹ' in syllabes[-2]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                #influence des nasales
                if syllabes[-1][0] in ['M', 'N']:
                    if syllabes[-1][1] == 'A':
                        changements.append('ei')
                    elif syllabes[-1][-1] == 'Ī':
                        changements.append('i')
                    else:

                        changements.append('e')
                #Métaphonie
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                #Anaphonie
                elif syllabes[-1][0] == 'Y':
                    changements.append('i')
                elif syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GÍ', 'GĘ', 'GE', 'GA', 'GÁ']:
                    changements.append('i')
                elif syllabes[-1][0] + syllabes[-1][1] in ['CY', 'FY', 'LY', 'TY', 'RY', 'GN']:
                    changements.append('i')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position ouverte
            elif syllabes[-2][-1] == 'Ẹ':
                #Fermeture occasionnée par le groupe PW qui suit
                if len(syllabes[-1]) > 1 and syllabes[-1][0] + syllabes[-1][1] == 'PW':
                    if syllabes[-1][-1] == 'Ī':
                        changements.append('ui')
                    else:
                        changements.append('u')
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                elif len(syllabes[-1]) > 1 and syllabes[-1][0] + syllabes[-1][1] == 'GY':
                    changements.append('e')
                elif syllabes[-2][-2] == syllabes[-2][0] == 'C':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        changements.append('i')
                    else:
                        changements.append('ei')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-3] + syllabes[-2][-2] == 'SS':
                    changements.append('ie')
                #influence des nasales
                elif syllabes[-1][0] in ['M', 'N']:
                    if syllabes[-1][1] == 'A':
                        changements.append('ei')
                    elif syllabes[-1][-1] == 'Ī':
                        changements.append('i')
                    else:

                        changements.append('e')
                #Métaphonie
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                #Anaphonie
                elif syllabes[-1][0] == 'Y':
                    changements.append('i')
                elif len(syllabes[-1]) > 1 and syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GÍ', 'GĘ', 'GA', 'GÁ']:
                    changements.append('i')
                elif len(syllabes[-1]) > 1 and syllabes[-1][0] + syllabes[-1][1] in ['CY', 'FY', 'LY', 'TY', 'RY', 'GN']:
                    changements.append('i')
                elif syllabes[-1] == 'ANT':
                    changements.append('oi')
                else:
                    changements.append('ei')
            #Si E fermé se trouve en position fermée
            elif syllabes[-2][-2] == 'Ẹ':
                #influence des nasales
                if syllabes[-2][-1] in ['M', 'N']:
                    #Contact avec un groupe consonantique dégageant un yod
                    if syllabes[-1][0] == 'C':
                        if syllabes[-1][1] in ['Y', 'U']:
                            changements.append('e')
                        else:
                            changements.append('ei')
                    elif syllabes[-1][-1] == 'Ī':
                        changements.append('i')
                    else:

                        changements.append('e')
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                #Fermeture en [i]
                #Arrondissement dû aux séquences intervocaliques CW PW
                elif len(syllabes[-2]) > 3 and syllabes[-2][-4] + syllabes[-2][-3] in ['CW', 'PW']:
                    changements.append('u')
                elif syllabes[-2][-1] + syllabes[-1][0] == 'YS':
                    changements.append('i')
                #Problème lors de la répartition des syllabes
                elif syllabes[-2][-1] + syllabes[-1][0] == 'CT':
                    changements.append('ei')
                elif syllabes[-2][-1] + syllabes[-1][0] == 'LL':
                    changements.append('e')
                elif len(syllabes[-2]) > 2 and syllabes[-2][-3] == 'C':
                    if len(syllabes[-2]) > 3 and syllabes[-2][-4] == 'T':
                        changements.append('e')
                    else:
                        changements.append('i')
                    #influence d'un I long
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                else:
                    changements.append('e')
            #Si se trouve en position antépénultième
            elif syllabes[-2][-3] == 'Ẹ':
                #Sous l'influence d'une palatale antécédente, la diphtongue ei ferme son premier élément
                if syllabes[-2][-4] == 'C':
                    changements.append('i')
                #Métaphonie
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                else:

                    changements.append('e')
            #Si E fermé se trouve en position fermée
            else:
                #Métaphonie
                if syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                else:

                    changements.append('e')

        #Ę ouvert
        elif 'Ę' in syllabes[-2]:
            #Cas ou la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                if syllabes[-1][0] + syllabes[-1][1] in ['CT', 'BY', 'SY', 'TY']:
                    changements.append('i')
                elif syllabes[-1][0] == 'X':
                    changements.append('i')
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                elif syllabes[-1][0] + syllabes[-1][1] in ['TW']:
                    changements.append('ui')
                elif syllabes[-1][0] + syllabes[-1][1] in ['CW']:
                    changements.append('iu')
                else:
                    changements.append('ie')
            #Si E ouvert se trouve en position finale
            elif syllabes[-2][-1] == 'Ę':
                #contact avec u ngroupe dégageant un yod
                if syllabes[-1][0] + syllabes[-1][1] in ['CT']:
                    changements.append('i')
                elif syllabes[-1][0] == 'X':
                    changements.append('i')
                elif syllabes[-1][0] + syllabes[-1][1] in ['TW']:
                    changements.append('ui')
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('i')
                elif syllabes[-1][0] + syllabes[-1][1] in ['CW']:
                    changements.append('iu')
                elif syllabes[-1] == 'UNT':
                    changements.append('oi')
                elif syllabes[-3][-1] == 'I' and syllabes[-1][0] == 'R':
                    changements.append('e')
                else:
                    changements.append('ie')
            #Si E ouvert se trouve en position pénultième
            elif syllabes[-2][-2] == 'Ę':
                if syllabes[-3][-1] + syllabes[-2][0] == 'PH':
                    changements.append('e')
                elif syllabes[-2][-1] + syllabes[-1][0] in ['MT', 'RT', 'PT', 'TT', 'PD']:
                    changements.append('ie')
                #Influence d'un groupe dégageant un yod
                elif syllabes[-2][-1] + syllabes[-1][0] in ['CT', 'SY', 'YC', 'YD', 'YY', 'YN', 'QW']:
                    changements.append('i')
                elif syllabes[-2][-1] + syllabes[-1][0] + syllabes[-1][1] == 'SCR':
                    changements.append('ei')
                else:
                    changements.append('e')
            #Si E ouvert se trouve en position antépénultième
            elif syllabes[-2][-3] == 'Ę':
                changements.append('e')
            #Si E ouvert se trouve en position fermée
            else:

                changements.append('e')

        #Í tonique
        elif 'Í' in syllabes[-2]:
            #Cas où la longueur syllabique est d'une lettre
            if len(syllabes[-2]) == 1:
                changements.append('i')
            #Si I tonique se trouve en position finale
            elif syllabes[-2][-1] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position pénultième
            elif syllabes[-2][-2] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position antépénultième
            elif syllabes[-2][-3] == 'Í':
                changements.append('i')
            #Si I tonique se trouve en position fermée
            else:
                changements.append('i')

        #Ọ fermé
        elif 'Ọ' in syllabes[-2]:
            if len(syllabes[-2]) == 1:
                #influence des nasales
                if syllabes[-1][0] in ['M', 'N']:
                    changements.append('o')
                #Métaphonie
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('u')
                #Anaphonie
                elif syllabes[-1][0] == 'Y':
                    changements.append('u')
                elif syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GÍ', 'GĘ', 'GE', 'GA', 'GÁ']:
                    changements.append('u')
                elif syllabes[-1][0] + syllabes[-1][1] in ['CY', 'FY', 'LY', 'TY', 'RY', 'GN']:
                    changements.append('u')
                else:
                    changements.append('ou')
            #Si O fermé se trouve en position finale
            elif syllabes[-2][-1] == 'Ọ':
                #influence des nasales
                if syllabes[-1][0] in ['M', 'N']:
                    changements.append('o')
                #Métaphonie
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('u')
                #Anaphonie
                elif syllabes[-1][0] == 'Y':
                    changements.append('u')
                elif syllabes[-1][0] + syllabes[-1][1] in ['BY', 'VY', 'DY', 'GY', 'GI', 'GÍ', 'GĘ', 'GE', 'GA', 'GÁ']:
                    changements.append('u')
                elif syllabes[-1][0] + syllabes[-1][1] in ['CY', 'FY', 'LY', 'TY', 'GN']:
                    changements.append('u')
                elif syllabes[-1][0] + syllabes[-1][1] == 'RY':
                    changements.append('oi')
                else:
                    changements.append('ou')
            #Si O fermé se trouve en position pénultième
            elif syllabes[-2][-2] == 'Ọ':
                #Métaphonie
                if syllabes[-1][-1] == 'Ī':
                    changements.append('u')
                elif syllabes[-2][-1] + syllabes[-1][0] in ['NY', 'YT']:
                    changements.append('oi')
                elif syllabes[-2][-1] + syllabes[-1][0] + syllabes[-1][1] in ['NDY', 'STY']:
                    changements.append('oi')
                else:
                    changements.append('o')
            #Si O fermé se trouve en position antépénultième
            elif syllabes[-2][-3] == 'Ọ':
                #Métaphonie
                if syllabes[-1][-1] == 'Ī':
                    changements.append('u')
                else:
                    changements.append('o')
            #Toutes les autres positions
            else:
                #Métaphonie
                if syllabes[-1][-1] == 'Ī':
                    changements.append('u')
                else:
                    changements.append('o')

        #Ǫ ouvert
        elif 'Ǫ' in syllabes[-2]:
            if len(syllabes[-2]) == 1:
                #influence des nasales
                if syllabes[-1][0] in ['M', 'N']:
                    if syllabes[-1][1] == 'O':
                        changements.append('ue')
                    else:
                        changements.append('o')
                elif syllabes[-1][0] + syllabes[-1][1] in ['CT', 'CW']:
                    changements.append('ui')
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                elif syllabes[-1][0] == 'X':
                    changements.append('ui')
                else:
                    changements.append('ue')
            #Si O ouvert se trouve en position finale
            elif syllabes[-2][-1] == 'Ǫ':
                if len(syllabes[-2]) > 2 and syllabes[-2][-3] + syllabes[-2][-2] == 'TY':
                    changements.append('io')
                elif syllabes[-1][0]  + syllabes[-1][1] == 'PY':
                    changements.append('o')
                #influence des nasales
                elif syllabes[-1][0] in ['M', 'N']:
                    changements.append('o')
                elif syllabes[-1][0] in ['X', 'CW']:
                    changements.append('ui')
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                else:
                    changements.append('ue')
            #Si O ouvert se trouve en position pénultième
            elif syllabes[-2][-2] == 'Ǫ':
                #Présence d'un groupe consonantique dégageant un yod
                if syllabes[-2][-1] + syllabes[-1][0] in ['CT', 'YY']:
                    changements.append('ui')
                elif syllabes[-2][-1] + syllabes[-1][0] in ['YN']:
                    changements.append('oi')
                else:
                    changements.append('o')
            #Si O ouvert se trouve en position antépénultième
            elif syllabes[-2][-3] == 'Ǫ':
                if syllabes[-2][-2] + syllabes[-2][-1] == 'YS':
                    changements.append('ui')
                else:
                    changements.append('o')
            #Toutes les autres positions
            else:
                changements.append('o')

        #Ú tonique
        elif 'Ú' in syllabes[-2]:
            if len(syllabes[-2]) == 1:
                changements.append('u')
            #Si U tonique se trouve en position finale
            elif syllabes[-2][-1] == 'Ú':
                if syllabes[-1] == 'NU':
                    changements.append('o')
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('ui')
                else:
                    changements.append('u')
            #SiU tonique se trouve en position pénultième
            elif syllabes[-2][-2] == 'Ú':
                if syllabes[-2][-1] + syllabes[-1][-0] == 'SY':
                    changements.append('ui')
                else:
                    changements.append('u')
            #Si U tonique se trouve en position antépénultième
            elif syllabes[-2][-3] == 'Ú':
                changements.append('u')
            #Toutes les autres positions
            else:
                changements.append('u')

        #Consonantisme final
        if syllabes[-2][-1] in listes_lettres['consonnes_et_semi_consonnes']:

            #Gestion de B
            if syllabes[-2][-1] == 'B':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de C
            elif syllabes[-2][-1] == 'C':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de D
            elif syllabes[-2][-1] == 'D':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de F
            elif syllabes[-2][-1] == 'F':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de G
            elif syllabes[-2][-1] == 'G':
                #Assimilation au N suivant
                if syllabes[-2][0] == 'N':
                    if syllabes[-2] == syllabes[-1]:
                        changements.append('')
                    else:
                        changements.append('g')
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de H (ne devrait pas exister ou cas très très rare)
            elif syllabes[-2][-1] == 'H':
                changements.append('')

            #Gestion de L
            elif syllabes[-2][-1] == 'L':
                if syllabes[-1][0] == 'L':
                    if syllabes[-2][-2] in ['Ẹ'] and syllabes[-1][1] in ['A']:
                        changements.append('l')
                    else:
                        changements.append('')
                elif syllabes[-1][0] + syllabes[-1][1] == 'GR':
                    changements.append('l')
                else:
                    #La liquide se vocalise en [w]
                    changements.append('u')

            #Gestion de M
            elif syllabes[-2][-1] == 'M':
                if syllabes[-1][0] in ['C', 'T', 'Y']:
                    if syllabes[-2][-2] == 'Í' and syllabes[-1] == 'YU':
                        changements.append('ng')
                    else:
                        changements.append('n')
                elif syllabes[-1][0] + syllabes[-1][1] == 'BY':
                    changements.append('n')
                elif syllabes[-1][0] == 'M':
                    changements.append('')
                else:
                    #Assimilation à la consonne suivante
                    changements.append('m')

            #Gestion de N
            elif syllabes[-2][-1] == 'N':
                if syllabes[-1][0] == 'Y':
                    changements.append('gn')
                elif syllabes[-1][0] + syllabes[-1][1] == 'DY':
                    changements.append('gn')
                elif syllabes[-1][0] == 'N':
                    if syllabes[-2][-2] == 'Ǫ' and syllabes[-1][1] == 'A':
                        changements.append('n')
                    else:
                        changements.append('')
                else:
                    changements.append('n')

            #Gestion de P
            elif syllabes[-2][-1] == 'P':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Q
            elif syllabes[-2][-1] == 'Q':
                if syllabes[-1][0] == 'W':
                    if syllabes[-2][-2] in ['Í'] and syllabes[-1][1] in ['A']:
                        changements.append('v')
                    elif syllabes[-2][-2] in ['Í'] and syllabes[-1][1] == 'U':
                        changements.append('f')
                    else:
                        changements.append('qu')
                else:
                    changements.append('')

            #Gestion de R
            elif syllabes[-2][-1] == 'R':
                if syllabes[-1][0] == 'R':
                    if syllabes[-2][-2] == 'Ę' and syllabes[-1][1] == 'A':
                        changements.append('r')
                    else:
                        changements.append('')
                elif syllabes[-2] in ['FR', 'TR']:
                    changements.append('')
                else:
                    #La vibrante est très stable
                    changements.append(syllabes[-2][-1])


            #Gestion de S
            elif syllabes[-2][-1] == 'S':
                if syllabes[-1][0] == 'S':
                    if syllabes[-2][-2] in ['A'] and syllabes[-1][1]  in ['A', 'Ę']:
                        changements.append('s')
                    else:
                        changements.append('')
                else:
                    changements.append('s')

            #Gestion de T
            elif syllabes[-2][-1] == 'T':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de V
            elif syllabes[-2][-1] == 'V':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de W
            elif syllabes[-2][-1] == 'W':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de X
            elif syllabes[-2][-1] == 'X':
                changements.append('s')

            #Gestion de Y
            elif syllabes[-2][-1] == 'Y':
                #Assimilation à la consonne suivante
                changements.append('')

            #Gestion de Z
            elif syllabes[-2][-1] == 'Z':
                #Assimilation à la consonne suivante
                changements.append('')

        return changements
