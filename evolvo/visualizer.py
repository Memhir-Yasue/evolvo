import matplotlib.pyplot as plt
import networkx as nx

from evolvo.neuralnet import NeuralNetwork


class Visualizer:
    def __init__(self, neuralnetwork: NeuralNetwork):
        self.neuralnet = neuralnetwork
        self.adj_matrix = neuralnetwork.get_relations()

    def draw_network(self):
        graph = nx.from_numpy_matrix(self.adj_matrix, create_using=nx.DiGraph)
        pos = nx.spring_layout(graph)
        nx.set_node_attributes(graph, pos, 'pos')
        nx.draw(graph, with_labels=True)
        plt.show()


