def printifier():

    import re
    import collections

    from Moine_dict import dict
    keys = dict.keys()
    values = dict.values()

    prints_Marie = open('prints.py', 'w', encoding = 'utf-8')

    for key in keys:
        prints_Marie.write('print(EvolutionPhonetique.evolution_phonetique("' + key + '")) # '+ dict[key] + '\n')

printifier()
