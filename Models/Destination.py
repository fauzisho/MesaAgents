from mesa import Agent


class Destination(Agent):
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.x, self.y = pos
        self.Loaded = False
