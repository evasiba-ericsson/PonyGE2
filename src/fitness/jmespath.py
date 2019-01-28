from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff

from difflib import SequenceMatcher

import sys

class jmespath(base_ff):
    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()
        
#         self.training, self.test, self.embed_header, self.embed_footer = \
#             self.get_data(params['DATASET_TRAIN'], params['DATASET_TEST'])
#         self.eval = self.create_eval_process()
        if params['MULTICORE']:
            print("Warning: Multicore is not supported with progsys "
                  "as fitness function.\n"
                  "Fitness function only allows sequential evaluation.")
            
    def evaluate(self, ind, **kwargs):
        phenotype = ind.phenotype
        target = "locations[?state == 'WA'].name | sort(@) | {WashingtonCities: join(', ', @)}"
        similarity_metric = 1.0 - SequenceMatcher(None, target, phenotype).ratio() 
        return similarity_metric