# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("./nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(dict)
# {"A": "Alfa", "B": "Bravo"}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your word").upper()
word = [x for x in word]
answer = [dict[letter] for letter in word]
print(answer)
