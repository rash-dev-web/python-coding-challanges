# file = open("myfile.txt")
# contents = file.read()
# print(contents)
# file.close()

# C:\Users\rashe\PycharmProjects\PythonCodingProjects\Intermediate_codes\file_system
with open("../../../../Desktop/myfile.txt") as file:
    contents = file.read()
    print(contents)

#   ../../../
# /Users/rashe/Desktop/myfile.txt

# with open("myfile.txt", mode="a") as file:
#     file.write("\nthis is a new line added")
