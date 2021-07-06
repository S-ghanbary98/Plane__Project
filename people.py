from airport import Airport


class People(Airport):

    def __init__(self):
        super().__init__()

    def name(self):
        return "Name"

    def tax_code(self):
        return "Tax Code"

    def id_number(self):
        return "ID Number"


people = People()
