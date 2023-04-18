RU_ALP = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
RU_IND = {RU_ALP[i]: i for i in range(len(RU_ALP))}
RU_LEN = len(RU_ALP)
RU_TOP = ['о', 'е', 'а', 'и', 'н']

EN_ALP = 'abcdefghijklmnopqrstuvwxyz'
EN_IND = {EN_ALP[i]: i for i in range(len(EN_ALP))}
EN_LEN = len(EN_ALP)
EN_TOP = ['e', 't', 'a', 'o', 'i']

assert (RU_LEN == 33)
assert (EN_LEN == 26)


DEFAULT_W_SIZE = "800x800"
WINDOW_TITLE = 'EasyCrypt — simple app for ciphers/steganography.'
LANGUAGES = ['ru', 'en']
CIPHERS = ['Caesar', 'Vigenere', 'Vernam']
OPERATIONS = ["Encode", 'Decode']

help_message = '''Usage: python3 console.py --arg=value

Possible args:
- mode: cipher / steganography - working mode.
- cipher: Caesar / Vigenere / Vernam - cipher to use.
- key: str - key or rotation for the cipher.
- op: decode / encode - operation to process.
- text: str - input text.
- lang: ru / en - language to use, default - ru.
- file [optional]: path - read input text from file.
- use_cracker: true / false - use automatic Caesar cracking functions.
- input_path: path - input image path.
- output_path: path - output image path.
'''

NO_ROTATE_MESSAGE = 'No roration passed, do you want to try auto cracking ways?'