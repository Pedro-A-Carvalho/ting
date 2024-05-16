import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, "r") as file:
            data = [line.strip() for line in file]
        return data
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
