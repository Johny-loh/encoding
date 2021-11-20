from tkinter import Label, Tk, Entry, Button, filedialog
from decoding import decod
from encoding import encod

def validate(new_value):
    return new_value == "" or new_value.isnumeric()

def dec():
    global file, func
    file = filedialog.askopenfilename(title='Декодировать',
                                        initialdir="\encoding",
                                        filetypes=(("AZar", "*.prar"),))
    lab = Label(text=file)
    lab.place(x=10, y=110)
    func = 'dec'

def enc():
    global file, func
    file = filedialog.askopenfilename(title='Кодировать',
                                        initialdir="\encoding",
                                        filetypes=(("txt files", "*.txt"),))
    lab = Label(text=file)
    lab.place(x=10, y=110)
    func = 'enc'

def start():
    global file, code, func
    if func == 'dec':
        decod(file)
    else:
        encod(file, code.get())
    exit(1)



window = Tk()
window.title('AZar')
but1 = Button(text='Закодировать',
                width=11,
                height=2,
                command=enc)
but2 = Button(text='Декодировать',
                width=11,
                height=2,
                command=dec)
startb = Button(text="Let's go",
                width=11,
                height=2,
                command=start)


vcmd = (window.register(validate), '%P')
code = Entry(validate='key', validatecommand=vcmd)
func = ''
file = ''

but1.place(x=45, y=10)
but2.place(x=135, y=10)
code.place(x=73, y=50)
startb.place(x=90, y=70)
window.geometry('267x130+850+405')
window.mainloop()