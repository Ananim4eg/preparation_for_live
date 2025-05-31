import re

PATH_TXT = "C:\\Users\\EasyGod\\PycharmProjects\\PythonProject\\preparation_for_live\\data\\names.txt"
PATH_FOR_SAVE_TXT = "C:\\Users\\EasyGod\\PycharmProjects\\PythonProject\\preparation_for_live\\data\\"


# Свой вариант
def get_all_names_from_file_var1(path: str) -> str:
    """Возвращает все имена из текстового файла"""

    with open(path, "r", encoding="utf-8") as file:

        context = file.readlines()
        context_new = []

        for line in context:

            letters_for_del = []

            for elem in line:
                if not elem.isalpha():
                    letters_for_del.append(elem)

            for item in letters_for_del:
                line = line.replace(item, "")

            if len(line):
                context_new.append(line)

    return "\n".join(context_new)


# Вариант с гуглом
def get_all_names_from_file_var2(path: str) -> str:
    """Возвращает все имена из текстового файла"""

    with open(path, "r", encoding="utf-8") as file:

        context = file.read()
        pattern = r"\b[а-я|a-z]*"

        all_names: list = list(filter(None, re.findall(pattern, context, re.IGNORECASE)))

    return "\n".join(all_names)


def get_sort_names_from_file(path: str, mode: str | None = None) -> None:
    """Возвращает имена, сортируя их в алфавитном порядке и раскладывая по двум спискам ру. или анг."""

    with open(path, "r", encoding="utf-8") as file:

        context = file.read()

    if mode is None:
        get_ru_sort_names_from_file(context)
        get_eng_sort_names_from_file(context)

    elif mode.lower() == "ru":
        get_ru_sort_names_from_file(context)

    elif mode.lower() == "eng":
        get_eng_sort_names_from_file(context)


def get_ru_sort_names_from_file(my_list: str) -> None:
    """Выбирает русские имена, сортирует их и записывает в файл"""
    pattern_ru_names = r"\b[а-я|ё]*"

    all_ru_names: list = list(filter(None, re.findall(pattern_ru_names, my_list, re.IGNORECASE)))

    with open(PATH_FOR_SAVE_TXT + "ru_names.txt", "w", encoding="utf-8") as ru_names:
        ru_names.write("\n".join(sorted(all_ru_names)))


def get_eng_sort_names_from_file(my_list: str) -> None:
    """Выбирает английские имена, сортирует их и записывает в файл"""
    pattern_eng_names = r"\b[a-z]*"

    all_eng_names: list = list(filter(None, re.findall(pattern_eng_names, my_list, re.IGNORECASE)))

    with open(PATH_FOR_SAVE_TXT + "eng_names.txt", "w", encoding="utf-8") as eng_names:
        eng_names.write("\n".join(sorted(all_eng_names)))


# get_sort_names_with_file(PATH_TXT)
print(get_all_names_from_file_var1(PATH_TXT))
