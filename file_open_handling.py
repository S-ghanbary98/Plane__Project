import json
class FileOpenHandling:
    def parse(self, xfile):
        try:
            with open(xfile, "r") as content: # open file into contents variable
                file = json.load(content) # JSON object as dictionary
                return file
        except FileNotFoundError as err:
            return "File not found"
        except KeyError as err:
            return "wrong number input"

    def list_flight_number(self, xfile):
        try:
            with open(xfile, "r") as content: # open file into contents variable
                file = json.load(content)  # JSON object as dictionary

                flight_number = file["flight"]
                for key in flight_number:
                    print(flight_number[0]["flight_number"])
                return
        except FileNotFoundError as err:
            return "File not found"