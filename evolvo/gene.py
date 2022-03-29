import numpy as np


class Gene():
    """ Heavily inspired by the work of David R. Miller"""
    def __init__(self):
        self.source_type = None # binary (input node or hidden node)
        self.sourceID = None
        self.sink_type = None # binary (output node or hidden node)
        self.sinkID = None
        self.weight = None # (-5, 5)
