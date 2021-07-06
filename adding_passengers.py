def add_passenger(id, name):
    print("sher")
    with open("flight_trips.json", "r+") as read_file:
        data2 = json.load(read_file)
        print(type(data2['flight_trip'][0]['passenger']))

        for i in range(0, len(data2['flight_trip'])):
            print(i)
            if data2['flight_trip'][i]['id'] == id:
                Name = {"name": name}
                data2['flight_trip'][i]['passenger'].append(Name)

                read_file.seek(0)
                json.dump(data2, read_file, indent=4)


add_passenger("W2", "shervs")

