import json


# Function to change flight trip details
def manage_flight_trips(flight_id, destination, origin, vehicle, duration, passenger_id, seat):
    flight_trp = flight_id
    # Open json file as read only to get a dict
    with open("flight_trips.json", "r") as file:
        json_file = json.load(file)
        flights_json = json_file["flight_trip"]

        # Iterate through dict to see if flight id is the same as what was inputted
        for flight in flights_json:
            # If there's a flight with the same id, change the details
            if flight["id"] == flight_trp:
                flight["destination"] = destination
                flight["origin"] = origin
                flight["vehicle"] = vehicle
                flight["duration"] = duration

                # Iterate through the passengers of the flight
                for passenger in flight["passenger"]:
                    # If there's a passenger with the same id, change details
                    if passenger["passport"] == passenger_id:
                        passenger["seat"] = seat

                # Write changes to the json file
                with open("flight_trips.json", "w") as f:
                    json.dump(json_file, f)  # serializing back to the original file


# User input
manage_flight_trips("W1", "Greece", "USA", "Helicopter", "120", "1445543LB", "5A")
