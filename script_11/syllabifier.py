"""
Sépare un terme écrit en latin vulgaire en une liste de ses syllabes.
Le travail a été inspiré du travail de Luke Hollis.
"""

__author__ = ['Luke Hollis <lukehollis@gmail.com>']
__license__ = 'MIT License. See LICENSE.'


import re



#Liste non exhaustive des lettres latines
LATIN = {
        #Diphtongues
        'diphthongs': ["AE", "OE", "AU"],

        #Voyelles avec les signes diacritiques ouvert/fermé
         'vowels': [
             "Í", "I", "Ī", "Ę", "Ẹ", "A", "Ọ", "Ǫ", "U", "Ú", "A", "E", "O", "Á",],

         #Yod et Wau
         'yod_et_wau' : ['Y', 'W'],

        #Consonnnes sourdes
         'mute_consonants_and_f': ["P", "B", "T", "D", "C", "G", "F",
         # 'W', 'Y'
         ],

         #Consonnes Liquides
         'liquid_consonants': ["R", "L",
         # 'W', 'Y'
         ],


         #N
         'nasale' : 'N'
         }


class Syllabifier(object):
    """
    Découpe un mot en ses syllabes
    """

    def __init__(self, language=LATIN):
        """
        Initialise le programme et importe la liste des lettres latines
        """

        self.language = language

        return

    def _is_consonant(self, char):
        #Vérifie si le caractère est dans la liste des voyelles
        return not char in self.language['vowels']

    def _is_vowel(self, char):
        #Vérifie si le caractère est dans la liste des voyelles
        return char in self.language['vowels']

    def _is_diphthong(self, char_1, char_2):
        #Vérifie si deux caractères à la suite forment une diphtongue
        return char_1 + char_2 in self.language['diphthongs']

    def _is_mute_consonant_or_f(self, char):
        #Vérifie si le caractère est une consonne sourde
        return char in self.language['mute_consonants_and_f']

    def _is_liquid_consonant(self, char):
        #Vérifie si le caractère est une consonnne liquide
        return char in self.language['liquid_consonants']

    def _is_yod_and_wau(self, char):
        return char in self.language['yod_et_wau']

    def _is_N(self, char):
        return char in self.language['nasale']

    def syllabify(self, word):
        """
        Découpe le mot latin en une liste de syllabes,
        selon les lettre téléchargées depuis LATIN_VULGAIRE.
        """

        syllables = []

        #Construction d'une syllabe vide
        syllable = ''

        #On cherche la longueur d'un mot pour determiner la place de chaque caractère
        word_len = len(word)

        # Iterate over characters to build syllables
        for i, char in enumerate(word):

            # Build syllable
            syllable = syllable + char
            syllable_complete = False

            # Checks to process syllable logic
            char_is_vowel = self._is_vowel(char)
            has_next_char = i < word_len - 1
            has_prev_char = i > 0

            # If it's the end of the word, the syllable is complete
            if not has_next_char:
                syllable_complete = True

            else:
                next_char = word[i + 1]
                if has_prev_char:
                    prev_char = word[i - 1]

                # 'i' is a special case for a vowel. when i is at the
                # beginning of the word (Iesu) or i is between
                # vowels (alleluia), then the i is treated as a
                # consonant (y) Note: what about compounds like 'adiungere'
                if char == 'Y' and has_next_char and self._is_vowel(next_char):
                    if i == 0:
                        char_is_vowel = False
                    elif self._is_vowel(prev_char):
                        char_is_vowel = False

                # Determine if the syllable is complete
                if char_is_vowel:

                    if ((  # If the next character's a vowel
                            self._is_vowel(next_char)
                                   # And it doesn't compose a dipthong with the current character
                                   and not self._is_diphthong(char, next_char)
                                   # And the current character isn't preceded by a q, unless followed by a u
                                   and not (has_prev_char and prev_char in ["C", "Q", 'K'] and char in ['U', 'W'] and next_char not in ['U', 'W']))
                            or (
                                    # If the next character's a consonant but not a double consonant, unless it's a mute consonant followed by a liquid consonant
                                    i < word_len - 2 and (((has_prev_char and prev_char not in ["Q", 'K'] and char in ['U', 'Ú', 'W'] and self._is_vowel(word[i + 2]))
                                                or (not has_prev_char and char in ['U', 'Ú', 'W'] and self._is_vowel(word[i + 2])))
                                                or (char not in ['U', 'Ú', 'W'] and self._is_vowel(word[i + 2]) and not self._is_diphthong(char, next_char))
                                                # or (self._is_mute_consonant_or_f(next_char) and self._is_liquid_consonant(word[i + 2]))
                                                #Cette ligne permet d'avoir des séquences complexes avec une semi-consonne en troisième position
                                                or (self._is_mute_consonant_or_f(next_char) and self._is_liquid_consonant(word[i + 2]) and self._is_yod_and_wau(word[i+3]))
                                                or (self._is_mute_consonant_or_f(next_char) and (self._is_liquid_consonant(word[i + 2]) or self._is_yod_and_wau(word[i+2])))
                                                # or (self._is_mute_consonant_or_f(next_char) and self._is_liquid_consonant(word[i + 2]))))
                                                # or (self._is_mute_consonant_or_f(next_char) and (self._is_liquid_consonant(word[i + 2]) or self._is_yod_and_wau))))
                                                or (self._is_liquid_consonant(next_char) and self._is_yod_and_wau(word[i+2]))
                                                or (self._is_mute_consonant_or_f(next_char) and self._is_N(word[i+2]))
                                                )
                            )
                    ):
                        syllable_complete = True

                # Otherwise, it's a consonant
                else:
                    if (  # If the next character's also a consonant (but it's not the last in the word)
                          ( not self._is_vowel(next_char) and i < word_len - 2)
                          # If the char's not a mute consonant followed by a liquid consonant
                          # and not (self._is_mute_consonant_or_f(char) and (self._is_liquid_consonant(next_char) or self._is_yod_and_wau(next_char)))
                          and not (self._is_mute_consonant_or_f(char) and (self._is_liquid_consonant(next_char)))
                          # If the char's not a c, p, or t followed by an h
                          and not (
                                (has_prev_char and not self._is_vowel(prev_char)
                                and char in ['C', 'P', 'T']
                                and next_char in ['H', 'W']) or (not has_prev_char and char in ['C', 'P', 'T']
                                and next_char in ['H', 'W'])
                                )
                        # And it's not the only letter in the syllable
                          and not len(syllable) == 1):

                        syllable_complete = True

            # If it's a complete syllable, append it to syllables list and reset syllable
            if syllable_complete:
                syllables.append(syllable)
                syllable = ''

        return syllables
