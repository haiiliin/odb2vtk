import sys
from pathlib import Path

from abqpy.cli import abaqus


def main():
    odb2vtk = str(Path(__file__).parent.resolve() / "odb2vtk.py")
    argv = sys.argv
    if "--step" in argv and len(argv) > argv.index("--step") + 1:
        idx = argv.index("--step")
        argv[idx + 1] = f'"{argv[idx + 1]}"'
    abaqus.python(odb2vtk, *argv[1:])


if __name__ == "__main__":
    main()
