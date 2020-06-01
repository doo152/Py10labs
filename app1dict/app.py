import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Do you mean %s instead? Enter Y if yes, or N for no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return  "The word does not exist. Please double check it."
        else: 
            return "We don't understand what you are talking about! "
    else:
        return "The word does not exist. Please double check it."

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    
    for item in output:
        print(item)
else: 
    print(output) 
