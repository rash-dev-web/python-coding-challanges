# TODO: Create a letter using starting_letter.docx
with open("./Input/Letters/starting_letter.docx") as file:
    contents = file.read()
    print(contents)

# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()
print(names)

for name in names:
    user_name = name.strip()
    with open(f"./Output/ReadyToSend/{user_name}.docx", mode="w") as file:
        # contents.replace("[name]", user_name)
        file.write(contents.replace("[name]", user_name))
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
