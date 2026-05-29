# Basic Control

This folder contains examples of basic clingo Control usage.

## Files

- `load_ground_solve.py` - Load an ASP program from file, ground it, and solve for all answer sets
- `basic_prog.lp` - Simple ASP program with choice rules and negation

## Usage

```sh
python load_ground_solve.py basic_prog.lp
```

## Concepts

- **clingo.Control**: Main interface for controlling grounding/solving process
- **ctl.add()**: Add ASP program parts to the control object
- **ctl.ground()**: Ground the program
- **ctl.solve()**: Solve the program and iterate over models
