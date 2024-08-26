import json

data = {
    'name' : 'John Doe',
    'age' : 30,
    'occupation' : 'Software Engineer'
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)