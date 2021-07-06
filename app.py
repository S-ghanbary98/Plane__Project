import json


def manage_flight_trips(flight_id, destination):
    flight_trp = flight_id
    with open("flight_trips.json", "r") as file:
        json_file = json.load(file)
        flights_json = json_file["flight_trip"]
        for flight in flights_json:
            if flight["id"] == flight_trp:
                flight["destination"] = destination
                print(flight["destination"])

                with open("flight_trips.json", "w") as f:
                    json.dump(json_file, f)  # serializing back to the original file


manage_flight_trips("W2", "Poland")
