from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from .portrayal import portrayCell, portray
from .model import LoadDeliverGame,StandardLoadDeliverGame


# Make a world that is 50x50, on a 250x250 display.
canvas_element = CanvasGrid(portrayCell, 10, 10, 500, 500)

server = ModularServer(
    LoadDeliverGame, [canvas_element], "Load and Deliver Agents", {"height": 10, "width": 10}
)
