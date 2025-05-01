import os


PATH_FOR_TXT = os.path.join("C:\\Users\EasyGod\PycharmProjects\PythonProject\preparation_for_live\\", "data\\names.txt")


def get_all_names_with_file(my_list: str) -> str:
    """ Возвращает имена из текстового файла"""

    with open(PATH_FOR_TXT, "r", encoding='utf-8') as file:

        context = file.readlines()
        context_new = []

        for idx, line in enumerate(context):

            letters_for_del = []
            modified_line = line

            for elem in line:
                if not elem.isalpha():
                    letters_for_del.append(elem)

            for item in letters_for_del:
                modified_line = modified_line.replace(item,'')

            if len(modified_line) > 0:
                context_new.append(modified_line)

    return '\n'.join(context_new)

