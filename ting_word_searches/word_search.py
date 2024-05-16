def search_word(word, instance, content=False):
    data = []
    for index in range(len(instance)):
        current = instance.search(index)
        current_data = {
            "palavra": word,
            "arquivo": current["nome_do_arquivo"],
            "ocorrencias": [],
        }
        current_data["ocorrencias"] = word_in_lines(
            word, current["linhas_do_arquivo"], content
        )
        if current_data["ocorrencias"]:
            data.append(current_data)
    return data


def word_in_lines(word, lines, content):
    occourences = []
    for index_line, line in enumerate(lines):
        if word.lower() in line.lower():
            occourence = {"linha": index_line + 1}
            if content:
                occourence["conteudo"] = line
            occourences.append(occourence)
    return occourences


def exists_word(word, instance):
    return search_word(word, instance)


def search_by_word(word, instance):
    return search_word(word, instance, True)
