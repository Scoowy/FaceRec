import pathlib
import os


def rename_files(path, rename_dirs=False):
    Id = input("Ingresa el Id\n")
    numImg = 1
    print("El directorio activo es " + str(path))
    os.chdir(str(path))
    for f in path.iterdir():
        if rename_dirs and f.is_dir():
            f.rename(str(f) + 'directorio')
        if f.is_file():
            f.rename('User.' + Id + '.' + str(numImg) + f.suffix)
            numImg = numImg + 1


path = pathlib.Path(r'C:/Users/HP-pc/Pictures/Camera Roll')
rename_files(path)
