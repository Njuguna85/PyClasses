import json

# the diff libraary checks for sequences of characters
from difflib import get_close_matches

"""
    The following program is a dictionary implemented
    on the command prompt
"""


# open the file and load it using json loads
data = json.load(open("data.json"))

# a function with an argument and returns is values from the dictionary of data


def meaning(search_word):

    # Convert to all small case
    search_word = search_word.lower()

    # search if the word is in data dictionary
    if search_word in data:
        return data[search_word]

    # Convert to Title for word such as Nairobi
    elif search_word.title() in data:
        return data[search_word.title()]

    # Convert to all Upper case for words such as UN
    elif search_word.upper() in data:
        return data[search_word.upper()]

    elif len(get_close_matches(search_word, data.keys())) > 0:
        yn = input("Did you mean %s instead ?\nEnter Y if yes or N for no: " %
                   get_close_matches(search_word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(search_word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please Check it again"
        else:
            return "We didn't get your input"
    else:
        return "The word doesn't exist. Please Check it again"


# Will allow the user to input sth and convert it to a string
search_word = str(input("Type in the word to be searched: "))

# pass the searchword variable to the function and print its
output = meaning(search_word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
