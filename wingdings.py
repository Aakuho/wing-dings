import random
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import simpleaudio as sa

root = tk.Tk()

root.iconbitmap('./assets/icon.ico')
root.title('☹︎☜︎✌︎☼︎☠︎✋︎☠︎☝︎   🕈︎✋︎☠︎☝︎👎︎✋︎☠︎☝︎💧︎')
root.geometry("700x180")
root['background'] = '#373737'
root.resizable(width=False, height=False)

label = tk.Label(
    root, 
    text="Upper case Wing Dings\n(it looks cooler than lower case)", 
    font=('Arial bold', 12), 
    anchor='w', 
    justify='left', 
    background='#303030', 
    foreground='#ffffff'
    ).grid(sticky = W, column=0, row=0)

#textbox = tk.Text(root, height=1, font=('Arial bold', 12)).grid(sticky=W, column=0, row=1)

arrow = tk.Label(root, font=('arial bold', 12),text=">", background='#373737', borderwidth=0, foreground='#ffffff')
arrow.place(anchor='w', y = 55)

inp = tk.Entry(root, font=('arial bold', 12), background='#373737', borderwidth=0, foreground='#ffffff', highlightthickness=1, highlightbackground='#ffffff', highlightcolor='#ffffff')
inp.place(anchor='w', y = 55, x = 20)

ratio = tk.Label(root, font=('arial bold', 12),text="0 correct   0 incorrect", background='#373737', borderwidth=0, foreground='#ffffff')
ratio.place(anchor='w', y = 83, x = 20)


wdgcorrect = ImageTk.PhotoImage(Image.open("./assets/wdg_correct_small.png"))
wdgincorrect = ImageTk.PhotoImage(Image.open("./assets/wdg_incorrect_small.png"))

feedbackimg = tk.Label(root, image=wdgincorrect, highlightthickness=0, borderwidth=0, anchor='w')
feedbackimg.place(anchor='w', y = 83, x = 312)

feedback = tk.Label(root, font=('arial', 20),text="👌☜☝✋☠", background='#373737', borderwidth=0, foreground='#ffffff')
feedback.place(anchor='w', y = 84, x = 400)

def correct():
    feedbackimg.config(image=wdgcorrect)
    feedback.config(text='👍⚐☼☼☜👍❄')
    #playsound(os.path.dirname(__file__) + '\\assets\\wdg_correct.wav')
    sa.WaveObject.from_wave_file("./assets/wdg_correct.wav").play().wait_done()

def incorrect(correct : str):
    feedbackimg.config(image=wdgincorrect)
    feedback.config(text=f'✋☠👍⚐☼☼☜👍❄ : {correct}')
    sa.WaveObject.from_wave_file("./assets/wdg_incorrect.wav").play().wait_done()


#? -----------------------------------

show = tk.Label(root, text='', font=('arial',50), background='#373737', borderwidth=0, foreground='#ffffff', highlightthickness=1, highlightbackground='#ffffff', highlightcolor='#ffffff')
show.place(anchor='w', y = 83, x = 220)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "✌👌👍👎☜☞☝☟✋🙂😐😟💣☠⚐🏱✈☼💧❄🕆✞🕈✠✡☪"
c = 0
inc = 0
dbg = None
show.config(text=f'{symbols[(l := random.randint(0, 25))]}')

def func(event):
    getvalue()

def getvalue():
    global c, inc, l, dbg
    if dbg: dbg.destroy()
    else: pass
    if not inp.get():
        dbg = tk.Label(root, text='Empty input', font=('Arial bold', 12), background='#373737', foreground='#ffffff')
        dbg.place(anchor='w', x = 50, y = 110)
    else:
        s = inp.get()
        if s.upper() == letters[l]:
            correct()
            c+=1
            show.config(text=f'{symbols[(l := random.randint(0, 25))]}')
        else:
            incorrect(letters[l])
            inc+=1
            show.config(text=f'{symbols[(l := random.randint(0, 25))]}')
        inp.delete(0, 'end')
    ratio.config(text=f"{c} correct   {inc} incorrect")

root.bind('<Return>', func)

#? -----------------------------------

root.mainloop()
