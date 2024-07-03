import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.nodi = DAO.getAllStates()
        self.archi = DAO.getArchi()

    def buildGraph(self, anno, giorni):
        print("creo nodi")
        self.grafo.add_nodes_from(self.nodi)
        idMap = {}
        for i in self.nodi:
            idMap[i.id] = i
        print( " aggiungo pesi")
        for arco in self.archi:
                self.grafo.add_edge(idMap[arco[0]], idMap[arco[1]], weight= DAO.getPeso(anno,giorni, idMap[arco[0]].id,idMap[arco[1]].id)[0])
        print("fine pesi")
    def sommaStato(self,n):
        vicini = self.grafo.neighbors(n)
        somma = 0
        for i in vicini:
            somma += self.grafo[n][i]["weight"]
        return somma

    def get_num_of_nodes(self):
        return self.grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self.grafo.number_of_edges()







