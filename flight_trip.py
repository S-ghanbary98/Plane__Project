
def print_options_flight():
    # Print flight options
    print("Flight Options")
    print("--------------")
    print("1. New flight")
    print("2. Existing Flight")
    print("")
    return get_flight()

# Choose existing flight or new flight
def get_flight():
    # Get origin choice
    while True:
        try:
            choice = int(input("Please choose an option "))
            if (choice < 1) or (choice > 2):
                print("Please select a choice between 1 and 2.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            return choice

def get_flight_info(choice):
    # Use numeric choice to look up destination info
    # New flight
    if (choice == 1):
        return create_flight()

    # Choice 2: Existing Flight
    elif (choice == 2):
        return check_flight()

def create_flight():
    pass

def check_flight():
    from file_open_handling import FileOpenHandling
    xfile = "flight_records.json"
    readf = FileOpenHandling()
    record = readf.list_flight_number(xfile)
    return record



# provides information about European destinations
def print_options_destinations():
    # Print travel options
    print("Travel Options")
    print("--------------")
    print("1. Rome")
    print("2. Berlin")
    print("3. Vienna")
    print("4. London")
    print("")
    return get_origin()

def get_origin():
    # Get origin choice
    while True:
        try:
            choice = int(input("Where is the flight from? "))
            if (choice < 1) or (choice > 4):
                print("Please select a choice between 1 and 4.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            return choice

def get_destination():
    # Get destination choice
    while True:
        try:
            choice = int(input("Where would you like to go? "))
            if (choice < 1) or (choice > 4):
                print("Please select a choice between 1 and 4.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            return choice

def get_destination_info(choice):
    # Use numeric choice to look up destination info

    if (choice == 1):
        return "Rome"

    # Choice 2: Berlin
    elif (choice == 2):
        return "Berlin"

    # Choice 3: Vienna
    elif (choice == 3):
        return "Vienna"

    # Choice 3: Vienna
    elif (choice == 4):
        return "London"

def get_duration():
    try:
        time = int(input("How long is the flight in minutes? "))
    except ValueError:
        print("The value you entered is invalid. Only numerical values are valid.")
    else:
        return time

def get_flight_id():
    try:
        id = int(input("Put a flight ID "))
    except ValueError:
        print("The value you entered is invalid. Only numerical values are valid.")
    else:
        return id

def check_id_exist(flight_ids_list, flight_id):

    for flight in flight_ids_list["flight"]:
        print(flight["flight_number"])
        if flight_id == flight["flight_number"]:
            return True
        else:
            return False

origin = print(get_destination_info(print_options_destinations()))
destination = print(get_destination_info(get_destination()))
duration = print(get_duration())
flight_ids_list = get_flight_info(print_options_flight())
flight_id = get_flight_id()
print(check_id_exist(flight_ids_list, flight_id))






# from people import People
#
#
# class FlightTrip(Aircraft, People):
#
#     def __init__(self):
#         super().__init__()
#
#     def destination(self):
#         return "Destination"
#
#     def flight_duration(self):
#         return "Flight Duration"
#
#     def origin(self):
#         return "Origin"
#
#     def passengers(self):
#         return "Passengers"
#
#
# flight1 = FlightTrip()

