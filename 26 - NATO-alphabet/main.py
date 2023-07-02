import pandas
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}


def generate():
    user_input = input("What to transform? ").upper()
    try:
        nato_final = [nato[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please... (No special characters or numbers)")
        generate()
    else:
        print(nato_final)

generate()