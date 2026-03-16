import os


def listar_diretorio(path, level=0):
    spaces = "  " * level

    try:
        with os.scandir(path) as entries:
            for entry in sorted(entries, key=lambda e: e.name.lower()):
                if entry.is_dir(follow_symlinks=False):
                    print(f"{spaces}[DIR] {entry.name}")
                    listar_diretorio(entry.path, level + 1)
                else:
                    print(f"{spaces}- {entry.name}")
    except PermissionError:
        print(f"{spaces}[sem permissão]")


listar_diretorio("D:/_infnet/26E1_26E2/Velocidade e Qualidade com Estruturas de Dados e Algoritmos/_codigo/tp03")
