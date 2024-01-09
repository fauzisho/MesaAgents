from mesa import Agent
import math
from Models.Load import Load
from Models.Destination import Destination

class SimpleAgent(Agent):
    _load = False
    _myLoads = list()
    entities = set()
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.entities = model.Entities
        self.x, self.y = pos
        self.Loaded = False
    def get_neighbours(self,grid_length, grid_width):
        neighbours = set()
        if(not self.pos[0]+1 >= grid_width):
            neighbours.add((self.pos[0]+1,self.pos[1]))
        if(not self.pos[0]-1 < 0):
            neighbours.add((self.pos[0]-1,self.pos[1]))
        if(not self.pos[1]+1 >= grid_length):
            neighbours.add((self.pos[0],self.pos[1]+1))
        if(not self.pos[1]-1 < 0):
            neighbours.add((self.pos[0],self.pos[1]-1))
        neighbours.add((self.pos[0],self.pos[1]))
        return list(neighbours)
    def NeighbourCellsCheck(self ):
        # Pick the next cell from the adjacent cells.
        #next_moves = self.model.grid.get_neighborhood(self.pos, False, False)
        next_moves = self.get_neighbours(self.model.grid.height,self.model.grid.width)
        #for move in next_moves:
            #"""Don't move from the edge of the grid to the other edge (behind the grid)"""
            # if(((move[1] == self.pos[1] and abs(move[0] - self.pos[0]) != 1 ) 
            # or (move[0] == self.pos[0] and  abs(move[1] - self.pos[1]) != 1))):
            # #or (move[0] == self.pos[0] and move[0] == self.pos[1])):
            #     next_moves.remove(move)
        for move in list(next_moves):
            if (not self.model.grid.is_cell_empty((move[0],move[1]))) and (not (move[0] == self.pos[0] and move[1] == self.pos[1])):
                """Check if the neighbour cells do not hold agents"""
                if(type(self.model.grid[move[0],move[1]]) != Destination):
                    next_moves.remove(move)
        return next_moves
    def ClosestDestination(self,agent,entities):
        """This Funtion returns the the closest destination to a given position ( assumting that the 
        given position is an interested agent"""
        Destinations = list(filter(lambda x: type(x) is Destination, entities))
        distance = -1
        for destination in Destinations:
            if distance == -1:
                target_destination = destination
                distance = self.DistanceCaluclation(agent.pos, destination.pos)
            elif (self.DistanceCaluclation(agent.pos, destination.pos) <= distance):
                target_destination = destination
                distance = self.DistanceCaluclation(agent.pos, destination.pos)
        return target_destination
    def ClosestLoad(self, agent, entities):
        """This Funtion returns the the closest load to a given position ( assumting that the 
        given position is an interested agent"""
        Loads = list(filter(lambda x: type(x) is Load, entities))
        distance = -1
        for load in Loads:
            if distance == -1:
                target_load = load
                distance = self.DistanceCaluclation(agent.pos, load.pos)
            elif (self.DistanceCaluclation(agent.pos, load.pos) <= distance):
                target_load = load
                distance = self.DistanceCaluclation(agent.pos, load.pos)
        return target_load
    def DistanceCaluclation(self, first_pos, second_position):
        """Function that calculates the shortest distance between two given entities (agents, loads, destinaitons..,"""
        # first_pos = first_entity.pos
        # second_position= second_entity.pos
        x = pow(first_pos[0] - second_position[0],2)
        y = pow(first_pos[1] - second_position[1],2)
        distance = math.sqrt( x + y)
        return distance
        
    def move_toward(self, target_position,next_moves):
        distance = -1
        for move in next_moves:
            if distance == -1:
                next_move = move
                distance = self.DistanceCaluclation(target_position, (move[0],move[1]))
            elif (self.DistanceCaluclation(target_position, (move[0],move[1])) <= distance):
                next_move = move
                distance = self.DistanceCaluclation(target_position, (move[0],move[1]))
        if len(next_moves) == 0:
            return self.pos
        else:
            return next_move
        #return next_move

    def ShortDistance(StartPos, EndPos):
        pass
    def PickUp(self):
        return
    #def Move(self):
    def step(self):
        """
        Step one cell in any allowable direction.
        """
        #next_moves = self.NeighbourCellsCheck()
        #ag = self.NeighbourCellsCheck(next_moves, self.entities)
        current_pos = self.pos
        if(self._load == True):
            """---------Moving toward the destination--------------"""
            target_destination = self.ClosestDestination(self, self.entities)
            DestinationPosition = (target_destination.pos[0], target_destination.pos[1])
            next_moves = self.NeighbourCellsCheck()
            next_move = self.move_toward(DestinationPosition,next_moves)
            
        target_load = self.ClosestLoad(self, self.entities)
        LoadingPosition = (target_load.pos[0], target_load.pos[1] + 1)
        if(self._load == False):
            """---------Moving toward the load--------------"""
            """After filtering possible moves, choose the closest move to the closes load"""
            next_moves = self.NeighbourCellsCheck()
            next_move = self.move_toward(LoadingPosition,next_moves)

        #next_move = self.random.choice(next_moves)
        # Now move:
        try:
            self.model.grid.move_agent(self, next_move)
            if(self._load == True and current_pos != self.pos):
                """Drage the load with you"""
                my_load = self._myLoads[0]
                self.model.grid.move_agent(my_load, current_pos)
            # if(self._load == True and current_pos == self.pos):
            #     """Reset everything if you reach destination"""
            #     self.model.__init__()
            #     self.model.steps = 0
            #     self.model.time = 0
            
        except BaseException as e:
            print("No place to move to")
        if(self.pos[0] == LoadingPosition[0] and self.pos[1] == LoadingPosition[1] ):
                self._load = True
                self._myLoads.append(target_load)

       
    def Drop(self):
        pass