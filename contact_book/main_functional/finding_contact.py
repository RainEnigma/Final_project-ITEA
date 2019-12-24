import file_operstions


def finding_obj(word):
    o_dict_contacts = file_operstions.File.finding_contact(None)
    list_rows_with_similar = []
    for num_of_row, list_rows in enumerate(o_dict_contacts):
        for id in dict(list_rows).values():
            if id == word:
                list_rows_with_similar.append(num_of_row)
                print()
                for m_keys, m_value in dict(o_dict_contacts[num_of_row]).items():
                    print(f"{m_keys} - {m_value}")
    if len(list_rows_with_similar) > 1:
        clarification_word = input(
            f"There are {len(list_rows_with_similar)} same contacts, please enter another word:")
        for num in list_rows_with_similar:
            print(clarification_word)
            if clarification_word in dict(o_dict_contacts[num]).values():
                print()
                for my_key,my_value in dict(o_dict_contacts[num]).items():
                    print(f"{my_key} - {my_value}")
                print()
