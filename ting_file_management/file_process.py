import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    list = []
    line = txt_importer(path_file)

    for length in range(len(instance)):
        if not instance.search(length)["nome_do_arquivo"]:
            return None
        list.append(instance.search(length)["nome_do_arquivo"])

    if path_file not in list:
        file_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(line),
            "linhas_do_arquivo": line,
        }
        instance.enqueue(file_info)
        sys.stdout.write(str(file_info))


def remove(instance):
    if len(instance) > 0:
        file = instance.dequeue()
        file_path = file["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {file_path} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(str(file))

    except IndexError:
        sys.stderr.write("Posição inválida")
