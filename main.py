from display import *
from draw import *
from parserp import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'dwscript', edges, polygons, transform, screen, color )
