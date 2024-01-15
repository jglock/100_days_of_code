import pandas

#TODO 1. Create a dictionary in this format:
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


while True:
    name = input("Enter a word: ").upper()

    print([alphabet[alphabet['letter']== character]['code'].values[0] for character in name])

    if name == "END":
        break
        