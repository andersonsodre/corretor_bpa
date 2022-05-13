import codecs


types_of_encoding = ["utf8", "cp1252"]


mylist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z']
for x in range(0, len(mylist)):
    conjunto = "999"
    dados = mylist[x]
    conjunto2 = (conjunto + dados)
    search_text = conjunto2
    replace_text = ("081" + dados)
    for encoding_type in types_of_encoding:
        # Opening our text file in read only
        # mode using the open() function
        with codecs.open(r'PA_SORRIR2022.ABR', 'r', encoding='utf8') as file:
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