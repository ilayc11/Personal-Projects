PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    namesList=names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letterContents = letter.read()
    for name in namesList:
        strippedName = name.strip()
        new_letter=letterContents.replace(PLACEHOLDER,strippedName)
        with open(f"./Output/ReadyToSend/letterFor{strippedName}.txt",mode='w') as completeLetter:
            completeLetter.write(new_letter)