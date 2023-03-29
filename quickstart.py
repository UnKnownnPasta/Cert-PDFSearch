import PyPDF2, os
from tkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

"""
./certifs is the location of folder with the pdfs in it
why am i using pystray? cuz window.
"""

# Creating window basics
win = Tk()
win.title('$ ᴘʏꜱᴇᴀʀᴄʜ')
win.configure(bg='#2c2c2c')
win.resizable(False, False)
win.iconphoto(False, PhotoImage(file='projic.png'))
win.geometry("400x400")

# status label
label = Label(win, text='- - - - -', background='#C0C0C0', borderwidth=1, font=('Segoe UI Light', 20, 'italic'), relief="solid", width=30, height=1, foreground='black')
label.pack_propagate(0)
label.pack(pady = 20)

def searchPDF(inp):
    results=[]
    if inp == '': return 'placeholderfornonebecauseyes'
    if inp == 'Input': return 'stop'

    for fname in os.listdir('./certifs'):
        if fname.endswith('.pdf'):
            with open(os.path.join('./certifs', fname), 'rb') as file: # open file per iteration
                pdf = PyPDF2.PdfReader(file)
                text = str(pdf.pages[0].extract_text())
                splitlist = text.split(' ')

                for i in splitlist:
                    if i.strip().lower().startswith(inp.lower()):
                        results.append(fname)

    results.append(inp)
    if len(results) != 0: return results
    else: return 'placeholderfornonebecauseyes'

def mainFunc():
    run = []
    i1 = text.get()
    i2 = i1.split(' ')

    if len(i2) > 1:
        for i in i2:
            j = searchPDF(i)
            if j == 'stop': break
            run.append(j)
    else: run.append(searchPDF(i2[0]))

    if run[0] == 'placeholderfornonebecauseyes' or len(run[0]) == 1: return label.config(text='Could not find a certificate.')

    label.config(text=f'Found {sum(len(i) for i in run)} pdfs, please wait..')
    finalResult = []

    for i in run:
        for j in range(0,len(i)-1):
            print(j)
            with open(os.path.join(f'./certifs/{i[j]}'), 'rb') as file:
                check = PyPDF2.PdfReader(file)
                t = str(check.pages[0].extract_text())
                t = t.split(' ')
                if (t[0] == i[-1]) or (t[0].lower() == i[-1].lower()) or (t[1] == i[-1]) or (t[1].lower() == i[-1].lower()):
                    finalResult.append(file.name)

    print(finalResult)


def temp_text(e): text.delete(0,"end")
text = Entry(win, width=40,  font=("Comic Sans MS", 10, "bold"))
text.insert(0, "krish")
text.pack(pady = 80, padx=10)
text.bind("<FocusIn>", temp_text)

# creating a button to search with
Button(win, text="Find", command=mainFunc, font=('Arial', 10), relief='solid').pack()

# Define a function for quit the window
def quit_window(): win.destroy()
   
# Define a function to show the window again
def show_window(icon, item): icon.stop(); win.after(0, win.deiconify())

# Hide the window and show on the system taskbar
def hide_window():
    win.withdraw()
    image = Image.open("projic.png")
    menu = (item('name', action), item('name', action))
    icon = pystray.Icon("name", image, "title", menu)
    icon.run()

win.protocol('WM_DELETE_WINDOW', quit_window)


win.mainloop()
