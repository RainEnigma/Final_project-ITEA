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
    print(list_rows_with_similar)