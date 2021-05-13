# 1.interface
# 2.get the meaning
# 3.printing output/modyfying program
import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        if(len(word)>0):
            y=get_close_matches(word,data)
            return ("you mean?:\n"+str(y))
        return("please enter something")

word = input("enter the word:- ")
output = translate(word)
if(type(output) == list):
    for item in output:
        print(">>> "+item)
else:
    print(output)