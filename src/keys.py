ENGLISH_UP_KEYS = "qwertyuiop"
ENGLISH_MIDDLE_KEYS = "asdfghjkl"
ENGLISH_DOWN_KEYS = "zxcvbnm"
ENGLISH_ALPHABET = f"{ENGLISH_UP_KEYS}" \
                   f"{ENGLISH_MIDDLE_KEYS}" \
                   f"{ENGLISH_DOWN_KEYS}"
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
