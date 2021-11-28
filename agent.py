#!usr/bin/env python

"""
agent.py: does stuff
"""

__author__ = "Max Hariri-Turner"
__email__ = "maxkht8@gmail.com"

import logging
from board import Board

# Constants
LOG_NAME = "agent"
ROWS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
FLEET_TEMPLATE = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
ORIENTATIONS = {'V': 0, 'H': 1}
SIZE = 10


class Agent:
    TYPE_PLAYER = 0

    def __init__(self, agent_type):
        self.agent_type = agent_type
        self.fleet_data = Board()
        self.enemy_data = Board()
        if self.agent_type is Agent.TYPE_PLAYER:
            self.name = input("Please enter your name: ")
        self.fleet_deployed = False

    def take_turn(self):
        if not self.fleet_deployed and self.agent_type is Agent.TYPE_PLAYER:
            self.player_deploy_fleet()

    def player_deploy_fleet(self):
        for ship_name, ship_length in FLEET_TEMPLATE.items():
            valid = False
            while not valid:
                print("Deploy your fleet by entering the row [A-J] column [1-10], and orientation (v, h)")
                print("For example, \'B4, v\' would place the ship vertically starting at square B4")
                self.fleet_data.display()
                print(f"Current ship: {ship_name}")
                line = input("Desired location: ")
                if line is None or len(line) < 5 or line.find(", ") == -1:
                    print("Invalid; bad syntax")
                    continue
                row = line[0]
                split = line.find(", ")
                col = line[1:split]
                ori = line[-1:]
                # print(f"Rows? {row.upper() in ROWS}")
                # print(f"Cols? {int(col) in range(SIZE)}")
                # print(f"Orientation? {ori.upper() in ORIENTATIONS}")
                if row.upper() not in ROWS or int(col) not in range(SIZE) or ori.upper() not in ORIENTATIONS.keys():
                    print("Invalid; that input values not in range")
                else:
                    print("Valid values")
                    target_cells = []
                    initial_x = ROWS.get(row.upper())
                    initial_y = col
                    dx = ORIENTATIONS.get(ori.upper())
                    dy = 1 - dx
                    for i in range(ship_length):
                        cell = self.fleet_data.get(initial_x + i * dx, initial_y + i * dy)
                        target_cells.append()
                    all_cells_empty = True
                    for cell in target_cells:
                        if cell.




