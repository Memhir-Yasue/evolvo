class Neuron:

    def __init__(self, id: int, value: float = None):
        self.id = id
        self.value = value
        self.connections_count = 0
        self.connections = []

    def connect_with(self, neuron_id: int):
        self.connections.append(neuron_id)
        self.connections_count += 1
        return f"Connected with {neuron_id}"

    def disconnect(self, id: int):
        if id in self.connections:
            self.connections.remove(id)
            self.connections_count -= 1
            return f"Disconnected from {id}"

    def get_connections(self):
        return self.connections

