from tkinter import *
import tkinter.ttk as ttk
import csv

def display_csvfile():
    root = Tk()
    root.title("Python - Import CSV File To Tkinter Table")
    width = 400
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("IV[0]", "IV[1]", "IV[2]","Snapheader"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('IV[0]', text="IV[0]", anchor=W)
    tree.heading('IV[1]', text="IV[1]", anchor=W)
    tree.heading('IV[2]', text="IV[2]", anchor=W)
    tree.heading('Snapheader', text="Snapheader", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.pack()

    with open('WEPOutputSim.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            iv0 = row['IV0']
            iv1 = row['IV1']
            iv2 = row['IV2']
            snapheader = row['Snapheader']
            tree.insert("", 0, values=(iv0, iv1, iv2, snapheader))
