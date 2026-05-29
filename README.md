# clingo_python_basics
Basic examples of the clingo Python API

## Installation of clingo

```sh
python -m pip install clingo
```
or, if you use conda
```sh
conda install -c potassco clingo
```

## Example Structure

This repository is organized into folders covering different aspects of the clingo Python API:

- **basic_control** - Basic Control usage: load, ground, and solve ASP programs
- **model_exploration** - How to explore and filter atoms in answer set models
- **projection** - Using the #project directive for answer set projection
- **embedded_python** - Calling Python functions from ASP using @-syntax
- **multishot_solving** - Incremental grounding and solving (multi-shot ASP)

## Usage

Each folder contains a README with specific usage instructions. For example:

```sh
cd basic_control
python load_ground_solve.py basic_prog.lp
```

```sh
cd model_exploration
python exploring_models.py ../basic_control/basic_prog.lp
```
