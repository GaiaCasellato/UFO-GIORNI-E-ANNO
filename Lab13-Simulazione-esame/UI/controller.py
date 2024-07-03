import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        pass

    def handle_graph(self, e):
        print("creo grafo")
        self._model.buildGraph(self._view.ddanno.value, self._view.ddgiorni.value)

        self._view.txt_result.controls.append(ft.Text(
            f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))

        for i in self._model.nodi:
            self._view.txt_result.controls.append(ft.Text(f"Stato {i.Name} --> peso {self._model.sommaStato(i)}"))

        self._view.update_page()


    def handle_path(self, e):
        pass

    def handlegiorni(self,e):
        try: int(self._view.ddgiorni.value)
        except ValueError:
            self._view.create_alert("Valore inserito non corretto.")
        if 1 <= int(self._view.ddgiorni.value) <= 180:
            self._view.btn_graph.disabled = False
        else:
            self._view.create_alert("Valore inserito non corretto.")

        self._view._page.update()

    def handle_anno(self,e):
        try: int(self._view.ddanno.value)
        except ValueError:
            self._view.create_alert("Valore inserito non corretto.")
        if 1906 <= int(self._view.ddanno.value) <= 2014:
            self._view.btn_graph.disabled = False
        else:
            self._view.create_alert("Valore inserito non corretto.")
        self._view._page.update()

