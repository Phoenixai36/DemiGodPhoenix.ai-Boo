class ThanathosAgent:
    def __init__(self, name, network, patience=0.5):
        self.name = name
        self.network = network
        self.patience = patience
    def decay(self, component):
        return f"{self.name} decays {component}"