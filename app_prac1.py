import json

from difflib import get_close_matches

data=json.load(open("data.json",'r'))

def return_meaning(key):
    key=key.lower()
    if key in data:
      return data[key]
    elif key.title() in data:
        return data[key.title()] #converts first letter to uppercase and all the others to lowercase
    elif len(get_close_matches(key,data.keys(),cutoff=0.8))>0:
        item=get_close_matches(key,data.keys(),cutoff=0.8)[0]
        result=input("Did you mean %s instead? Enter Y if yes or N if no: "%item)
        if result=="Y":
            return data[item]
        elif result=="N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word=input("Enter a word:")

output=return_meaning(word)

if type(output)==list:
    for s in output:
        print(s)
else:
    print(output)
