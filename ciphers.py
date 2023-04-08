from collections import Counter
import enchant

from constants import *


class Caesar:
    @staticmethod
    def __shift_symbol(symbol: str, lang: str = 'ru', rotate: int = 0) -> str:
        '''Correctly shifts given symbol in given lang.'''
        if lang == 'ru' and symbol.lower() in RU_ALP:
            res = RU_ALP[(RU_IND[symbol.lower()] + rotate) % RU_LEN]
        elif lang == 'en' and symbol.lower() in EN_ALP:
            res = EN_ALP[(EN_IND[symbol.lower()] + rotate) % EN_LEN]
        else:
            res = symbol
        if symbol.isupper():
            res = res.upper()
        return res

    @staticmethod
    def __rotate(text: str = "", lang: str = 'ru', rotate: int = 0) -> str:
        '''Rotates given text by Caesar cipher; rotate can be any integer number.'''
        return "".join(Caesar.__shift_symbol(i, lang, rotate) for i in text)

    @staticmethod
    def encode(text: str = "", lang: str = 'ru', rotate: int = 0) -> str:
        return "".join(Caesar.__shift_symbol(i, lang, rotate) for i in text)

    @staticmethod
    def decode(text: str = "", lang: str = 'ru', rotate: int = 0) -> str:
        return "".join(Caesar.__shift_symbol(i, lang, -rotate) for i in text)

    @staticmethod
    def crack_by_frequency(text: str = "", lang: str = 'ru', common_count: int = 5) -> str:
        '''Decodes the text with the most probable rotate (using [common_count] symbols' rotates).'''
        if not 1 <= common_count <= 5:
            raise ValueError('common_count not in [1, 5]!')
        if lang == 'ru':
            top_5 = [i[0] for i in sorted(Counter(i for i in text.lower() if i in RU_ALP).items(
            ), key=lambda x: x[-1], reverse=True)[:common_count]]
            rotate = Counter((RU_IND[top_5[i]] - RU_IND[RU_TOP[i]]) %
                             RU_LEN for i in range(min(common_count, len(top_5)))).most_common(1)[0][0]
        elif lang == 'en':
            top_5 = [i[0] for i in sorted(Counter(i for i in text.lower() if i in EN_ALP).items(
            ), key=lambda x: x[-1], reverse=True)[:common_count]]
            rotate = Counter((EN_IND[top_5[i]] - EN_IND[EN_TOP[i]]) %
                             EN_LEN for i in range(min(common_count, len(top_5)))).most_common(1)[0][0]
        else:
            raise ValueError('Unknown language passed!')
        return Caesar.__rotate(text, lang=lang, rotate=-rotate)

    @staticmethod
    def crack_by_enchant(text: str = "", lang='ru') -> str:
        '''Decodes the text with the enchant morth analizer.'''
        if lang == 'ru':
            enc_dict = 'ru'
        else:
            enc_dict = 'en_US'
        checker = enchant.Dict(enc_dict)
        score, result = -1, text
        for i in range(max(EN_LEN, RU_LEN)):
            decoded = Caesar.decode(text, lang, i)
            s = sum([checker.check(j) for j in decoded.split()])
            if s > score:
                score, result = s, decoded
        return result


class Vigenere:
    @staticmethod
    def check_key(key: str, lang: str) -> None:
        '''Checks key correctness.'''
        if (lang == 'ru' and not all(i.lower() in RU_ALP for i in key)) or (lang == 'en' and not all(i.lower() in EN_ALP for i in key)):
            raise ValueError(f'Wrong key language (expected: {lang}).')

    @staticmethod
    def encode(text: str = "", lang: str = 'ru', key: str = "") -> str:
        output = ""
        Vigenere.check_key(key, lang)
        first_ord = ord('а') if lang == 'ru' else ord('a')
        for i in range(len(text)):
            output += Caesar.encode(text[i], lang=lang, rotate=ord(
                key[i % len(key)].lower()) - first_ord)
        return output

    @staticmethod
    def decode(text: str = "", lang: str = 'ru', key: str = "") -> str:
        output = ""
        Vigenere.check_key(key, lang)
        first_ord = ord('а') if lang == 'ru' else ord('a')
        for i in range(len(text)):
            output += Caesar.decode(text[i], lang=lang, rotate=ord(
                key[i % len(key)]) - first_ord)
        return output


class Vernam:
    @staticmethod
    def encode(text: str = "", key: str = "") -> str:
        output = []
        for i in range(len(text)):
            output.append(ord(text[i]) ^ ord(key[i % len(key)]))
        return ' '.join(map(str, output))

    @staticmethod
    def decode(text: str = "", key: str = "") -> str:
        output = ''
        i = 0
        for s in text.strip().split():
            try:
                num = int(s)
            except:
                raise ValueError('Input in not a sequence of integers!')
            output += chr(num ^ ord(key[i % len(key)]))
            i += 1
        return output
