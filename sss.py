import json
identity = open("passengers.json", "r")
id = json.load(identity)
id2 =id["passenger"][0]["fName"]
print(id2)

def identity_checker():
    fname_prompt = input("What is your first name? ").capitalize()






print(identity_checker())
def id_check():
    fname_prompt = input("What is your first name? ").capitalize()
    for fname_prompt in id:
        if fname_prompt["passenger"] == "fName":
            return "success"
        else:
            return "fail"
print(id_check())