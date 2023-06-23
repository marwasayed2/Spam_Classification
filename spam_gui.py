from tkinter import *
from PIL import Image , ImageTk
import tkinter.messagebox as msg

root = Tk()


def spam():

    # put the model here 
    c = 0
    # output message box 
    if input_txt.get() !='':
        msg.showinfo("Spam Result" , "Not A Spam Txt")
    else:
        msg.showinfo("Spam Result" , "A Spam Txt")


# setting some heading settings
root.geometry("400x415")
root.title("Spam Detection")


# loading batch image 
spam_img = ImageTk.PhotoImage(Image.open('spam.png'))


# create the label image
Label(
    root, 
    image=spam_img,
    padx=10,
    pady=50
).pack(pady=20)


# create input field 
input_txt = Entry(
    root, 
    font=('Consolas',25,'bold'),
    width=20,
    relief=SUNKEN,
    bg = 'white',
    fg = 'black',
)
input_txt.pack(padx=10,pady=10)


# create button for action
process_btn = Button(
    root,
    text="Detect",
    font=('Consolas',20,'bold'),
    bg='#0A2647',
    fg='white',
    command = lambda : spam()
)
process_btn.pack(fill=BOTH,expand=True)

root.mainloop()