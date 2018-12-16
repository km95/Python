import Node
import matplotlib.pyplot as plt
import networkx as nx
from tkinter import *


def cpm(T, table):
    table_of_node = []
    table_of_cost_nodes = table
    critical_patch = []

    find_tab1 = []
    find_tab2 = []
    for i in table_of_cost_nodes:
        find_tab1.append(i.start)
        find_tab2.append(i.stop)
    node = len(set(find_tab1) | set(find_tab2))

    T.insert(END, "\nLista kosztow : \n")
    for i in table_of_cost_nodes:
        T.insert(END, i.wyswietl())

    for i in range(node):
        tab = []
        for j in range(len(table_of_cost_nodes)):
            if i + 1 == table_of_cost_nodes[j].start:
                tab.append(table_of_cost_nodes[j])
        table_of_node.append(Node.Node(int(i + 1), tab))

    for i in range(len(table_of_cost_nodes)):
        cost = table_of_node[table_of_cost_nodes[i].start - 1].t0 + table_of_cost_nodes[i].cost
        if cost > table_of_node[table_of_cost_nodes[i].stop - 1].t0:
            table_of_node[table_of_cost_nodes[i].stop - 1].t0 = cost
    T.insert(END, "\nLista wezlow : \n")
    for i in table_of_node:
        T.insert(END, i.wyswietl())

    table_of_node[node - 1].t1 = table_of_node[node - 1].t0
    table_of_node[node - 1].L = table_of_node[node - 1].t1 - table_of_node[node - 1].t0
    critical_patch.append(table_of_node[node - 1].id)
    for i in range(len(table_of_cost_nodes) - 1, -1, -1):
        for j in table_of_node:
            if table_of_cost_nodes[i].start == j.id:
                cost = table_of_node[table_of_cost_nodes[i].stop - 1].t1 - table_of_cost_nodes[i].cost
                if j.t1 == 0 or j.t1 > cost:
                    if j.id == 1 and j.t1 <= 0:
                        continue
                    j.t1 = cost
                    j.L = j.t1 - j.t0
                    if j.L == 0:
                        critical_patch.append(j.id)

    T.insert(END, "\nLista wezlow : \n")
    for i in table_of_node:
        T.insert(END, i.wyswietl())

    T.insert(END, "\nSciezka krytyczna: \n")
    critical_patch = critical_patch[::-1]
    T.insert(END, critical_patch)
    T.insert(END, "\n\n")

    plt.clf()
    g = nx.Graph()
    for i in table_of_cost_nodes:
        g.add_edge(i.start, i.stop)

    nx.draw_networkx(g)

    plt.savefig("simple_path.png")

    plt.show()
