class ClienteService:
    def __init__(self):
        self.clientes = []

    def crear_cliente(self, cliente):
        self.clientes.append(cliente)

    def obtener_clientes(self):
        return self.clientes

    def actualizar_cliente(self, id, nuevo_cliente):
        for i, cliente in enumerate(self.clientes):
            if cliente.id == id:
                self.clientes[i] = nuevo_cliente

    def eliminar_cliente(self, id):
        self.clientes = [cliente for cliente in self.clientes if cliente.id != id]
        