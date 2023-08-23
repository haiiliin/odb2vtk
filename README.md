# odb2vtk

A python wrapper package for the [ODB2VTK](https://github.com/Arris-Composites/ODB2VTK) library.

## Installation

```sh
pip install git+https://github.com/haiiliin/odb2vtk.git@main
```

## Usage

Use the `odb2vtk` command to convert an ODB file to a VTK file.

```sh
$ odb2vtk

usage: odb2vtk.py [-h] --header HEADER [--instance [INSTANCE [INSTANCE ...]]]
                  [--step [STEP [STEP ...]]] [--writeHistory WRITEHISTORY]
                  --odbFile ODBFILE [--writePVD WRITEPVD] [--suffix SUFFIX]
```

Use the `odb2vtk-multiprocess` command for the multiprocessing version.

```sh
$ odb2vtk-multiprocess

usage: odb2vtk-multiprocess [-h] --header HEADER [--instance [INSTANCE ...]]
                            [--step [STEP ...]] [--writeHistory WRITEHISTORY]
                            --odbFile ODBFILE [--suffix SUFFIX]
```
