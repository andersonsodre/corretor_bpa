import codecs
types_of_encoding = ["utf8", "cp1252"]
# creating a variable and storing the text
# that we want to search
search_text = "010                                65000000"


# creating a variable and storing the text
# that we want to add
replace_text = "010                                65090000"

for encoding_type in types_of_encoding:
    # Opening our text file in read only
    # mode using the open() function
    with codecs.open(r'PA_SORRIR2022.ABR', 'r', encoding='utf8') as file:
        # Reading the content of the file
        # using the read() function and storing
        # them in a new variable
        data = file.read()

        # Searching and replacing the text
        # using the replace() function
        data = data.replace(search_text, replace_text)

    # Opening our text file in write only
    # mode to write the replaced content
    with codecs.open(r'PA_SORRIR2022.ABR', 'w', encoding='utf8') as file:
        # Writing the replaced data in our
        # text file
        file.write(data)

    # Printing Text replaced
    print("CORRIGIDO PRA 081")

