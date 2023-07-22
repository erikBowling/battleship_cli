import string
import re

from tabulate import tabulate

from modules.grid import Grid
from modules.cell import Cell

def main():
    game_board_object: Grid = Grid()

    playing: bool = True
    turns_left: int = 30
    while playing:
        print_board(game_board_object)

        cell_to_hit: str = input(f"REMAINING SHOTS: {turns_left} CELL: ")

        if cell_to_hit == "bb":
            break

        if re.fullmatch('[a-jA-J]([1-9]|10)', cell_to_hit) is None:
            print("INVALID CELL")
            continue
        
        game_board_object.cell_hit(cell_to_hit)

        turns_left -= 1
        if turns_left <= 0:
            playing = False
            print(f"REMAINING SHOTS: {turns_left}")
            print("Game over")

def print_board(game_board_object: Grid) -> None:
    grid_letters: list[str] = list(string.ascii_lowercase[:10])
    grid_letters.insert(0, "row")
    display_grid: list[list[Cell]] = [grid_letters]

    for row_num, row in enumerate(game_board_object.grid):
        display_row: list[Cell] = [row_num + 1]
        for cell in row:
            if cell.hit_status:
                if cell.occupied:
                    display_row.append("O")
                else:
                    display_row.append("X")
            else:
                display_row.append("_")
        
        display_grid.append(display_row)

    print(tabulate(display_grid))

main()