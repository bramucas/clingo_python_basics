# Model Exploration

This folder contains examples of how to explore and filter atoms in answer set models.

## Files

- `exploring_models.py` - Example of filtering atoms by name and arity from models
- `basic_prog.lp` - Simple ASP program (same as in 01_basic_control)

## Usage

```sh
python exploring_models.py ../01_basic_control/basic_prog.lp
```

## Concepts

- **model.symbols(atoms=True)**: Retrieve all atoms from a model (ignoring #show statements)
- **atom.name**: Get the predicate name of an atom
- **atom.arguments**: Access the arguments of an atom (indexed list)
- **Filtering atoms**: Check atom name and arity to process specific predicates
