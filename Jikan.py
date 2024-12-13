import json

# Open and load the JSON file
with open('Jikan.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)
print(data)

## print all anime that have a score greater than 9.0

for score in Jikan["score"]:
    if score <= 9:
        print(titles["title_english"])


## Print all anime that stopped airing before 2015

for anime in Jikan["aired"]:
    
    if "year" <= 2015:
        print("title")