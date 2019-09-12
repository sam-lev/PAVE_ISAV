import PAVE
from torch.utils.data import DataLoader

def load_data(visualisation_variable=None, path = None):
    if path:
        train_set  = PAVE.AdiosDataLoader(path)
        train_data = DataLoader(dataset = train_set)
        return train_data
    else:
        PAVE.open(visualisation_variables)
        
def train(Model, simulation_variables):
    for (i, var) in enumerate(visualisation_variables):
        train_sample = load_data(var)
        prediction = Model(train_sample)
        ...
