
class Ship:

    def __init__(self, name: str, size: int) -> None:
        self.name: str = name
        self.size: int = size
        self.health: int = size

    def hit(self):
        self.health -= 1

        if self.health == 0:
            print(f"{self.name} was destroyed!")

    


    