import numpy as np

from .constants import INPUT_NODE_TYPE, INTERNAL_NODE_TYPE, OUTPUT_NODE_TYPE
from .gene import Gene


class Genome:
    def __init__(self):
        self.genes = []
        self.description = {'Sequence_length': 0,
                            'Input-to-Output': 0,
                            'Input-to-Internal': 0,
                            'Internal-to-Output': 0}

    def _update_description(self, source_type: int, sink_type: int):
        if source_type == INPUT_NODE_TYPE and sink_type == OUTPUT_NODE_TYPE:
            self.description['Input-to-Output'] += 1
        elif source_type == INPUT_NODE_TYPE and sink_type == INTERNAL_NODE_TYPE:
            self.description['Input-to-Internal'] += 1
        elif source_type == INTERNAL_NODE_TYPE and sink_type == OUTPUT_NODE_TYPE:
            self.description['Internal-to-Output'] += 1

    def generate_gene_sequence(self):
        sequence_length = np.random.randint(1, 100)
        self.description['Sequence_length'] = sequence_length

        for _ in range(sequence_length):
            gene = Gene()

            gene.source_type = np.random.randint(0, 2) # input node (0) or internal node (1)
            # gene.sourceID = sequence_length % 5
            gene.sink_type = np.random.randint(1, 3) # internal node (1) or output node (2)
            # gene.sinkID = sequence_length % 5
            gene.weight = np.random.uniform(-5, 5)

            self.genes.append(gene)
            self._update_description(gene.source_type, gene.sink_type)




