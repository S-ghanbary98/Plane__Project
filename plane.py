from aircraft import Aircraft


class Plane(Aircraft):
    def __init__(self, capacity, age, fuel_capacity):
        super().__init__(capacity, age, "PLANE", fuel_capacity)
