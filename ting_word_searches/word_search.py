def exists_word(word, instance):
    list = []
    lower = word.lower()

    for length in range(len(instance)):
        file = instance.search(length)
        info = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1}
                for index, file_line in enumerate(file["linhas_do_arquivo"])
                if lower in file_line.lower()
            ],
        }

        if info["ocorrencias"]:
            list.append(info)

    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
