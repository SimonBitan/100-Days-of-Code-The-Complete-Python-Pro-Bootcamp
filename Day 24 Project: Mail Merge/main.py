# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter_template_file:
    letter_template = letter_template_file.read()
    with open("./Input/Names/invited_names.txt") as names:
        name_list = names.readlines()
        for name in name_list:
            with open(f"./Output/ReadyToSend/{name.strip()}_letter.txt", mode="w") as letter:
                letter.write(letter_template.replace("[name]", f"{name.strip()}"))
