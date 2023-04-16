import sys

from src.constants import help_message, OPERATIONS, LANGUAGES, CIPHERS
from src.ciphers import *
from src.steganography import *

from main import App

args_ = sys.argv[1:]

if not args_ or '--help' in args_:
    print(help_message)
    exit()

args = {'lang': 'ru'}

for arg in args_:
    key, value = arg.split('=')
    args[key[2:]] = value

if 'mode' not in args:
    print('Error: mode not passed.')
    exit()

if args['mode'] == 'cipher':
    if 'text' not in args and 'file' not in args:
        print('Error: no input given.')
        exit()
    if 'text' in args:
        text = args['text']
    else:
        with open(args['file'], 'r', encoding='utf-8') as f:
            text = f.read()
    op = args.get('op')
    key = args.get('key')
    if op not in OPERATIONS:
        print('Wrong operation chosen!')
        exit()
    if args['lang'] not in LANGUAGES:
        print('Wrong language chosen!')
        exit()
    lang = args['lang']
    cip = args.get('cipher')
    if cip not in CIPHERS:
        print('Wrong cipher chosen!')
        exit()
    if op == 'Encode':
        if cip == 'Caesar':
            mes = Caesar.encode(text, lang, int(key))
        else:
            if not key:
                print('No key passed!')
                exit()
            if cip == 'Vigenere':
                mes = Vigenere.encode(text, lang, key)
            elif cip == 'Vernam':
                mes = Vernam.encode(text, key)
    else:
        if cip == 'Caesar':
            if 'use_cracker' in args and args['use_cracker'] == 'true' or not key:
                mes = App.crack_caesar(text, lang)
            else:
                mes = Caesar.decode(text, lang, int(key))
        else:
            if not key:
                raise ValueError('No key passed!')
            if cip == 'Vigenere':
                mes = Vigenere.decode(text, lang, key)
            elif cip == 'Vernam':
                mes = Vernam.decode(text, key)
    print(mes)
else:
    in_path = args.get('input_path')
    out_path = args.get('output_path')
    op = args.get('op')
    if op not in OPERATIONS:
        print('Wrong operation chosen!')
        exit()
    if op == 'Encode':
        if 'text' not in args and 'file' not in args:
            print('Error: no input given.')
            exit()
        if 'text' in args:
            text = args['text']
        else:
            with open(args['file'], 'r', encoding='utf-8') as f:
                text = f.read()
        if not in_path or not out_path:
            print('output_path or input_path not passed!')
            exit()
        mes = 'Successfully inserted!'
        Steganography.insert_text(in_path, text, out_path)
    else:
        if not in_path:
            print('input_path not passed!')
            exit()
        mes = Steganography.read_text(in_path)
    print(mes)
