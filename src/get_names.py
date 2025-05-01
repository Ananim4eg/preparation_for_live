import os
import re

PATH_TXT = os.path.join(
    "C:\\Users\\EasyGod\\PycharmProjects\\PythonProject\\preparation_for_live\\", "data\\names.txt"
)
PATH_FOR_SAVE_TXT = "C:\\Users\\EasyGod\\PycharmProjects\\PythonProject\\preparation_for_live\\data\\"

#Свой вариант
def get_all_names_with_file_var1(path: str) -> str:
    """Возвращает все имена из текстового файла"""

    with open(path, "r", encoding="utf-8") as file:

        context = file.readlines()
        context_new = []

        for idx, line in enumerate(context):

            letters_for_del = []
            modified_line = line

            for elem in line:
                if not elem.isalpha():
                    letters_for_del.append(elem)

            for item in letters_for_del:
                modified_line = modified_line.replace(item, "")

            if len(modified_line) > 0:
                context_new.append(modified_line)

    return "\n".join(context_new)


#Вариант с гуглом
def get_all_names_with_file_var2(path: str) -> str:
    """Возвращает все имена из текстового файла"""

    with open(path, "r", encoding="utf-8") as file:

        context = file.read()
        pattern = r"\b[а-я|a-z]*"

        all_names = list(filter(None, re.findall(pattern, context, re.IGNORECASE)))

    return "\n".join(all_names)


def get_sort_names_with_file(path: str):
    """Возвращает имена, сортируя их в алфавитном порядке и раскладывая по двум спискам ру. и анг."""

    with open(path, "r", encoding="utf-8") as file:

        context = file.read()
        pattern_ru_names = r"\b[а-я]*"
        pattern_eng_names = r"\b[a-z]*"

    all_ru_names = list(filter(None, re.findall(pattern_ru_names, context, re.IGNORECASE)))

    all_eng_names = list(filter(None, re.findall(pattern_eng_names, context, re.IGNORECASE)))

    with open(PATH_FOR_SAVE_TXT + "ru_names.txt", 'w', encoding="utf-8") as ru_names:

        ru_names.write('\n'.join(sorted(all_ru_names)))

    with open(PATH_FOR_SAVE_TXT + "eng_names.txt", 'w', encoding="utf-8") as eng_names:

        eng_names.write('\n'.join(sorted(all_eng_names)))

get_sort_names_with_file(PATH_TXT)