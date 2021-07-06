import json

## Creates a passanger and adds passenger info to database

def create_passenger(first_name, last_name, passport_number, age,):
    new_passenger = {'passport': passport_number, 'fName': first_name.lower(), 'lName': last_name.lower(), 'age': age}

    if age <= 2:
        pass
    # Some function to not reduce seat number
    ## Reads, Updates and Closes json file

    with open("passengers.json", "r+") as read_file:
        data = json.load(read_file)
        data["passenger"].append(new_passenger)
        read_file.seek(0)
        json.dump(data, read_file, indent = 4)



def add_flight_details(dictionary, flight)

with open("flightID.json.", "r+") as read_file:
    data = json.load(read_file)
    print(data)
    print(data['flight'])


with open("passengers.json", "r+") as read_file:
    data = json.load(read_file)
    dataa = data["passenger"][0]
    dataa["red"] = "red"
    print(dataa)