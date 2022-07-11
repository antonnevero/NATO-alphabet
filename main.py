import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate():
    user_input = input("Enter your name: ").upper()
    try:
        phonetic_code = [code_dict[letter] for letter in user_input]
    except KeyError:
        print("Only letters available")
        generate()
    else:
        print(phonetic_code)


generate()




