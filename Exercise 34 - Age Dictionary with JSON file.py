# Edit an Age Dictionary by loading a JSON file.


import json

age_dictionary = {
    "Christopher": "20",
    "Andreen": "24",
    "Kyle": "26",
    "Rich": "31",
    "Chad": "18",
    "Jawn": "27",
    "Kelly": "45",
    "Jhene": "21",
    "Carlos": "49",
    "Michael": "61",
    "Tevin": "23",
    "Lisa": "43",
    "Wes": "33",
    "Dennis": "10",
    "Aiden": "15",
    "Audrey": "30",
    "Francis": "20",
    "Sammy": "19"

}


with open('ages.json', 'w') as ag:
    json.dump(age_dictionary, ag)


def add_entry():
    name = input('Who do you want to add to the Age Dictionary?\n')
    date = input(f'How old is {name}?\n')
    age_dictionary[name] = date
    with open('ages.json', 'w') as ae:
        json.dump(age_dictionary, ae)
    print(f'{name} was added to your Age Dictionary.\n')


def find_date():
    name = input("Who's age do you want to know?\n")
    try:
        if age_dictionary[name]:
            print(f'{name} is {age_dictionary[name]} years old.\n')
    except KeyError:
        print(f'{name} is not in the list.\n')


def list_entries():
    print('The current entries in my birthday list are:\n')
    for key in age_dictionary:
        print(key.ljust(15), ':', age_dictionary[key])
    print()


while True:
    what_next = input('What do you want to do next? You can: Add, Find, List or Quit\n')
    if what_next == 'Quit':
        print('Goodbye.')
        raise SystemExit(0)
    elif what_next == 'Add':
        add_entry()
    elif what_next == 'Find':
        find_date()
    elif what_next == 'List':
        list_entries()
