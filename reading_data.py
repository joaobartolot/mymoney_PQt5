import json

def load():
    with open('database.json') as f:
        data = json.load(f)
    return data

def register(username, password, name):
        data = load()

        data['users'].append([username, password, name])

        with open('database.json', 'w') as f:
            json.dump(data, f, indent=4, sort_keys =True)
