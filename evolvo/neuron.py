class Neuron:

    def __init__(self, id: int, value: float):
        self.id = id
        self.value = value
        self.connections = []

    def connect_with(self, id: int):
        self.connections.append(id)
        return f"Connected with {id}"

    def disconnect(self, id: int):
        if id in self.connections:
            self.connections.remove(id)
            return f"Disconnected from {id}"

    def get_connections(self):
        return self.connections

