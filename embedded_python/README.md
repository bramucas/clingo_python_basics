# Embedded Python

This folder contains examples of using Python code from within ASP programs using the @-syntax.

## Files

- `embedded_python.py` - Example showing how to call Python functions from ASP

## Usage

```sh
python embedded_python.py
```

## Concepts

- **Context class**: Python class with methods callable from ASP using @-syntax
- **@function()**: Call Python functions during grounding
- **context parameter**: Pass context object to ctl.ground() to make functions available
- **on_model callback**: Function called for each model found during solving
