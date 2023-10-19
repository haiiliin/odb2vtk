# odb2vtk

A python wrapper package for the [ODB2VTK](https://github.com/Arris-Composites/ODB2VTK) library.

## Installation

```sh
pip install odb2vtk
```

## Usage

Use the `odb2vtk` command to convert an ODB file to a VTK file.

```sh
$ odb2vtk --help

usage: odb2vtk.py [-h] [--header HEADER] [--instance [INSTANCE [INSTANCE ...]]]
                  [--step [STEP [STEP ...]]] [--writeHistory WRITEHISTORY]
                  --odbFile ODBFILE [--writePVD WRITEPVD] [--suffix SUFFIX]

optional arguments:
  -h, --help            show this help message and exit
  --header HEADER       if 1, extract header information and generate a .json
                        file. Otherwise, generate .vtu file. By default 0
  --instance [INSTANCE [INSTANCE ...]]
                        selected instance names which are separated by
                        whitespace, e.g. 'instanceName1' 'instanceName2'
  --step [STEP [STEP ...]]
                        selected step names and frames which are separated by
                        whitespace, e.g., 'step1:1,2,3' 'step2:2,3,4'. The
                        frames can be any valid Python expression that can be
                        evaluated to an integer iterable, e.g., 'range(1, 10)'
  --writeHistory WRITEHISTORY
                        if 1, write history output.
  --odbFile ODBFILE     selected odb file (full path name)
  --writePVD WRITEPVD   if 1 write a pvd file
  --suffix SUFFIX       string appended to the file
```

Use the `odb2vtk-multiprocess` command for the multiprocessing version.

```sh
$ odb2vtk-multiprocess --help

usage: odb2vtk-multiprocess [-h] [--header HEADER] [--instance [INSTANCE ...]]
                            [--step [STEP ...]] [--writeHistory WRITEHISTORY]
                            --odbFile ODBFILE [--suffix SUFFIX]

options:
  -h, --help            show this help message and exit
  --header HEADER       if 1, extract header information and generate a .json
                        file. Otherwise, generate .vtu file. By default 0
  --instance [INSTANCE ...]
                        selected instance names which are separated by
                        whitespace, e.g. 'instanceName1' 'instanceName2'
  --step [STEP ...]     selected step names and frames which are separated by
                        whitespace, e.g., 'step1:1,2,3' 'step2:2,3,4'. The
                        frames can be any valid Python expression that can be
                        evaluated to an integer iterable, e.g., 'range(1, 10)'
  --writeHistory WRITEHISTORY
                        if 1, write history output.
  --odbFile ODBFILE     selected odb file (full path name)
  --suffix SUFFIX       string appended to the file
```
