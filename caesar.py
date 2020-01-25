from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import os

try:
    import pyperclip
    from nltk.tokenize import TweetTokenizer
except:
    try:
        os.system("pip install pyperclip")
        os.system("pip install nltk")
    except:
        messagebox.showinfo("INTERNET UNAVAILABLE","Please connect to internet and try again")
        exit(1)
end_of_line = "\n________________________________________________________________________________________________\n"
bf = 0
try:
    file = open("words.txt")
    my_dict = list(file.read().lower().split('\n'))
    file.close()
except:
    bf = 1


root = Tk()
root.title("CAESAR CIPHER")
root.geometry("800x670")
root.resizable(False, False)

#Frame 1
Frame1 = Frame(root)

TextAreaIN = Text(Frame1, width=100, height=15, bd=5)
ScrollBarIN = Scrollbar(Frame1)
ScrollBarIN.config(command=TextAreaIN.yview)
TextAreaIN.config(yscrollcommand=ScrollBarIN.set)
ScrollBarIN.pack(side=RIGHT, fill=Y)
TextAreaIN.pack(expand=YES)


Frame1.pack(side=TOP, ipady=3)

#Frame 2
Frame2 = Frame(root)

def Clear_IN():
    TextAreaIN.delete("1.0", END)

def Copy_IN():
    s = str(TextAreaIN.get("1.0", END))
    s = s[:len(s)-1]
    pyperclip.copy(s)

def Paste_IN():
    TextAreaIN.insert(INSERT,pyperclip.paste())


def Encoding():
    raw_text = str(TextAreaIN.get("1.0",END))
    try:
        my_key = int(key.get())
    except:
        messagebox.showinfo("INVALID KEY", "Please choose a key to encrypt")
        my_key = 0
    new_text = ""

    for i in raw_text:
        if (ord(i) >= 97 and ord(i) <= 122):
            x = int(ord(i)) + my_key
            if (x > 122):
                x = x - 26
            new_text += chr(x)
        elif (ord(i) >= 65 and ord(i) <= 90):
            x = int(ord(i)) + my_key
            if (x > 90):
                x = x - 26
            new_text += chr(x)
        elif(i == '\0'):
            break
        else:
            new_text += i
    Clear_OUT()
    TextAreaOUT.config(state="normal")
    TextAreaOUT.insert("1.0", new_text)
    TextAreaOUT.config(state="disabled")

def Decoding():
    raw_text = str(TextAreaIN.get("1.0",END))
    try:
        my_key = int(key.get())
    except:
        messagebox.showinfo("INVALID KEY", "Please choose a key to decrypt")
        my_key = 0
    new_text = ""

    for i in raw_text:
        if (ord(i) >= 97 and ord(i) <= 122):
            x = int(ord(i)) - my_key
            if (x < 97):
                x = x + 26
            new_text += chr(x)
        elif (ord(i) >= 65 and ord(i) <= 90):
            x = int(ord(i)) - my_key
            if (x < 65):
                x = x + 26
            new_text += chr(x)
        else:
            new_text += i
    Clear_OUT()
    TextAreaOUT.config(state="normal")
    TextAreaOUT.insert("1.0", new_text)
    TextAreaOUT.config(state="disabled")


def Brute_Force():
    flag = 1
    raw_text = str(TextAreaIN.get("1.0", END))
    Clear_OUT()
    try:
        for my_key in range(1, 26):
            new_text = ""
            for i in raw_text:
                if (ord(i) >= 97 and ord(i) <= 122):
                    x = int(ord(i)) - my_key
                    if (x < 97):
                        x = x + 26
                    new_text += chr(x)
                elif (ord(i) >= 65 and ord(i) <= 90):
                    x = int(ord(i)) - my_key
                    if (x < 65):
                        x = x + 26
                    new_text += chr(x)
                else:
                    new_text += i
            tokens = TweetTokenizer().tokenize(new_text.lower())
            if (tokens[0] in my_dict and tokens[len(tokens) - 1] in my_dict):
                flag = 0
                TextAreaOUT.config(state="normal")
                TextAreaOUT.insert("1.0", "Key: " + str(my_key) + "\nMessage: " + new_text + end_of_line)
                TextAreaOUT.config(state="disabled")
        if (flag):
            messagebox.showinfo("STRONG ENCRYPTION", "Too strong to decrypt")
    except:
        messagebox.showinfo("INVALID INPUT", "Can not decrypt empty text")


