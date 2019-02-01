from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff
import jmespath

from difflib import SequenceMatcher

import sys

class jmespathFit(base_ff):        
    
    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()
         
#         self.training, self.test, self.embed_header, self.embed_footer = \
#             self.get_data(params["DATASET_TRAIN"], params["DATASET_TEST"])
#         self.eval = self.create_eval_process()
            
    def evaluate(self, ind, **kwargs):
        phenotype = ind.phenotype
        if ("locations [?" in phenotype):
            v = 0
        sourceJson = '{"locations": [{"name": "Seattle", "state": "WA"},{"name": "New York", "state": "NY"},{"name": "Bellevue", "state": "WA"},{"name": "Olympia", "state": "WA"}]}'
        resultJson = '{"WashingtonCities": "Bellevue, Olympia, Seattle"}'
        target = "locations [?state == 'WA'].name | sort(@) | { WashingtonCities : join(', ', @) }"
        
        try:
            target = jmespath.search(phenotype, sourceJson)
            target = str(target)
            similarity_metric = 1.0 - SequenceMatcher(None, target, resultJson).ratio() 
            return similarity_metric
        except Exception as err:
            return 1