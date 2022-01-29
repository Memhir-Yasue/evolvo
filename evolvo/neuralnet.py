from evolvo.neuron import Neuron
from evolvo.adjmatrix import AdjacencyMatrix


class NeuralNetwork:
    def __init__(self, max_size=10):
        self.root_id = 0
        self.max_size = max_size
        self.root = Neuron(self.root_id)
        self.neurons = {self.root_id: self.root}
        self.neurons_count = 1
        self.relations = AdjacencyMatrix(max_size)

    def add_to_root(self):
        if self.neurons_count < self.max_size:
            child_id = self.neurons_count
            self.neurons[child_id] = Neuron(child_id)
            self.root.connect_with(child_id)
            self.relations.activate_relation(self.root_id, child_id)
            self.neurons_count += 1

    def add_unto(self, parent_id):
        if self.neurons_count < self.max_size:
            parent_neuron = self.neurons[parent_id]
            child_id = self.neurons_count

            self.neurons[child_id] = Neuron(child_id)
            parent_neuron.connect_with(child_id)
            self.relations.activate_relation(parent_id, child_id)
            self.neurons_count += 1

    def get_neurons(self):
        return self.neurons

    def get_relations(self):
        return self.relations.get_matrix()
