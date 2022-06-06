import codecs
types_of_encoding = ["utf8", "cp1252", 'Latin-1']
# creating a variable and storing the text
# that we want to search

# CEP including
ceps = ['789', '099', '480', '062', '507', '031', '005', '039', '079', '008', '653', '092', '067', '000',
        '101', '094', '698', '090', '100', '472', '487', '096', '091', '081', '999', '791']

for x in range(len(ceps)):
    ddd = ceps[x]
    search_text = "010                                        "+ddd
    # creating a variable and storing the text
    # that we want to add
    replace_text = "010                                65090000"+ddd

    for encoding_type in types_of_encoding:
        # Opening our text file in read only
        # mode using the open() function
        with codecs.open(r'PA_UEOS2022.MAI', 'r', encoding='Latin-1') as file:
            # Reading the content of the file
            # using the read() function and storing
            # them in a new variable
            data = file.read()

            # Searching and replacing the text
            # using the replace() function
            data = data.replace(search_text, replace_text)

        # Opening our text file in write only
        # mode to write the replaced content
        with codecs.open(r'PA_UEOS2022.MAI', 'w', encoding='Latin-1') as file:
            # Writing the replaced data in our
            # text file
            file.write(data)

        # CEP including ends


        # Starts logradouro CORRECTION

        mylist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'X', 'Y', 'W', 'Z']
        for x in range(0, len(mylist)):
            conjunto = "999"
            dados = mylist[x]
            conjunto2 = (conjunto + dados)
            search_text = conjunto2
            replace_text = ("081" + dados)
            for encoding_type in types_of_encoding:
                # Opening our text file in read only
                # mode using the open() function
                with codecs.open(r'PA_UEOS2022.MAI', 'r', encoding='Latin-1') as file:
                    data = file.read()

                    # Searching and replacing the text
                    # using the replace() function
                    data = data.replace(search_text, replace_text)

                # Opening our text file in write only
                # mode to write the replaced content
                with codecs.open(r'PA_UEOS2022.MAI', 'w', encoding='Latin-1') as file:
                    # Writing the replaced data in our
                    # text file
                    file.write(data)


        # Ends Logradouro correction



        # Start CEP correction
        search_text = "010                                65085000"

        # creating a variable and storing the text
        # that we want to add
        replace_text = "010                                65090000"

        for encoding_type in types_of_encoding:
            # Opening our text file in read only
            # mode using the open() function
            with codecs.open(r'PA_UEOS2022.MAI', 'r', encoding='Latin-1') as file:
                # Reading the content of the file
                # using the read() function and storing
                # them in a new variable
                data = file.read()

                # Searching and replacing the text
                # using the replace() function
                data = data.replace(search_text, replace_text)

            # Opening our text file in write only
            # mode to write the replaced content
            with codecs.open(r'PA_UEOS2022.MAI', 'w', encoding='Latin-1') as file:
                # Writing the replaced data in our
                # text file
                file.write(data)
        # Ends CEP correction


        # Printing Text replaced
        print("PROCESSO FINALIZADO!")
