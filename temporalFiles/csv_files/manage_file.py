from pathlib import Path
from os import path


class FILES:
    file_1 = 'file_1.csv'
    file_2 = 'file_2.csv'
    file_3 = 'file_3.csv'
    canal_10_file_1 = 'canal_10/file_1.csv'
    canal_20_file_1 = 'canal_20/minable/file_1.csv'
    canal_10_anyName = 'canal_10/csv_{}.csv'


def make_dir_exist(file_path: str):
    destination_path = Path(file_path).parent.absolute()
    if destination_path.exists() is False:
        destination_path.mkdir(777, True, True)

    return destination_path.exists()


def getPath(_path):
    if _path is not None and _path is not '':
        if _path in list(vars(FILES).values()):
            currentPath = Path(__file__).parent.absolute()
            resultPath = path.join(currentPath, _path)
            if make_dir_exist(resultPath) is True:
                return resultPath
            raise Exception('No se pudo crear Directorio')
        raise Exception('query no registrada en mantenedor QUERY')
    raise Exception('parametro Query invalido')