ButtonClearIN = Button(Frame2, text="CLEAR", relief=RIDGE, bd=5, command=Clear_IN)
ButtonClearIN.grid(row=0, column=0, ipadx=30, ipady=10)

ButtonCopyIn = Button(Frame2, text="COPY", relief=RIDGE, bd=5, command=Copy_IN)
ButtonCopyIn.grid(row=0, column=2, ipadx=30, ipady=10)

ButtonPasteIN = Button(Frame2, text="PASTE", relief=RIDGE, bd=5, command=Paste_IN)
ButtonPasteIN.grid(row=0, column=4, ipadx=30, ipady=10)

LabelSpaceF2R0C5 = Label(Frame2, text=" ")
LabelSpaceF2R0C5.grid(row=0,column=5)

ButtonBruteForce = Button(Frame2, text="BRUTE FORCE", relief=RIDGE, bd=5, command=Brute_Force)
ButtonBruteForce.grid(row=0, column=6, ipadx=30, ipady=10)

ButtonEncode = Button(Frame2, text="ENCODE", bg="White", relief=GROOVE, bd=5, command=Encoding)
ButtonEncode.grid(row=1, column=0, ipadx=30, ipady=10)

LabelSpaceF2R1C1 = Label(Frame2, text=" ")
LabelSpaceF2R1C1.grid(row=1,column=1)

key = StringVar()
DropDownKey = Combobox(Frame2, textvariable=key, justify='center', width=8, state="readonly",
                       values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
DropDownKey.set("Enter Key")
DropDownKey.config(font="BOLD 14")
DropDownKey.grid(row=1, column=2, rowspan=2, ipady=10)

LabelSpaceF2R1C3 = Label(Frame2, text=" ")
LabelSpaceF2R1C3.grid(row=1,column=3)

ButtonDecode = Button(Frame2, text="DECODE", bg="White", relief=GROOVE, bd=5, command=Decoding)
ButtonDecode.grid(row=1, column=4, ipadx=30, ipady=10)

Frame2.pack()


#Frame 3
Frame3 = Frame(root)

TextAreaOUT = Text(Frame3, width=100, height=15, bd=5)
ScrollBar = Scrollbar(Frame3)
ScrollBar.config(command=TextAreaOUT.yview)
TextAreaOUT.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side=RIGHT, fill=Y)
TextAreaOUT.config(state="disabled")
TextAreaOUT.pack(expand=YES)

Frame3.pack()

Frame4 = Frame(root)


def Clear_OUT():
    TextAreaOUT.config(state="normal")
    TextAreaOUT.delete("1.0", END)
    TextAreaOUT.config(state="disabled")

def Copy_OUT():
    s = str(TextAreaOUT.get("1.0", END))
    s = s[:len(s)-2]
    pyperclip.copy(s)

def Save_As():
    try:
        s = str(TextAreaOUT.get("1.0", END))
        save = filedialog.asksaveasfilename(defaultextension="*.txt", filetypes=(("text files","*.txt"),("all files","*.*")))
        file=open(save, "w")
        file.write(s)
        file.close()
    except:
        messagebox.showinfo("INCOMPLETE ACTION", "File not saved!")


ButtonClearOUT = Button(Frame4, text="CLEAR", relief=RIDGE, bd=5, command=Clear_OUT)
ButtonClearOUT.grid(row=0, column=0, ipadx=30, ipady=10)

LabelSpaceF4R0C1 = Label(Frame4, text=" ")
LabelSpaceF4R0C1.grid(row=0,column=1)

ButtonCopyOUT = Button(Frame4, text="COPY", relief=RIDGE, bd=5, command=Copy_OUT)
ButtonCopyOUT.grid(row=0, column=2, ipadx=30, ipady=10)

LabelSpaceF4R0C3 = Label(Frame4, text=" ")
LabelSpaceF4R0C3.grid(row=0,column=3)

ButtonSaveAs = Button(Frame4, text="SAVE", relief=RIDGE, bd=5, command=Save_As)
ButtonSaveAs.grid(row=0, column=4, ipadx=30, ipady=10)

if(bf):
    messagebox.showinfo("FILE MISSING", "words.txt file is missing! Brute force will not work.")
    ButtonBruteForce.config(state = DISABLED)

Frame4.pack()

root.mainloop()