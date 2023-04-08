# EasyCrypt

Проект предлагает шифрование при помощи шифров Цезаря, Виженера и Вернама, их взлома, а также реализует стеганографию в картинках.

Функционал:
-- Шифрование и дешифрование файлов шифрами Цезаря, Виженера и Вернама.
-- Автоматический взлом шифра Цезаря методами частотного анализа, а также при помощи пакета ```enchant``` (морфологический анализ адекватности текста).
-- Стеганография: внедрение и извлечение текста в/из картинки формата bmp/png/jpg/etc, используя по 2 бита каждого пикселя.
-- Графический интерфейс.
-- Скрипт для работы из консоли.

Проект покрыт базовыми тестами, все функции задокументированы.

Для корректной работы сначала установите все зависимости: ```pip -r requirements.txt```

Далее предполагается, что вы находитесь в корне проекта.
-- Запуск графического приложения: ```python3 app.py```
-- Запуск консольного скрипта: ```python3 console.py --help```
Например: ```python3 console.py --mode=cipher --text="100 13 15 0 27 13 69 34 84 89 11 6 30 72 86 83" --lang=en --op=Decode --cipher=Vernam```
```python3 console.py --mode=steganography --op=Decode --input_path=images/test_images/lk_enc.png```

Иерархия проекта такова:
-- ```images``` - изображения для тестов и фона приложения.
-- ```test_project.py``` - Unit-тесты внутренностей проекта.
-- ```app.py``` - графическое приложение.
-- ```ciphers.py``` - реализация шифров.
-- ```steganography.py``` - реализация стеганографии.
-- ```constants.py``` - константы проекта (словари и языки, размер окна клиента и так далее).
-- ```requirements.txt``` - зависимости проекта.
-- ```console.py``` - консольный клиент.
