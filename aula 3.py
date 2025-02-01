from tkinter import *

root = Tk()
root.title("colors")

azul='#007fff'
vermelho='#ff0000'
amarelo='#fffa00'
verde='#45ff00'

root.geometry('500x600')
root.wm_resizable(width=False, height=False)
root.configure(bg=azul)

def fundo1():
    root.configure(background=azul)
    label.configure(text='azul', background=azul)

def fundo2():
    root.configure(background=vermelho)
    label.configure(text='vermelho', background=vermelho)

def fundo3():
    root.configure(background=amarelo)
    label.configure(text='amarelo', background=amarelo)

def fundo4():
    root.configure(background=verde)
    label.configure(text='verde', background=verde)

label= Label(root, text='escolha uma cor', font='Arial 20 bold')
label.place(width=200, height=100, x=150, y=400 )


bt1 = Button(root, text='azul', font='Arial 14 bold', command=fundo1)
bt1.place(width=200, height=160, x=40, y=20)

bt2 = Button(root, text='vermelho', font='Arial 14 bold', command=fundo2)
bt2.place(width=200, height=160, x=260, y=20)

bt3 = Button(root, text='verde', font='Arial 14 bold', command=fundo4)
bt3.place(width=200, height=160, x=40, y=200)

bt4 = Button(root, text='amarelo', font='Arial 14 bold', command=fundo3)
bt4.place(width=200, height=160, x=260, y=200)


root.mainloop()