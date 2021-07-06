
def passenger_prices():
    ticket_price = int(input("How much is the regular ticket? "))
    age = int(input("How old is the passenger? "))
    if age <= 2:
        infant_ticket = ticket_price / 3
        return f"The price of the infant ticket is £{infant_ticket}"
    elif 2 < age <= 12:
        child_ticket = ticket_price / 2
        return f"The price of a child ticket is £{child_ticket}"
    else:
        return f"The price of a regular ticket is £{ticket_price}"
print(passenger_prices())
print(passenger_prices())
print(passenger_prices())