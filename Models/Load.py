from mesa import Agent

class Load(Agent):
    Loaded = False
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.x, self.y = pos
    

    def step(self):
        """
        If the tree is on fire, spread it to fine trees nearby.
        """
        # for neighbor in self.model.grid.neighbor_iter(self.pos):
        #     self.pos = neighbor.pos
        return 