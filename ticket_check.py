import json
import os
tickets = open("passenger_records.json", "r")
tick_count = json.load(tickets)

# print(tick_count["Tickets"])
def passenger_prices():
    with open("passenger_records.json", "r") as tickets:
        tick_count = json.load(tickets)
    ticket_price = int(input("How much is the regular ticket? "))
    age = int(input("How old is the passenger? "))
    total_tickets = tick_count["tickets"]
    if age <= 2:
        if total_tickets > 0:
            print(f"There are {total_tickets} tickets remaining")
            infant_ticket = ticket_price / 3
            return f"The price of the infant ticket is £{infant_ticket}"
    elif 2 < age <= 12:
        child_ticket = ticket_price / 2
        tick_count["tickets"] -= 1
        tickets.seek(0)
        json.dump(tick_count, tickets , indent=4)
        print(f"There are {total_tickets} tickets remaining")
        return f"The price of a child ticket is £{child_ticket}"
    # else:
        return f"The price of a regular ticket is £{ticket_price}"
print(passenger_prices())