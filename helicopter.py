from aircraft import Aircraft


class Helicopter(Aircraft):
    def __init__(self, capacity, age, fuel_capacity):
        super().__init__(capacity, age, "HELICOPTER", fuel_capacity)
