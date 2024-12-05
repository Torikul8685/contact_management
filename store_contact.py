import json

def save_contact(contacts):
    with open("contact.json", "w") as file:
        json.dump(contacts, file, indent=4)



def load_contact():
    with open("contact.json", "r") as file:
        return json.load(file)
        
