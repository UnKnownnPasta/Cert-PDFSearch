import PyPDF2, os, threading
from tkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

"""
./certifs is the location of folder with the pdfs in it
why am i using pystray? cuz window.
"""

def main():
    # Creating window basics
    win = Tk()
    win.title('$ ᴘʏꜱᴇᴀʀᴄʜ')
    win.configure(bg='#2c2c2c')
    win.resizable(False, False)
    win.iconphoto(False, PhotoImage(file='projic.png'))
    win.geometry("410x400")

    # status label
    label = Label(win, text='- - - - -', background='#C0C0C0', borderwidth=1, font=('Segoe UI Light', 20, 'italic'), relief="solid", width=29, height=1, foreground='black')
    label.pack()
    label.pack_propagate(0)
    label.place(y=20, x=0)

    output = Label(win, text=' ', background='#7F7F7F', borderwidth=1, font=('Segoe UI Light', 20, 'italic'), relief="solid", width=30, height=3, foreground='black')
    output.pack()
    output.pack_propagate(0)
    output.place(x=0, y= 80)

    def searchPDF(inp):
        results=[]
        inp = inp.strip()
        if inp == '': return 'placeholderfornonebecauseyes'
        if inp == 'Input': return 'stop'

        label.configure(text='Searching...')
        output.configure(text=' ')

        for fname in os.listdir('./certifs'):
            if fname.endswith('.pdf'):
                with open(os.path.join('./certifs', fname), 'rb') as file: # open file per iteration
                    text = str(PyPDF2.PdfReader(file).pages[0].extract_text()).split(' ') # 

                    for i in text:
                        if i.strip().lower().startswith(inp.lower()) and i.strip() != '':
                            results.append(fname)

        results.append(inp)
        if len(results) != 0: return results
        else: return 'placeholderfornonebecauseyes'

    def mainFunc():
        run = []
        i1 = text.get().strip()
        i2 = i1.split(' ')

        if len(i2) > 1:
            for o in i2:
                if o.strip() != '':
                    j =searchPDF(o)
                    if j == 'stop': break
                    run.append(j)
        else: run.append(searchPDF(i2[0]))

        if run[0] == 'placeholderfornonebecauseyes' or len(run[0]) == 1: return label.config(text='Could not find a certificate.')

        # label.config(text=f'Found {sum(len(i) for i in run)} pdfs, please wait..')
        finalResult = collectedNames = []
        collectedNames = [i[-1] for i in run if i[-1] not in collectedNames]

        for i in run:
            for j in range(0,len(i)-1):
                with open(os.path.join(f'./certifs/{i[j]}'), 'rb') as file:
                    check = PyPDF2.PdfReader(file)
                    t = str(check.pages[0].extract_text()).split(' ')
                    g = [word.strip() for word in t if word.strip() != '']

                    print(collectedNames, g)
                    for n in range(0, len(collectedNames)):
                        if len(collectedNames)-1 == n and len(collectedNames) <= len(g):
                            teststring1 = teststring2 = ''
                            for lk in range(0, len(collectedNames)):
                                teststring1 += g[lk].lower() + ' '
                                teststring2 += collectedNames[lk].lower() + ' '

                            if teststring1 == teststring2:
                                finalResult.append(file.name)

        print(run, finalResult)
        result = ''
        for i in finalResult[:1]:
            result += f"""{i.replace('./certifs/', '')}
"""
        output.configure(text=result)

        return label.configure(text=f'Found {len(finalResult)} pdfs')

    def start_combine_in_bg():
        threading.Thread(target=mainFunc).start()

    def temp_text(e): text.delete(0,"end")
    text = Entry(win, width=40,  font=("Comic Sans MS", 10, "bold"))
    text.insert(0, "  Enter your name here!")
    text.pack()
    text.pack_propagate(0)
    text.place(y= 260, x=40)
    text.bind("<FocusIn>", temp_text)

    # creating a button to search with
    b = Button(win, text="Find", command=start_combine_in_bg, font=('Arial', 10), relief='solid')
    b.pack()
    b.pack_propagate(0)
    b.place(x=180, y = 300)
    

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

if __name__ == '__main__':
    main()
