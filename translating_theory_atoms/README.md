# Translating Theory Atoms

This folder contains examples of parsing and translating theory atoms in ASP programs using the clingo Python API.

## Files

- `example.lp` - ASP program with a theory atom using the `&dl` operator
- `parse_and_translate.py` - Python script that parses the ASP program and translates theory atoms

## Usage

```sh
python parse_and_translate.py
```

## Concepts

- **Theory atoms**: Custom theory extensions in ASP (e.g., `&dl{ q & -p | r }`)
- **AST parsing**: Using `clingo.ast.parse_string` to parse ASP programs into Abstract Syntax Trees
- **AST transformation**: Traversing the AST and modifying nodes (e.g., replacing theory atoms with regular literals)
- **SymbolicTerm**: AST node representing a symbol (function, number, etc.)
- **SymbolicAtom**: AST node representing an atom with a symbolic term
- **Literal**: AST node representing a literal (positive or negative)

## Example

The script parses `example.lp` which contains:
```
b.
a :- &dl{ q & -p | r}, b.
```

It detects the `&dl` theory atom and translates it into a regular literal `@whatever(1,2,3)`, producing:
```
b.
a :- not @whatever(1,2,3).
```

This demonstrates how to implement custom theory atom handling by translating them into standard ASP constructs.
