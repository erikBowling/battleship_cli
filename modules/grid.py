import string
import random

from modules.cell import Cell
from modules.ship import Ship

ships_dict: dict[str, int]= {
            "Carrier": 5,
            "Battleship": 4,
            "Cruiser": 3,
            "Submarine": 3,
            "Destroyer": 2
        }

class Grid:
    
    def __init__(self) -> None:
        self.grid: list[list[Cell]] = []
        self.ships: list[Ship] = [Ship(ship, ships_dict[ship]) for ship in ships_dict]

        self.__populate_grid_cells()
        self.__populate_grid_ships()

    def __populate_grid_cells(self) -> None:
        grid_numbers: list[int] = [i for i in range(1, 11)]
        grid_letters: list[str] = list(string.ascii_lowercase[:10])

        for row, num in enumerate(grid_numbers):
            grid_row: list[Cell] = []
            for col, letter in enumerate(grid_letters):
                grid_row.append(Cell(f"{letter}{num}", [row, col]))
            
            self.grid.append(grid_row)

    def __populate_grid_ships(self) -> None:
        directions: list[str] = ["horizontal", "vertical"]

        # Loop through the ship types
        for ship in self.ships:

            # Find a random cell to start with, and validate the ship will fit
            while True:
                ship_direction: str = random.choice(directions)
                location_cell: Cell = random.choice(random.choice(self.grid))
                
                # Validate
                if ship_direction == "vertical":
                    valid = self.__validateVertical(location_cell, ship)
                else:
                    valid = self.__validateHorizontal(location_cell, ship)

                if valid:
                    break

    def __place_ship(self, ship: Ship, direction: str, starting_cell_coordinates: list[int, int]) -> None:
        if direction == "left":
            for index in range(ship.size):
                self.grid[starting_cell_coordinates[0]][starting_cell_coordinates[1] - index].populate_ship(ship)

        elif direction == "up":
            for index in range(ship.size):
                self.grid[starting_cell_coordinates[0] - index][starting_cell_coordinates[1]].populate_ship(ship)

        elif direction == "right":
            for index in range(ship.size):
                self.grid[starting_cell_coordinates[0]][starting_cell_coordinates[1] + index].populate_ship(ship)

        elif direction == "down":
            for index in range(ship.size):
                self.grid[starting_cell_coordinates[0] + index][starting_cell_coordinates[1]].populate_ship(ship)

    def __validateVertical(self, starting_cell: Cell, ship: Ship) -> bool:
        valid_list: list[bool] = [True, True]
        up_or_down: list[str] = ["up", "down"]

        for direction in range(2):
            # Check up
            if direction == 0:
                if starting_cell.grid_coordinates[0] - (ship.size - 1) >= 0:
                    for i in range(ship.size):
                        if self.grid[starting_cell.grid_coordinates[0] - i][starting_cell.grid_coordinates[1]].occupied:
                            valid_list[direction] = False
                            break
                else:
                    valid_list[direction] = False

            # Check Down
            if direction == 1:
                if starting_cell.grid_coordinates[0] + (ship.size - 1) <= 9:
                    for i in range(ship.size):
                        if self.grid[starting_cell.grid_coordinates[0] + i][starting_cell.grid_coordinates[1]].occupied:
                            valid_list[direction] = False
                            break
                else:
                    valid_list[direction] = False

        
        # If both valid, pick a random direction
        if valid_list[0] and valid_list[1]:
            self.__place_ship(ship, random.choice(up_or_down), starting_cell.grid_coordinates)
            return True
        
        # Up
        elif valid_list[0] and not valid_list[1]:
            self.__place_ship(ship, up_or_down[0], starting_cell.grid_coordinates)
            return True
        
        # Down
        elif not valid_list[0] and valid_list[1]:
            self.__place_ship(ship, up_or_down[1], starting_cell.grid_coordinates)
            return True
        
        # Not valid
        else:
            return False

    def __validateHorizontal(self, starting_cell: Cell, ship: Ship) -> bool:
        valid_list: list[bool] = [True, True]
        left_or_right: list[str] = ["left", "right"]

        for direction in range(2):
            # Check left
            if direction == 0:
                if starting_cell.grid_coordinates[1] - (ship.size - 1) >= 0:
                    for i in range(ship.size):
                        if self.grid[starting_cell.grid_coordinates[0]][starting_cell.grid_coordinates[1] - i].occupied:
                            valid_list[direction] = False
                else:
                    valid_list[direction] = False


            # Check right
            if direction == 1:
                if starting_cell.grid_coordinates[1] + (ship.size - 1) <= 9:
                    for i in range(ship.size):
                        if self.grid[starting_cell.grid_coordinates[0]][starting_cell.grid_coordinates[1] + i].occupied:
                            valid_list[direction] = False
                else:
                    valid_list[direction] = False


        # If both valid, pick a random direction
        if valid_list[0] and valid_list[1]:
            self.__place_ship(ship, random.choice(left_or_right), starting_cell.grid_coordinates)
            return True
        
        # Left
        elif valid_list[0] and not valid_list[1]:
            self.__place_ship(ship, left_or_right[0], starting_cell.grid_coordinates)
            return True
        
        # Right
        elif not valid_list[0] and valid_list[1]:
            self.__place_ship(ship, left_or_right[1], starting_cell.grid_coordinates)
            return True
        
        # Not valid
        else:
            return False
        
    def cell_hit(self, id: str) -> None:
        col: str = id[0]
        row: int = int(id[1:])

        col = col.upper()

        self.grid[row - 1][ord(col)-65].hit()