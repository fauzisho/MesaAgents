from .random_agent import SimpleAgent
from .Destination import Destination
from .Load import Load
def portray(agent):

    # Green
    RICH_COLOR = "#46FF33"
    # Red
    POOR_COLOR = "#FF3C33"
    # Blue
    MID_COLOR = "#3349FF"
    portrayal = {}
    # if agent is None:
    #         return
    assert agent is not None
    if type(agent) is Load:
        portrayal["Shape"]= "circle"
        portrayal["w"]= 1
        portrayal["h"]= 1
        portrayal["Filled"]= "true"
        portrayal["Layer"]= 0
        portrayal["x"]= agent.x
        portrayal["y"]= agent.y
        portrayal["Color"]= "green"
    elif type(agent) is SimpleAgent:
        portrayal["Shape"]= "rect"
        portrayal["w"]= 1
        portrayal["h"]= 1
        portrayal["Filled"]= "true"
        portrayal["Layer"]= 0
        portrayal["x"]= agent.x
        portrayal["y"]= agent.y
        portrayal["Color"]= "grey"
    else:
        portrayal["Shape"]= "rect"
        portrayal["w"]= 1
        portrayal["h"]= 1
        portrayal["Filled"]= "true"
        portrayal["Layer"]= 0
        portrayal["x"]= agent.x
        portrayal["y"]= agent.y
        portrayal["Color"]= "black"
        
    return portrayal
def portrayCell(Age):
    """
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the cell in its current state.
    :param cell:  the cell in the simulation
    :return: the portrayal dictionary.
    """
    assert Age is not None
    CellType = {Load: "#00AA00", SimpleAgent: "#880000"}
    # return {
    #     "Shape": "rect",
    #     "w": 1,
    #     "h": 1,
    #     "Filled": "true",
    #     "Layer": 0,
    #     "x": cell.x,
    #     "y": cell.y,
    #     "Color": "red",
    # }
    portrayal = {}
    if type(Age) is Load:
        portrayal["Shape"]= "rect"
        portrayal["w"]= 1
        portrayal["h"]= 1
        portrayal["Filled"]= "true"
        portrayal["Layer"]= 0
        portrayal["x"]= Age.x
        portrayal["y"]= Age.y
        portrayal["Color"]= "green"
    if type(Age) is SimpleAgent:
        portrayal["Shape"]= "rect"
        portrayal["w"]= 1
        portrayal["h"]= 1
        portrayal["Filled"]= "true"
        portrayal["Layer"]= 0
        portrayal["x"]= Age.x
        portrayal["y"]= Age.y
        portrayal["Color"]= "grey"
    if type(Age) is Destination:
        portrayal["Shape"]= "rect"
        portrayal["w"]= 1
        portrayal["h"]= 1
        portrayal["Filled"]= "true"
        portrayal["Layer"]= 0
        portrayal["x"]= Age.x
        portrayal["y"]= Age.y
        portrayal["Color"]= "red"
        
    return portrayal
