from mesa import Model
from mesa.time import BaseScheduler, SimultaneousActivation, StagedActivation
from mesa.space import SingleGrid

from .random_agent import SimpleAgent, Destination
from .Load import Load


class LoadDeliverGame(Model):
    """
    Represents the 2-dimensional array of cells in Conway's
    Game of Life.
    """
    Entities = set()
    Second_initialization = False
    def __init__(self, height=10, width=10):
        """
        Create a new playing area of (height, width) cells.
        """
        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.
        
        #self.schedule = SimultaneousActivation(self)
        #self.schedule = StagedActivation(self)
        self.schedule = BaseScheduler(self)
        # Use a simple grid, where edges wrap around.
        self.grid = SingleGrid(height, width, torus=True)

        # Place a cell at each location, with some initialized to
        # ALIVE and some to DEAD.
        # for (contents, x, y) in self.grid.coord_iter():
        #     cell = Cell((x, y), self)
        #     if self.random.random() < 0.1:
        #         cell.state = cell.ALIVE
        #     self.grid.place_agent(cell, (x, y))
        #     self.schedule.add(cell)

        # emergent behavior
        # self.Entities = set()
        # # Agent 1
        # Ag = SimpleAgent((8, 1), self)
        # self.grid.place_agent(Ag, (8, 1))
        # self.schedule.add(Ag)
        # self.Entities.add(Ag)
        # # Agent 2
        # Ag = SimpleAgent((8, 2), self)
        # self.grid.place_agent(Ag, (8, 2))
        # #Ag = SimpleAgent((9, 2), self)
        # #self.grid.place_agent(Ag, (9, 2))
        # self.schedule.add(Ag)
        # self.Entities.add(Ag)
        # # Agent 3
        # Ag = SimpleAgent((9, 1), self)
        # self.grid.place_agent(Ag, (9, 1))
        # self.schedule.add(Ag)
        # self.Entities.add(Ag)
        # # Agent 4
        # Ag = SimpleAgent((9, 0), self)
        # self.grid.place_agent(Ag, (9, 0))
        # self.schedule.add(Ag)
        # self.Entities.add(Ag)

        # no emergent behavior
        self.Entities = set()
        # Agent 1
        Ag = SimpleAgent((6, 0), self)
        self.grid.place_agent(Ag, (6, 0))
        self.schedule.add(Ag)
        self.Entities.add(Ag)
        # Agent 2
        Ag = SimpleAgent((7, 0), self)
        self.grid.place_agent(Ag, (7, 0))
        #Ag = SimpleAgent((9, 2), self)
        #self.grid.place_agent(Ag, (9, 2))
        self.schedule.add(Ag)
        self.Entities.add(Ag)
        # Agent 3
        Ag = SimpleAgent((8, 0), self)
        self.grid.place_agent(Ag, (8, 0))
        self.schedule.add(Ag)
        self.Entities.add(Ag)
        # Agent 4
        Ag = SimpleAgent((9, 0), self)
        self.grid.place_agent(Ag, (9, 0))
        self.schedule.add(Ag)
        self.Entities.add(Ag)

        Ld = Load((0,0), self)
        self.grid.place_agent(Ld, (0, 0))
        self.schedule.add(Ld)
        self.Entities.add(Ld)
        Des = Destination((0,9),self)
        self.grid.place_agent(Des, (0, 9))
        self.schedule.add(Des)
        self.Entities.add(Des)
        self.running = True

    def step(self):
        """
        Have the scheduler advance each cell by one step
        """
        self.schedule.step()

    @staticmethod
    def count_type(model, tree_condition):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for load in model.schedule.agents:
            if load.condition == tree_condition:
                count += 1
        return count


class StandardLoadDeliverGame(Model):
    """
    Represents the 2-dimensional array of cells in Conway's
    Game of Life.
    """
    Entities = set()
    Second_initialization = False
    def __init__(self, height=10, width=10):
        """
        Create a new playing area of (height, width) cells.
        """
        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.
        
        #self.schedule = SimultaneousActivation(self)
        #self.schedule = StagedActivation(self)
        self.schedule = BaseScheduler(self)
        # Use a simple grid, where edges wrap around.
        self.grid = SingleGrid(height, width, torus=True)

        # Place a cell at each location, with some initialized to
        # ALIVE and some to DEAD.
        # for (contents, x, y) in self.grid.coord_iter():
        #     cell = Cell((x, y), self)
        #     if self.random.random() < 0.1:
        #         cell.state = cell.ALIVE
        #     self.grid.place_agent(cell, (x, y))
        #     self.schedule.add(cell)
        self.Entities = set()
        # Agent 1
        Ag = SimpleAgent((9, 0), self)
        self.grid.place_agent(Ag, (9, 0))
        self.schedule.add(Ag)
        self.Entities.add(Ag)
        # Agent 2
        # Ag = SimpleAgent((8, 2), self)
        # self.grid.place_agent(Ag, (8, 2))
        # self.schedule.add(Ag)
        # self.Entities.add(Ag)
        # # Agent 3
        # Ag = SimpleAgent((9, 1), self)
        # self.grid.place_agent(Ag, (9, 1))
        # self.schedule.add(Ag)
        # self.Entities.add(Ag)
        # # Agent 4
        # Ag = SimpleAgent((9, 0), self)
        # self.grid.place_agent(Ag, (9, 0))
        # self.schedule.add(Ag)
        # self.Entities.add(Ag)
        
        Ld = Load((0,0), self)
        self.grid.place_agent(Ld, (0, 0))
        self.schedule.add(Ld)
        self.Entities.add(Ld)
        Des = Destination((0,9),self)
        self.grid.place_agent(Des, (0, 9))
        self.schedule.add(Des)
        self.Entities.add(Des)
        self.running = True

    def step(self):
        """
        Have the scheduler advance each cell by one step
        """
        self.schedule.step()

    @staticmethod
    def count_type(model, tree_condition):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for load in model.schedule.agents:
            if load.condition == tree_condition:
                count += 1
        return count
