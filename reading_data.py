import json

def load():
    with open('database.json') as f:
        data = json.load(f)
    return data

def register(name, username, password):
    data = load()

    data['users'].append(
            {
                'name': name,
                'username': username,
                'password': password
            }
        )

    with open('database.json', 'w') as f:
        json.dump(data, f, indent=2)

def new_account(identification, balance = 0, account_type):
    pass
