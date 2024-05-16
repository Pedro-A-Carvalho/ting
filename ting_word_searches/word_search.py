def exists_word(word, instance):
    """Aqui irá sua implementação"""
    data = []
    # if not word:
    #     return []
    for index in range(len(instance)):
        current = instance.search(index)
        current_data = {
            "palavra": word,
            "arquivo": current["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index_line, line in enumerate(current["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                current_data["ocorrencias"].append({"linha": index_line + 1})
        if current_data["ocorrencias"]:
            data.append(current_data)
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
