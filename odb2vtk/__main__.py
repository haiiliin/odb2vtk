import sys
from pathlib import Path

from abqpy.cli import abaqus


def main():
    odb2vtk = str(Path(__file__).parent.resolve() / "odb2vtk.py")
    argv = sys.argv
    for i in range(1, len(argv)):
        if " " in argv[i]:
            argv[i] = f'"{argv[i]}"'
    abaqus.python(odb2vtk, *argv[1:])


if __name__ == "__main__":
    main()
