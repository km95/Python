from tkinter import *
from tkinter.filedialog import askopenfilename
import CPM
import CostNodes
import json


def string(cost, start, stop):
    return "wezel %d -> %d koszt = %d\n" % (start, stop, cost)


def add_cost():
    try:
        cost = int(m1.get())
        start = int(m2.get())
        stop = int(m3.get())
        table_of_cost_nodes.append(CostNodes.CostNodes(cost, start, stop))
        T.insert(END, string(cost, start, stop))
    except ValueError:
        T.insert(END, "\nTo nie jest liczba")




def start():
    CPM.cpm(T, table_of_cost_nodes)


def openfile():
    filename = askopenfilename()
    try:
        with open(filename) as data_file:
            data = json.load(data_file)
            table_of_cost_nodes = [CostNodes.CostNodes(int(x["cost"]), int(x["start"]), int(x["stop"])) for x in
                                   data["CostNodes"]]

        CPM.cpm(T, table_of_cost_nodes)
    except FileNotFoundError:
        T.insert(END, "\nProsze wybrac plik")

table_of_cost_nodes = []
root = Tk()
root.title("CPM gui")
root.geometry("660x500")
T = Text(root)

m1 = StringVar()
m2 = StringVar()
m3 = StringVar()

button1 = Button(Frame(root).pack(), text="Add", command=add_cost)
button2 = Button(Frame(root).pack(), text="Start", command=start)
button3 = Button(Frame(root).pack(), text="File", command=openfile).pack(side=TOP, anchor=W, fill=X, expand=YES)
button2.pack(side=TOP)

mlabel1 = Label(root, text="Podaj koszt ").pack()
mEntry1 = Entry(root, textvariable=m1).pack()

mlabel2 = Label(root, text="Podaj poczatek ").pack()
mEntry2 = Entry(root, textvariable=m2).pack()

mlabel3 = Label(root, text="Podaj koniec ").pack()
mEntry3 = Entry(root, textvariable=m3).pack()
button1.pack(side=TOP)

T.pack()
scroll = Scrollbar(root, command=T.yview)
T.configure(yscrollcommand=scroll.set)
T.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
