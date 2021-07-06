import json
class FileOpenHandling:
    def parse(self, xfile):
        try:
            with open(xfile, "r") as content: # open file into contents variable
                exchange = json.load(content) # JSON object as dictionary
                rates = exchange["rates"][country]
                return rates
        except FileNotFoundError as err:
            return "File not found"
        except KeyError as err:
            return "Bad country code"

    def list(self, xfile):
        try:
            with open(xfile, "r") as content: # open file into contents variable
                exchange = json.load(content)  # JSON object as dictionary
                rates = exchange["rates"]
                for key in rates.keys():
                    print(key)
                return
        except FileNotFoundError as err:
            return "File not found"