from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return
    data = txt_importer(path_file)
    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }
    instance.enqueue(processed_data)
    print(processed_data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
