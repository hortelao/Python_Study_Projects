with open("./Input/Names/invited_names.txt", mode="r") as names:
    ind_names = names.readlines()
    for name in ind_names:
        n = name.strip()
        n.replace('\n', "")
        with open("./Input/Letters/starting_letter.txt", mode="r") as start:
            text = start.read()
            txt = text.replace("[name]", f"{n}")
        with open(f"./Output/ReadyToSend/letter_for_{n}", mode="w") as output:
            output.write(txt)
