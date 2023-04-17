import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd

from constants import DEFAULT_W_SIZE, WINDOW_TITLE, LANGUAGES, \
    CIPHERS, OPERATIONS, NO_ROTATE_MESSAGE
from ciphers import Caesar, Vernam, Vigenere
from steganography import Steganography


class App(tk.Tk):
    def __init__(self):
        """Main app class."""
        super().__init__()

        self.run_style = ttk.Style()
        self.run_style.theme_use('alt')
        self.run_style.configure('TButton', background='red', foreground='white',
                                 width=20, borderwidth=1, focusthickness=3,
                                 focuscolor='none')
        self.run_style.map('TButton', background=[('active', 'red')])

        self.title(WINDOW_TITLE)
        self.geometry(DEFAULT_W_SIZE)

        self.notebook = ttk.Notebook()
        self.notebook.pack(expand=True, fill=BOTH)

        self.main_frame = ttk.Frame(self.notebook)
        self.bg = PhotoImage(
            file="images/background.png")
        self.bg_label = Label(self.main_frame, image=self.bg)
        self.bg_label.place(x=-1, y=-1, )

        self.input_label = ttk.Label(
            self.main_frame, text='Enter your text:', font='Arial 24')
        self.input_label.pack()

        self.input = Text(self.main_frame, width=85, height=13)
        self.input.insert(END, "")
        self.input.pack()

        self.input_button = ttk.Button(self.main_frame, text='Paste from file')
        self.input_button['command'] = self.insert_from_file
        self.input_button.pack()

        self.dummy_label2 = ttk.Label(self.main_frame)
        self.dummy_label2.pack()

        self.settings_frame = Frame(self.main_frame)

        self.lang_label = ttk.Label(
            self.settings_frame, padding=10, text='Language:', font='Arial 12')
        self.lang_label.pack(side=LEFT)
        self.language = StringVar(value=LANGUAGES[0])
        self.lang_combobox = ttk.Combobox(
            self.settings_frame, textvariable=self.language, values=LANGUAGES)
        self.lang_combobox.pack(side=LEFT)

        self.cipher_label = ttk.Label(
            self.settings_frame, padding=10, text='Cipher:', font='Arial 12')
        self.cipher_label.pack(side=LEFT)
        self.cipher = StringVar(value=CIPHERS[0])
        self.cipher_combobox = ttk.Combobox(
            self.settings_frame, textvariable=self.cipher, values=CIPHERS)
        self.cipher_combobox.pack(side=LEFT)

        self.op_label = ttk.Label(
            self.settings_frame, padding=10, text='Operation:', font='Arial 12')
        self.op_label.pack(side=LEFT)
        self.op = StringVar(value=OPERATIONS[0])
        self.op_combobox = ttk.Combobox(
            self.settings_frame, textvariable=self.op, values=OPERATIONS)
        self.op_combobox.pack(side=LEFT)

        self.settings_frame.pack()

        self.key_frame = ttk.Frame(self.main_frame)
        self.key_label = ttk.Label(
            self.key_frame, text='Key/rotation:', font='Arial 12')
        self.key_label.pack(side=LEFT)

        self.key = Text(self.key_frame, width=30, height=1)
        self.key.insert(END, "")
        self.key.pack(side=LEFT)

        self.key_frame.pack()

        self.run_button = ttk.Button(
            self.main_frame, text='Run!', width=10)
        self.run_button['command'] = self.run_operation
        self.run_button.pack()

        self.dummy_label = ttk.Label(self.main_frame)
        self.dummy_label.pack()

        self.output_label = ttk.Label(
            self.main_frame, text='Output:', font='Arial 24')
        self.output_label.pack()

        self.output = Text(self.main_frame, width=85, height=13)
        self.output.insert(END, "")
        self.output.pack()

        self.second_frame = ttk.Frame(self.notebook)

        self.bg2 = PhotoImage(
            file="images/background 2.png")
        self.bg_label2 = Label(self.second_frame, image=self.bg2)
        self.bg_label2.place(x=-1, y=-1, )

        self.input_label2 = ttk.Label(
            self.second_frame, text='Enter your text:', font='Arial 24')
        self.input_label2.pack()

        self.input2 = Text(self.second_frame, width=85, height=11)
        self.input2.insert(END, "")
        self.input2.pack()

        self.dummy_label = ttk.Label(self.second_frame)
        self.dummy_label.pack()

        self.choose_input_path = ttk.Button(
            self.second_frame, text='Choose input image path:', padding=10, width=30)
        self.choose_input_path['command'] = self.input_picture_path
        self.choose_input_path.pack()

        self.input_path = Text(self.second_frame, width=90, height=1)
        self.input_path.insert(END, "")
        self.input_path.pack()

        self.dummy_label = ttk.Label(self.second_frame)
        self.dummy_label.pack()

        self.op_frame = ttk.Frame(self.second_frame)
        self.op_label2 = ttk.Label(
            self.op_frame, padding=10, text='Operation:', font='Arial 12')
        self.op_label2.pack(side=LEFT)
        self.op2 = StringVar(value=OPERATIONS[0])
        self.op_combobox2 = ttk.Combobox(
            self.op_frame, textvariable=self.op2, values=OPERATIONS)
        self.op_combobox2.pack(side=LEFT)

        self.run_button2 = ttk.Button(
            self.op_frame, text='Run!', width=10, )
        self.run_button2['command'] = self.run_operation2
        self.run_button2.pack(side=LEFT)

        self.op_frame.pack()

        self.choose_output_path = ttk.Button(
            self.second_frame, text='Choose output image path:', padding=10, width=30)
        self.choose_output_path['command'] = self.input_output_path
        self.choose_output_path.pack()

        self.output_path = Text(self.second_frame, width=90, height=1)
        self.output_path.insert(END, "")
        self.output_path.pack()

        self.dummy_label = ttk.Label(self.second_frame)
        self.dummy_label.pack()

        self.output_label2 = ttk.Label(
            self.second_frame, text='Output:', font='Arial 24')
        self.output_label2.pack()

        self.output2 = Text(self.second_frame, width=85, height=11)
        self.output2.insert(END, "")
        self.output2.pack()

        self.notebook.add(self.main_frame, text="Ciphers")
        self.notebook.add(self.second_frame, text="Steganography")

    def insert_from_file(self):
        """Inserts text to the first frame from file."""
        name = fd.askopenfilename()
        if not name:
            return
        with open(name, 'r', encoding='utf-8') as f:
            data = f.read()
        self.input.delete("1.0", "end")
        self.input.insert(END, data)

    def input_picture_path(self):
        """Inserts input picture path to the second frame."""
        name = fd.askopenfilename()
        self.input_path.delete("1.0", "end")
        self.input_path.insert(END, name)

    def input_output_path(self):
        """Inserts output picture path to the second frame."""
        name = fd.asksaveasfilename()
        self.output_path.delete("1.0", "end")
        self.output_path.insert(END, name)

    def run_operation(self):
        """Main function to process input in first frame."""
        text = self.input.get("1.0", END)[:-1]
        op = self.op_combobox.get()
        lang = self.lang_combobox.get()
        cip = self.cipher.get()
        key = self.key.get("1.0", END).strip()
        try:
            if op not in OPERATIONS:
                raise ValueError('Wrong operation chosen!')
            if lang not in LANGUAGES:
                raise ValueError('Wrong language chosen!')
            if cip not in CIPHERS:
                raise ValueError('Wrong cipher chosen!')
            if op == 'Encode':
                if cip == 'Caesar':
                    if not key:
                        raise ValueError('Key not passed!')
                    mes = Caesar.encode(text, lang, int(key))
                else:
                    if not key:
                        raise ValueError('No key passed!')
                    if cip == 'Vigenere':
                        mes = Vigenere.encode(text, lang, key)
                    elif cip == 'Vernam':
                        mes = Vernam.encode(text, key)
            else:
                if cip == 'Caesar':
                    if not key:
                        res = tk.messagebox.askquestion(
                            title='Choose crack way', message=NO_ROTATE_MESSAGE)
                        if res == 'yes':
                            mes = self.crack_caesar(text, lang)
                        else:
                            return
                    else:
                        mes = Caesar.decode(text, lang, int(key))
                else:
                    if not key:
                        raise ValueError('No key passed!')
                    if cip == 'Vigenere':
                        mes = Vigenere.decode(text, lang, key)
                    elif cip == 'Vernam':
                        mes = Vernam.decode(text, key)
        except Exception as err:
            mes = f"Error: {str(err)}"
        self.output.delete("1.0", END)
        self.output.insert(END, mes)

    def run_operation2(self):
        """Main function to process input in second frame."""
        try:
            text = self.input2.get("1.0", END)[:-1]
            in_path = self.input_path.get("1.0", END)[:-1]
            out_path = self.output_path.get("1.0", END)[:-1]
            op = self.op_combobox2.get()
            if op not in OPERATIONS:
                raise ValueError('Wrong operation chosen!')
            if op == 'Encode':
                mes = 'Success!'
                Steganography.insert_text(in_path, text, out_path)
            else:
                mes = Steganography.read_text(in_path)
        except Exception as err:
            mes = f"Error: {str(err)}"
        self.output2.delete("1.0", END)
        self.output2.insert(END, mes)
        
    @staticmethod
    def crack_caesar(text: str, lang: str) -> str:
        output = 'Frequency cracker output:\n'
        output += Caesar.crack_by_frequency(text, lang)
        output += '\n\nEnchant cracker output:\n'
        output += Caesar.crack_by_enchant(text, lang)
        return output


