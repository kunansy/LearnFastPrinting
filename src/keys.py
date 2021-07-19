ENGLISH_UP_KEYS = {
    "Q": 'q',
    "W": 'w',
    "E": 'e',
    "R": 'r',
    "T": 't',
    "Y": 'y',
    "U": 'u',
    "I": 'i',
    "O": 'o',
    "P": 'p'
}
ENGLISH_MIDDLE_KEYS = {
    "A": 'a',
    "S": 's',
    "D": 'd',
    "F": 'f',
    "G": 'g',
    "H": 'h',
    "J": 'j',
    "K": 'k',
    "L": 'l'
}
ENGLISH_DOWN_KEYS = {
    "Z": 'z',
    "X": 'x',
    "C": 'c',
    "V": 'v',
    "B": 'b',
    "N": 'n',
    "M": 'm'
}
ENGLISH_ALPHABET = {
    **ENGLISH_UP_KEYS,
    **ENGLISH_MIDDLE_KEYS,
    **ENGLISH_DOWN_KEYS
}
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
