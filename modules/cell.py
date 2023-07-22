from modules.ship import Ship

class Cell:

    def __init__(self, id: str, coordinates: list[int, int]) -> None:
        self.id: str = id
        self.hit_status: bool = False
        self.grid_coordinates: list[int, int] = coordinates
        self.occupied: bool = False
        self.occupied_ship: Ship | None = None


    def hit(self):
        self.hit_status = True
        
        if self.occupied:
           print("Hit!!")
           self.occupied_ship.hit()
        else:
           print("Miss!!")

    def populate_ship(self, ship: Ship) -> None:
        self.occupied_ship = ship
        self.occupied = True

        
