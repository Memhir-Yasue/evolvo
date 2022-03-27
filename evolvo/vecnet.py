import numpy as np


class VecNetwork:
    """ A Vectorized FeedForward Neural Network """

    def __init__(self, alpha_1: np.ndarray, theta_1: np.ndarray, architecture: list):
        """

        :param alpha_1: Initial Inputs
        :param theta_1: Initial Weights
        :param architecture: A list where each index corresponds to a layer, and the element denotes the num of nodes
                             Example: [2,3,3,1] is a network with two input nodes, two hidden layers with three nodes
                                      each, and one output node
        """

        self.init_input = alpha_1
        self.init_weights = theta_1
        self.activation = lambda x: x * (x > 0) # ReLU

        self.architecture = architecture
        self.total_layers = len(architecture)

        self.vectors = {}

        self._init_vecs()

    def _init_vecs(self):

        if len(self.init_input) != self.architecture[0]:
            raise AssertionError\
                (f"You specified that the network will contain {self.architecture[0]} input nodes, "
                 f"yet you've entered {len(self.init_input)}")

        self.vectors['alpha_0'] = self.init_input
        self.vectors['theta_0'] = self.init_weights
        self.vectors['zeta_1'] = np.dot(self.init_weights, self.init_input)

        # TODO: User (or some external algo) can specify fixed values for the weights
        # Hidden layer initializations and computations (given 1st set of inputs)
        for j, n_nodes in enumerate(self.architecture):

            if j > 0:

                if j == len(self.architecture) - 1:
                    self.vectors[f'alpha_{j}'] = self.activation(self.vectors[f'zeta_{j}'])
                    continue

                next_n_nodes = self.architecture[j+1]
                self.vectors[f'alpha_{j}'] = self.activation(self.vectors[f'zeta_{j}'])
                self.vectors[f'theta_{j}'] = np.random.normal(size=(next_n_nodes, n_nodes)) + 1 # bias
                self.vectors[f'zeta_{j+1}'] = np.dot(self.vectors[f'theta_{j}'], self.vectors[f'alpha_{j}'])

    def get_output(self):
        return self.vectors[f'alpha_{self.total_layers - 1}']
