import json

def flight_attendees_list_report():
    identity = open("passenger_records.json", "r")
    id = json.load(identity)
    for value, key in id.items():
        if not isinstance(key, list):
            for x, y in key.items():
                print(x,':', y)
        else:
            for i in key:
                for s, m in i.items():
                    print(s,':', m)
print(flight_attendees_list_report())