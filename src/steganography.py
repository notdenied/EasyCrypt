from PIL import Image


class Steganography:
    @staticmethod
    def insert_text(path: str, text: str, output_path: str) -> None:
        '''Inserts given text using two first bytes of each color.
        Asserts (any) of formats with >= 2 bytes for one pixel.'''
        img = Image.open(path)
        obj = img.load()
        w, h = img.size
        br = False
        text_b = []
        for i in bytes(text, encoding='utf-8'):
            text_b.append((i & (2**8 - 1 - (2**6 - 1))) >> 6)
            text_b.append((i & (2**6 - 1 - (2**4 - 1))) >> 4)
            text_b.append((i & (2**4 - 1 - (2**2 - 1))) >> 2)
            text_b.append(i & (2**2 - 1))

        if w * h < len(text_b) + 1:
            raise ValueError("Image is too small for this text!")

        i = 0
        for x in range(w):
            if br:
                break
            for y in range(h):
                data = list(obj[x, y])
                if i == len(text_b):
                    data[1] -= data[1] % 2
                    obj[x, y] = tuple(data)
                    br = True
                    break
                if data[1] > 0:
                    data[1] -= (data[1] + 1) % 2
                else:
                    data[1] = 1
                data[0] &= 2**8 - 1 - (2 ** 2 - 1)
                data[0] |= text_b[i]
                obj[x, y] = tuple(data)
                i += 1
        if output_path.endswith('.jpg'):
            output_path = output_path.rsplit('.', 1)[0] + '.png'
        img.save(output_path, subsampling='keep', quality='keep')

    @staticmethod
    def read_text(path: str) -> str:
        '''Extracts text from the picture.'''
        img = Image.open(path)
        obj = img.load()
        w, h = img.size
        br = False
        text_b = []
        for x in range(w):
            if br:
                break
            for y in range(h):
                data = obj[x, y]
                if data[1] % 2 == 0:
                    br = True
                    break
                text_b.append(data[0] & (2**2 - 1))
        codes = []
        for i in range(0, len(text_b), 4):
            codes.append((text_b[i] << 6) + (text_b[i+1] <<
                         4) + (text_b[i+2] << 2) + text_b[i+3])
        return ''.join(i.to_bytes(length=1, byteorder='big', signed=False)
                       .decode('utf-8') for i in codes)
