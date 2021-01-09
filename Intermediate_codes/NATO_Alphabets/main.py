# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data_dict = {
#     "letter": data.letter.to_list(),
#     "code": data.code.to_list()
# }
# data_frame = pandas.DataFrame(data_dict)
# for (index, row) in data_frame.iterrows():
#     alphabet_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(alphabet_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# one way of implementation without function
# do_continue = True
# while do_continue:
#     user_input = input("Enter your name: ").upper()
#     try:
#         user_name_list = [alphabet_dict[letter] for letter in user_input]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#     else:
#         print(user_name_list)
#         do_continue = False

# with function
def generate_phonetic():
    user_input = input("Enter your name: ").upper()
    try:
        user_name_list = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(user_name_list)


generate_phonetic()
