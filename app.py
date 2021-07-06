import json


# Function to change flight trip details
def manage_flight_trips(flight_id, destination):
    flight_trp = flight_id
    # Open json file as read only to get a dict
    with open("flight_trips.json", "r") as file:
        json_file = json.load(file)
        flights_json = json_file["flight_trip"]

        # Iterate through dict to see if flight id is the same as what was inputted
        for flight in flights_json:
            if flight["id"] == flight_trp:
                # If there's a flight with the same id, change the details
                flight["destination"] = destination
                print(flight["destination"])

                # Write changes to the json file
                with open("flight_trips.json", "w") as f:
                    json.dump(json_file, f)  # serializing back to the original file


# User input
manage_flight_trips("W2", "Poland")
