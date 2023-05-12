import pandas
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
user_input = input("What to transform? ").upper()

user_letters = [letter for letter in user_input]

nato = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

nato_final = [nato[letter] for letter in user_letters]
print(nato_final)

