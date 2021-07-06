from people import People


class FlightTrip(Aircraft, People):

    def __init__(self):
        super().__init__()

    def destination(self):
        return "Destination"

    def flight_duration(self):
        return "Flight Duration"

    def origin(self):
        return "Origin"

    def passengers(self):
        return "Passengers"


flight = FlightTrip()
