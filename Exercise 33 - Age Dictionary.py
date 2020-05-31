# Age Dictionary

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

print("Welcome to your age dictionary. We have the ages of: ")
for name in age_dictionary:
    print(name)

try:
    request = input("\nWho's age do you want to see?: ")
    print(f"{request} is {age_dictionary[request]} years old.")
except KeyError:
    print("I don't have the age of this person.")
