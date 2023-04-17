import unittest
from ciphers import *
from steganography import *


class TestAppApi(unittest.TestCase):
    def test_vernam(self):
        a = Vernam.encode('ALLSWELLTHATENDSWELL', 'EVTIQWXQVVOPMCXREPYZ')
        self.assertTrue(
            a == "4 26 24 26 6 18 20 29 2 30 14 4 8 13 28 1 18 21 21 22")
        self.assertTrue('ALLSWELLTHATENDSWELL' ==
                        Vernam.decode(a, 'EVTIQWXQVVOPMCXREPYZ'))

    def test_vinegere(self):
        a = Vigenere.encode('ATTACKATDAWN', 'en', 'LEMON')
        self.assertTrue(a == 'LXFOPVEFRNHR')
        self.assertTrue(Vigenere.decode(
            a, 'en', key='lemon') == 'ATTACKATDAWN')

    def test_caesar(self):
        text = '''Возвратившись со смотра, Кутузов,
        сопутствуемый австрийским генералом, прошел в свой кабинет и, кликнув адъютанта,
        приказал подать себе некоторые бумаги, относившиеся до состояния приходивших войск,
        и письма, полученные от эрцгерцога Фердинанда, начальствовавшего передовою армией.
        Князь Андрей Болконский с требуемыми бумагами вошел в кабинет главнокомандующего.
        Перед разложенным на столе планом сидели Кутузов и австрийский член гофкригсрата.'''
        enc_text = Caesar.encode(text, rotate=10)
        self.assertTrue(Caesar.crack_by_frequency(
            enc_text, c_count=5) == text)
        self.assertTrue(Caesar.crack_by_enchant(enc_text, 'ru') == text)

    def test_steganography(self):
        Steganography.insert_text(
            'images/test_images/lk.png', 'I like Python!',
            'images/test_images/lk_enc.png')
        Steganography.insert_text(
            'images/test_images/lk.jpg', 'I like Python!',
            'images/test_images/lk_enc_jpg.png')
        # We couldn't use jpg for Steganography so easy here because
        # it uses complex compress algorithm and some data may be corrupted.
        Steganography.insert_text(
            'images/test_images/lk.bmp', 'I like Python!',
            'images/test_images/lk_enc.bmp')
        self.assertTrue(Steganography.read_text(
            'images/test_images/lk_enc.png') == 'I like Python!'
            == Steganography.read_text('images/test_images/lk_enc_jpg.png')
            == Steganography.read_text('images/test_images/lk_enc.bmp'))


if __name__ == '__main__':
    unittest.main()
