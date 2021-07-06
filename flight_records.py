import json
identity = open("passenger_records.json", "r")
id = json.load(identity)
id2 =id["passenger"][0]["fName"]
print(id2)
def identity_checker():
    fname_prompt = input("What is your first name? ").capitalize()
    if fname_prompt in id2[1]:
        return "Success"
    else:
        return "Fail"

# print(identity_checker())