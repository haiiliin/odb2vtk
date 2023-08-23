import sys
from pathlib import Path

from abqpy.cli import abaqus


def main():
    odb2vtk = str(Path(__file__).parent.resolve() / "odb2vtk.py")
    abaqus.python(odb2vtk, *sys.argv[1:])


if __name__ == "__main__":
    main()
