# clingo_python_basics
Basic stuff about clingo API

## Installation of clingo

```sh
python -m pip install clingo
```
or, if you use conda
```sh
conda install -c potassco clingo
```

## Small example

```python
# load_ground_solve.py

import sys
import clingo

# Reads the program given by command line
with open(sys.argv[1], "r") as f:
    ASP_program = f.read()

# Control object is a low-level interface for controlling the grounding/solving process.
ctl = clingo.Control(
    arguments=['-n', '0'],  # Here you can write the arguments you would pass to clingo by command line.
)

ctl.add("base", [], ASP_program)  # Adds the program to the control object.

ctl.ground([("base", [])])  # Grounding...

# Solving...
with ctl.solve(yield_=True) as solution_iterator:
        nanswer=1
        for model in solution_iterator:
            # Model is an instance of clingo.solving.Model class 
            # Reference: https://potassco.org/clingo/python-api/current/clingo/solving.html#clingo.solving.Model
            print(f'Answer {nanswer}')
            print(model)
            nanswer+=1
```

## Usage

```sh
python load_ground_solve.py basic_prog.lp
```

```sh
python exploring_models.py basic_prog.lp
```
