import string 


ENGLISH_ALPHABET = string.ascii_uppercase
RUSSIAN_ALPHABET = 'ё' + ''.join(
    chr(letter_index)
    for letter_index in range(ord('а'), ord('я') + 1)
)

HJKL = {
    "UP": 'k',
    "DOWN": 'j',
    "LEFT": 'h',
    "RIGHT": 'l'
}
