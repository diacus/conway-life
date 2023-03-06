import os
import random
from time import sleep

from life import World


random.seed()
world = (
    World()
    .set_height(50)
    .set_width(140)
    .set_population(1200)
    .generate_board()
)

try:

    while world.has_life():
        os.system("clear")
        print(world)
        world = world.generate_next_board_configuration()
        sleep(0.2)
        os.system("clear")

    print(world)
    print("there is no live now")

except KeyboardInterrupt:
    print("bye")
